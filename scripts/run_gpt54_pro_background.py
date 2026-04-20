#!/usr/bin/env python3
"""Submit and monitor GPT-5.4 Pro background reasoning jobs per LaTeX problem."""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
import html
import json
import os
import re
import sys
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from typing import Any
from urllib.parse import parse_qs, urlparse
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


SYSTEM_PROMPT = (
    "You are an expert mathematician working on an Erdős problem. "
    "Try to solve the problem fully. If a complete solution is not reached, produce the best "
    "viable proof sketch you can. As soon as you have a viable proof sketch, stop and output it "
    "instead of continuing to explore. "
    "Output in Markdown. The final line must be exactly one of: "
    "Status: Solved or Status: Proof Sketch or Status: Failed"
)

STATUS_RE = re.compile(r"^Status:\s*(Solved|Proof Sketch|Failed)\s*$", re.IGNORECASE)
NON_TERMINAL = {"queued", "in_progress"}
TERMINAL = {"completed", "failed", "cancelled", "incomplete"}


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Submit and monitor GPT-5.4 Pro background jobs for Erdos problems."
    )
    parser.add_argument(
        "--state-file",
        type=Path,
        default=Path("data/gpt54_pro_background_jobs.json"),
        help="JSON file storing background job state.",
    )
    parser.add_argument(
        "--problems-jsonl",
        type=Path,
        default=Path("data/unsolved.jsonl"),
        help="JSONL with problem records containing number and latex.",
    )
    parser.add_argument(
        "--solutions-dir",
        type=Path,
        default=Path("data/solutions"),
        help="Base directory where per-problem markdown outputs are written.",
    )
    parser.add_argument(
        "--output-filename",
        default="gpt54_pro_background.md",
        help="Output markdown filename under each problem directory.",
    )
    parser.add_argument(
        "--api-base",
        default="https://api.openai.com/v1",
        help="OpenAI API base URL.",
    )
    parser.add_argument(
        "--model",
        default="gpt-5.4-pro",
        help="Responses model used for background jobs.",
    )
    parser.add_argument(
        "--reasoning-effort",
        default="xhigh",
        choices=["medium", "high", "xhigh"],
        help="Reasoning effort for the model.",
    )
    parser.add_argument(
        "--max-runtime-seconds",
        type=int,
        default=14400,
        help="Mark jobs failed if they remain non-terminal longer than this.",
    )
    parser.add_argument(
        "--request-timeout",
        type=float,
        default=120.0,
        help="HTTP timeout (seconds) for submit/retrieve/cancel calls.",
    )
    parser.add_argument(
        "--max-problems",
        type=int,
        default=0,
        help="Max number of problems to submit (0 means all).",
    )
    parser.add_argument(
        "--submit-interval-seconds",
        type=float,
        default=0.0,
        help="Delay between each submit attempt to avoid burst traffic.",
    )
    parser.add_argument(
        "--submit-max-retries",
        type=int,
        default=5,
        help="Max retries per problem when submit is rate-limited (HTTP 429).",
    )
    parser.add_argument(
        "--submit-retry-seconds",
        type=float,
        default=10.0,
        help="Backoff delay between submit retries after HTTP 429.",
    )
    parser.add_argument(
        "--max-active-jobs",
        type=int,
        default=0,
        help="Maximum queued/in-progress jobs allowed during submit (0 disables cap).",
    )
    parser.add_argument(
        "--submit-wait-seconds",
        type=float,
        default=15.0,
        help="How long submit waits before re-checking active job capacity.",
    )
    parser.add_argument(
        "--force-submit",
        action="store_true",
        help="Submit even if a job already exists for that problem number.",
    )
    parser.add_argument(
        "--interval",
        type=float,
        default=5.0,
        help="Dashboard refresh/poll interval in seconds.",
    )
    parser.add_argument(
        "--web-host",
        default="127.0.0.1",
        help="Host/interface for web dashboard server.",
    )
    parser.add_argument(
        "--web-port",
        type=int,
        default=8765,
        help="Port for web dashboard server.",
    )
    parser.add_argument(
        "--web-refresh-seconds",
        type=float,
        default=3.0,
        help="Client-side refresh interval for web dashboard.",
    )
    parser.add_argument(
        "--until-done",
        action="store_true",
        help="For dashboard: keep polling until all jobs are terminal.",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)
    subparsers.add_parser("submit", help="Submit background jobs for problems.")
    subparsers.add_parser(
        "dashboard",
        help="Poll jobs, render dashboard, and write completed outputs to disk.",
    )
    subparsers.add_parser(
        "web-dashboard",
        help="Run local web app to view job states and results from state file.",
    )
    return parser.parse_args()


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        raise FileNotFoundError(f"Problems JSONL not found: {path}")
    records: list[dict[str, Any]] = []
    with path.open("r", encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, start=1):
            stripped = line.strip()
            if not stripped:
                continue
            try:
                value = json.loads(stripped)
            except json.JSONDecodeError as exc:
                raise ValueError(f"Invalid JSON at line {line_number}: {exc}") from exc
            if isinstance(value, dict):
                records.append(value)
    return records


def load_state(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {"created_at": now_iso(), "jobs": []}
    with path.open("r", encoding="utf-8") as handle:
        value = json.load(handle)
    if not isinstance(value, dict):
        raise ValueError(f"State file must be a JSON object: {path}")
    jobs = value.get("jobs")
    if not isinstance(jobs, list):
        value["jobs"] = []
    return value


def save_state(path: Path, state: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temp_path = path.with_suffix(path.suffix + ".tmp")
    with temp_path.open("w", encoding="utf-8") as handle:
        json.dump(state, handle, ensure_ascii=False, indent=2)
        handle.write("\n")
    temp_path.replace(path)


def build_user_prompt(number: str, latex: str) -> str:
    return (
        f"Problem number: {number}\n\n"
        "Problem statement (LaTeX):\n"
        f"{latex}\n\n"
        "Task: Solve this problem. If you cannot complete a full solution, provide the best viable "
        "proof sketch and stop there.\n"
        "Remember: your final line must be exactly one of: "
        "Status: Solved or Status: Proof Sketch or Status: Failed"
    )


def request_json(
    *,
    method: str,
    url: str,
    api_key: str,
    timeout: float,
    payload: dict[str, Any] | None = None,
) -> dict[str, Any]:
    body = None if payload is None else json.dumps(payload).encode("utf-8")
    request = Request(
        url,
        data=body,
        method=method,
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
    )
    try:
        with urlopen(request, timeout=timeout) as response:
            raw = response.read().decode("utf-8")
            data = json.loads(raw)
    except HTTPError as exc:
        detail = ""
        try:
            detail = exc.read().decode("utf-8", errors="replace")
        except Exception:
            detail = ""
        raise RuntimeError(f"HTTP {exc.code}: {detail}") from exc
    except (URLError, TimeoutError, json.JSONDecodeError) as exc:
        raise RuntimeError(f"Request failed: {exc}") from exc
    if not isinstance(data, dict):
        raise RuntimeError("API response must be a JSON object")
    return data


def create_background_response(
    *,
    api_base: str,
    api_key: str,
    model: str,
    reasoning_effort: str,
    number: str,
    latex: str,
    timeout: float,
) -> dict[str, Any]:
    payload = {
        "model": model,
        "background": True,
        "store": True,
        "reasoning": {"effort": reasoning_effort},
        "input": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": build_user_prompt(number, latex)},
        ],
    }
    url = f"{api_base.rstrip('/')}/responses"
    return request_json(method="POST", url=url, api_key=api_key, timeout=timeout, payload=payload)


def retrieve_response(*, api_base: str, api_key: str, response_id: str, timeout: float) -> dict[str, Any]:
    url = f"{api_base.rstrip('/')}/responses/{response_id}"
    return request_json(method="GET", url=url, api_key=api_key, timeout=timeout)


def cancel_response(*, api_base: str, api_key: str, response_id: str, timeout: float) -> dict[str, Any]:
    url = f"{api_base.rstrip('/')}/responses/{response_id}/cancel"
    return request_json(method="POST", url=url, api_key=api_key, timeout=timeout)


def extract_output_text(response_data: dict[str, Any]) -> str:
    output_text = response_data.get("output_text")
    if isinstance(output_text, str) and output_text.strip():
        return output_text.strip()
    output = response_data.get("output")
    chunks: list[str] = []
    if isinstance(output, list):
        for item in output:
            if not isinstance(item, dict):
                continue
            content = item.get("content")
            if isinstance(content, str) and content.strip():
                chunks.append(content.strip())
                continue
            if not isinstance(content, list):
                continue
            for block in content:
                if not isinstance(block, dict):
                    continue
                text = block.get("text")
                if isinstance(text, str) and text.strip():
                    chunks.append(text.strip())
    return "\n\n".join(chunks).strip()


def extract_model_status(text: str) -> str | None:
    found: str | None = None
    for line in text.splitlines():
        match = STATUS_RE.match(line.strip())
        if match:
            value = match.group(1).lower()
            if value == "solved":
                found = "Solved"
            elif value == "proof sketch":
                found = "Proof Sketch"
            elif value == "failed":
                found = "Failed"
    return found


def write_markdown_output(path: Path, number: str, response_text: str, model_status: str | None) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    status_line = f"Status: {model_status}" if model_status else "Status: (missing)"
    header = f"# GPT-5.4 Pro Background Result for Problem {number}\n\n{status_line}\n\n---\n\n"
    path.write_text(header + response_text.strip() + "\n", encoding="utf-8")


def problem_sort_key(value: str):
    return (0, int(value)) if value.isdigit() else (1, value)


def run_submit(args: argparse.Namespace, api_key: str) -> None:
    records = load_jsonl(args.problems_jsonl)
    state = load_state(args.state_file)
    jobs = state.setdefault("jobs", [])
    if not isinstance(jobs, list):
        raise ValueError("State field 'jobs' must be a list")

    existing_numbers = {
        str(job.get("number", "")).strip()
        for job in jobs
        if isinstance(job, dict) and str(job.get("number", "")).strip()
    }

    filtered: list[dict[str, str]] = []
    for record in records:
        number = str(record.get("number", "")).strip()
        latex = str(record.get("latex", "")).strip()
        if not number or not latex:
            continue
        if not args.force_submit and number in existing_numbers:
            continue
        filtered.append({"number": number, "latex": latex})

    filtered.sort(key=lambda item: problem_sort_key(item["number"]))
    if args.max_problems > 0:
        filtered = filtered[: args.max_problems]

    total = len(filtered)
    if total == 0:
        print("No problems to submit.", file=sys.stderr)
        return

    submitted = 0
    failed = 0
    started_at = now_iso()
    print(
        (
            f"Submitting {total} background jobs with model={args.model}. "
            f"submit_interval={args.submit_interval_seconds}s "
            f"max_retries={args.submit_max_retries} retry_delay={args.submit_retry_seconds}s "
            f"max_active_jobs={args.max_active_jobs} submit_wait={args.submit_wait_seconds}s"
        ),
        file=sys.stderr,
    )
    for index, item in enumerate(filtered, start=1):
        number = item["number"]
        latex = item["latex"]
        output_path = args.solutions_dir / number / args.output_filename

        while args.max_active_jobs > 0:
            active_jobs = [
                job
                for job in jobs
                if isinstance(job, dict) and str(job.get("response_status", "")).strip() in NON_TERMINAL
            ]
            if not active_jobs:
                break

            for job in active_jobs:
                response_id = str(job.get("response_id", "")).strip()
                if not response_id:
                    continue
                try:
                    data = retrieve_response(
                        api_base=args.api_base,
                        api_key=api_key,
                        response_id=response_id,
                        timeout=args.request_timeout,
                    )
                    previous_status = str(job.get("response_status", "")).strip()
                    new_status = str(data.get("status", previous_status)).strip() or previous_status
                    if new_status != previous_status:
                        job["response_status"] = new_status
                    job["last_polled_at"] = now_iso()
                    if new_status in TERMINAL and not str(job.get("terminal_at", "")).strip():
                        job["terminal_at"] = now_iso()
                except Exception as exc:
                    job["last_error"] = f"retrieve_failed: {exc}"

            save_state(args.state_file, state)
            active_count = sum(
                1
                for job in jobs
                if isinstance(job, dict) and str(job.get("response_status", "")).strip() in NON_TERMINAL
            )
            if active_count < args.max_active_jobs:
                break
            print(
                (
                    f"[{index}/{total}] Waiting for capacity: active={active_count} "
                    f"cap={args.max_active_jobs}; sleeping {args.submit_wait_seconds}s"
                ),
                file=sys.stderr,
            )
            time.sleep(max(0.0, args.submit_wait_seconds))

        attempt = 0
        while True:
            try:
                response_data = create_background_response(
                    api_base=args.api_base,
                    api_key=api_key,
                    model=args.model,
                    reasoning_effort=args.reasoning_effort,
                    number=number,
                    latex=latex,
                    timeout=args.request_timeout,
                )
                response_id = str(response_data.get("id", "")).strip()
                response_status = str(response_data.get("status", "unknown")).strip()
                if not response_id:
                    raise RuntimeError("Missing response id")
                jobs.append(
                    {
                        "number": number,
                        "latex": latex,
                        "response_id": response_id,
                        "response_status": response_status,
                        "submitted_at": now_iso(),
                        "run_started_at": started_at,
                        "output_path": str(output_path),
                        "output_saved": False,
                    }
                )
                submitted += 1
                print(
                    f"[{index}/{total}] Submitted problem {number}: id={response_id}, status={response_status}",
                    file=sys.stderr,
                )
                save_state(args.state_file, state)
                break
            except Exception as exc:
                is_rate_limited = "HTTP 429:" in str(exc)
                if is_rate_limited and attempt < args.submit_max_retries:
                    attempt += 1
                    print(
                        (
                            f"[{index}/{total}] Rate limited for problem {number}; "
                            f"retry {attempt}/{args.submit_max_retries} in {args.submit_retry_seconds}s"
                        ),
                        file=sys.stderr,
                    )
                    time.sleep(max(0.0, args.submit_retry_seconds))
                    continue
                failed += 1
                print(f"[{index}/{total}] Failed submit for {number}: {exc}", file=sys.stderr)
                break

        if index < total and args.submit_interval_seconds > 0:
            time.sleep(args.submit_interval_seconds)

    print(f"Submit done. submitted={submitted}, failed={failed}", file=sys.stderr)
    print(f"State saved at: {args.state_file}", file=sys.stderr)


def parse_time_or_zero(value: Any) -> float:
    if not isinstance(value, str) or not value.strip():
        return 0.0
    try:
        return datetime.fromisoformat(value).timestamp()
    except ValueError:
        return 0.0


def usage_counts(data: dict[str, Any]) -> tuple[int, int, int]:
    usage = data.get("usage")
    if not isinstance(usage, dict):
        return (0, 0, 0)

    input_tokens = usage.get("input_tokens")
    output_tokens = usage.get("output_tokens")
    total_tokens = usage.get("total_tokens")

    input_value = int(input_tokens) if isinstance(input_tokens, int) else 0
    output_value = int(output_tokens) if isinstance(output_tokens, int) else 0
    total_value = int(total_tokens) if isinstance(total_tokens, int) else 0

    if total_value <= 0:
        total_value = input_value + output_value
    return (input_value, output_value, total_value)


def render_bar(done: int, total: int, width: int = 30) -> str:
    if total <= 0:
        return "[------------------------------]"
    done = max(0, min(done, total))
    filled = int(width * done / total)
    return "[" + ("#" * filled) + ("-" * (width - filled)) + "]"


def print_dashboard(state: dict[str, Any]) -> None:
    jobs = [job for job in state.get("jobs", []) if isinstance(job, dict)]
    total = len(jobs)
    counts: dict[str, int] = {}
    for job in jobs:
        status = str(job.get("response_status", "unknown"))
        counts[status] = counts.get(status, 0) + 1
    terminal = sum(counts.get(value, 0) for value in TERMINAL)
    queued = counts.get("queued", 0)
    in_progress = counts.get("in_progress", 0)
    bar = render_bar(terminal, total)
    print(f"{bar} done={terminal}/{total} queued={queued} in_progress={in_progress}")
    print(
        "completed={} failed={} cancelled={} incomplete={}".format(
            counts.get("completed", 0),
            counts.get("failed", 0),
            counts.get("cancelled", 0),
            counts.get("incomplete", 0),
        )
    )
    input_total = sum(int(job.get("usage_input_tokens", 0) or 0) for job in jobs)
    output_total = sum(int(job.get("usage_output_tokens", 0) or 0) for job in jobs)
    tokens_total = sum(int(job.get("usage_total_tokens", 0) or 0) for job in jobs)
    usage_reported = sum(
        1
        for job in jobs
        if any(int(job.get(key, 0) or 0) > 0 for key in ("usage_input_tokens", "usage_output_tokens", "usage_total_tokens"))
    )
    print(
        f"tokens input={input_total} output={output_total} total={tokens_total} reported_for={usage_reported}/{total}"
    )
    active = [job for job in jobs if str(job.get("response_status", "")) in NON_TERMINAL]
    active.sort(key=lambda job: problem_sort_key(str(job.get("number", ""))))
    if active:
        print("Active jobs:")
        now_ts = time.time()
        for job in active[:20]:
            number = str(job.get("number", ""))
            response_id = str(job.get("response_id", ""))
            submitted_ts = parse_time_or_zero(job.get("submitted_at"))
            elapsed = int(max(0.0, now_ts - submitted_ts)) if submitted_ts > 0 else 0
            print(f"  - {number}: {job.get('response_status', 'unknown')} elapsed={elapsed}s id={response_id}")


def job_identity(job: dict[str, Any]) -> str:
    response_id = str(job.get("response_id", "")).strip()
    if response_id:
        return f"id:{response_id}"
    number = str(job.get("number", "")).strip()
    submitted_at = str(job.get("submitted_at", "")).strip()
    return f"number:{number}|submitted_at:{submitted_at}"


def run_dashboard(args: argparse.Namespace, api_key: str) -> None:
    loop = True
    while loop:
        state = load_state(args.state_file)
        jobs = state.get("jobs", [])
        if not isinstance(jobs, list):
            raise ValueError("State field 'jobs' must be a list")
        if not jobs:
            print("\033[2J\033[H", end="")
            print(f"Dashboard refreshed at {now_iso()}")
            print(f"State file: {args.state_file}")
            print("No jobs in state file yet.")
            if not args.until_done:
                break
            time.sleep(max(0.5, args.interval))
            continue

        state_changed = False
        for job in jobs:
            if not isinstance(job, dict):
                continue
            response_id = str(job.get("response_id", "")).strip()
            status = str(job.get("response_status", "")).strip()
            if not response_id:
                continue
            if status not in NON_TERMINAL and status in TERMINAL:
                if status == "completed" and not bool(job.get("output_saved", False)):
                    text = str(job.get("response_text", "")).strip()
                    if not text:
                        try:
                            data = retrieve_response(
                                api_base=args.api_base,
                                api_key=api_key,
                                response_id=response_id,
                                timeout=args.request_timeout,
                            )
                            text = extract_output_text(data)
                            if text:
                                job["response_text"] = text
                            input_tokens, output_tokens, total_tokens = usage_counts(data)
                            if input_tokens > 0 or output_tokens > 0 or total_tokens > 0:
                                if int(job.get("usage_input_tokens", 0) or 0) != input_tokens:
                                    job["usage_input_tokens"] = input_tokens
                                if int(job.get("usage_output_tokens", 0) or 0) != output_tokens:
                                    job["usage_output_tokens"] = output_tokens
                                if int(job.get("usage_total_tokens", 0) or 0) != total_tokens:
                                    job["usage_total_tokens"] = total_tokens
                            job["last_polled_at"] = now_iso()
                            state_changed = True
                        except Exception as exc:
                            job["last_error"] = f"retrieve_failed: {exc}"
                            state_changed = True
                            continue
                    if text:
                        model_status = extract_model_status(text)
                        output_path = Path(str(job.get("output_path", "")).strip())
                        number = str(job.get("number", "")).strip()
                        write_markdown_output(output_path, number, text, model_status)
                        job["output_saved"] = True
                        job["model_status"] = model_status
                        state_changed = True
                continue

            submitted_ts = parse_time_or_zero(job.get("submitted_at"))
            now_ts = time.time()
            if submitted_ts > 0 and status in NON_TERMINAL and now_ts - submitted_ts > args.max_runtime_seconds:
                timeout_at = now_iso()
                job["timeout_exceeded_at"] = timeout_at
                job["failure_reason"] = "max_runtime_exceeded"
                job["cancel_requested_at"] = timeout_at
                try:
                    cancel_data = cancel_response(
                        api_base=args.api_base,
                        api_key=api_key,
                        response_id=response_id,
                        timeout=args.request_timeout,
                    )
                    job["cancel_response_status"] = str(cancel_data.get("status", "unknown"))
                    job["cancelled_at"] = now_iso()
                except Exception as exc:
                    job["cancel_error"] = f"cancel_failed: {exc}"
                job["response_status"] = "failed"
                job["failed_at"] = now_iso()
                job["terminal_at"] = now_iso()
                state_changed = True
                continue

            try:
                data = retrieve_response(
                    api_base=args.api_base,
                    api_key=api_key,
                    response_id=response_id,
                    timeout=args.request_timeout,
                )
            except Exception as exc:
                job["last_error"] = f"retrieve_failed: {exc}"
                state_changed = True
                continue

            new_status = str(data.get("status", status)).strip() or status
            if new_status != status:
                job["response_status"] = new_status
                state_changed = True
            input_tokens, output_tokens, total_tokens = usage_counts(data)
            if input_tokens > 0 or output_tokens > 0 or total_tokens > 0:
                if int(job.get("usage_input_tokens", 0) or 0) != input_tokens:
                    job["usage_input_tokens"] = input_tokens
                    state_changed = True
                if int(job.get("usage_output_tokens", 0) or 0) != output_tokens:
                    job["usage_output_tokens"] = output_tokens
                    state_changed = True
                if int(job.get("usage_total_tokens", 0) or 0) != total_tokens:
                    job["usage_total_tokens"] = total_tokens
                    state_changed = True
            job["last_polled_at"] = now_iso()
            if new_status in TERMINAL:
                job["terminal_at"] = now_iso()

            if new_status == "completed":
                text = extract_output_text(data)
                job["response_text"] = text
                model_status = extract_model_status(text)
                job["model_status"] = model_status
                output_path = Path(str(job.get("output_path", "")).strip())
                number = str(job.get("number", "")).strip()
                write_markdown_output(output_path, number, text, model_status)
                job["output_saved"] = True
                state_changed = True

            if new_status != "completed":
                error_data = data.get("error")
                if isinstance(error_data, dict) and error_data:
                    job["response_error"] = error_data
                    state_changed = True

        if state_changed:
            latest_state = load_state(args.state_file)
            latest_jobs = latest_state.get("jobs", [])
            if isinstance(latest_jobs, list):
                known = {
                    job_identity(job)
                    for job in state.get("jobs", [])
                    if isinstance(job, dict)
                }
                for latest_job in latest_jobs:
                    if not isinstance(latest_job, dict):
                        continue
                    identity = job_identity(latest_job)
                    if identity in known:
                        continue
                    state.setdefault("jobs", []).append(latest_job)
                    known.add(identity)
            save_state(args.state_file, state)

        print("\033[2J\033[H", end="")
        print(f"Dashboard refreshed at {now_iso()}")
        print(f"State file: {args.state_file}")
        print_dashboard(state)

        jobs = [job for job in state.get("jobs", []) if isinstance(job, dict)]
        all_terminal = all(str(job.get("response_status", "")) in TERMINAL for job in jobs)
        if not args.until_done:
            break
        if all_terminal:
            break
        time.sleep(max(0.5, args.interval))


def jobs_for_web(state: dict[str, Any]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    jobs = [job for job in state.get("jobs", []) if isinstance(job, dict)]
    jobs.sort(key=lambda job: problem_sort_key(str(job.get("number", "")).strip()))
    for job in jobs:
        number = str(job.get("number", "")).strip()
        output_path = str(job.get("output_path", "")).strip()
        output_exists = False
        if output_path:
            output_exists = Path(output_path).is_file()
        rows.append(
            {
                "number": number,
                "response_id": str(job.get("response_id", "")).strip(),
                "response_status": str(job.get("response_status", "")).strip() or "unknown",
                "submitted_at": str(job.get("submitted_at", "")).strip(),
                "terminal_at": str(job.get("terminal_at", "")).strip(),
                "failed_at": str(job.get("failed_at", "")).strip(),
                "cancelled_at": str(job.get("cancelled_at", "")).strip(),
                "timeout_exceeded_at": str(job.get("timeout_exceeded_at", "")).strip(),
                "failure_reason": str(job.get("failure_reason", "")).strip(),
                "model_status": str(job.get("model_status", "")).strip(),
                "output_path": output_path,
                "output_saved": bool(job.get("output_saved", False)),
                "output_exists": output_exists,
                "usage_input_tokens": int(job.get("usage_input_tokens", 0) or 0),
                "usage_output_tokens": int(job.get("usage_output_tokens", 0) or 0),
                "usage_total_tokens": int(job.get("usage_total_tokens", 0) or 0),
                "last_error": str(job.get("last_error", "")).strip(),
                "cancel_error": str(job.get("cancel_error", "")).strip(),
            }
        )
    return rows


def counts_for_jobs(jobs: list[dict[str, Any]]) -> dict[str, int]:
    counts: dict[str, int] = {}
    for job in jobs:
        status = str(job.get("response_status", "unknown"))
        counts[status] = counts.get(status, 0) + 1
    return counts


def web_index_html(refresh_seconds: float) -> str:
    refresh_ms = int(max(0.5, refresh_seconds) * 1000)
    return f"""<!doctype html>
<html lang=\"en\">
<head>
  <meta charset=\"utf-8\" />
  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\" />
  <title>Background Jobs Dashboard</title>
  <style>
    body {{ font-family: system-ui, -apple-system, sans-serif; margin: 20px; color: #111; }}
    h1 {{ margin: 0 0 6px; }}
    .meta {{ color: #555; font-size: 14px; margin-bottom: 14px; }}
    .stats {{ display: flex; gap: 10px; flex-wrap: wrap; margin-bottom: 12px; }}
    .chip {{ background: #f2f2f2; border: 1px solid #ddd; border-radius: 999px; padding: 6px 10px; font-size: 12px; }}
    .controls {{ display: flex; gap: 10px; align-items: center; margin-bottom: 10px; }}
    table {{ width: 100%; border-collapse: collapse; }}
    th, td {{ border: 1px solid #ddd; padding: 7px; text-align: left; vertical-align: top; font-size: 13px; }}
    thead {{ background: #f8f8f8; position: sticky; top: 0; }}
    .status-queued {{ color: #7a5200; }}
    .status-in_progress {{ color: #004a8f; }}
    .status-completed {{ color: #0a6b1c; }}
    .status-failed {{ color: #8e1010; }}
    .status-cancelled {{ color: #5d0d6e; }}
    .status-incomplete {{ color: #555; }}
    .mono {{ font-family: ui-monospace, SFMono-Regular, Menlo, monospace; font-size: 12px; }}
    .muted {{ color: #666; }}
  </style>
</head>
<body>
  <h1>Background Jobs Dashboard</h1>
  <div class=\"meta\" id=\"meta\">Loading…</div>
  <div class=\"stats\" id=\"stats\"></div>
  <div class=\"controls\">
    <label>Status:
      <select id=\"statusFilter\">
        <option value=\"\">all</option>
      </select>
    </label>
    <label>Problem:
      <input id=\"numberFilter\" placeholder=\"e.g. 123\" />
    </label>
  </div>
  <table>
    <thead>
      <tr>
        <th>Problem</th>
        <th>Status</th>
        <th>Model Status</th>
        <th>Timestamps</th>
        <th>Result</th>
        <th>Response ID</th>
        <th>Errors</th>
      </tr>
    </thead>
    <tbody id=\"rows\"></tbody>
  </table>
  <script>
    const rowsEl = document.getElementById('rows');
    const statsEl = document.getElementById('stats');
    const metaEl = document.getElementById('meta');
    const statusFilterEl = document.getElementById('statusFilter');
    const numberFilterEl = document.getElementById('numberFilter');
    let state = {{ jobs: [], counts: {{}} }};

    function esc(text) {{
      return String(text || '').replaceAll('&','&amp;').replaceAll('<','&lt;').replaceAll('>','&gt;');
    }}

    function updateStatusOptions(counts) {{
      const statuses = Object.keys(counts).sort();
      const existing = new Set(Array.from(statusFilterEl.options).map(o => o.value));
      for (const status of statuses) {{
        if (!existing.has(status)) {{
          const option = document.createElement('option');
          option.value = status;
          option.textContent = status;
          statusFilterEl.appendChild(option);
        }}
      }}
    }}

    function render() {{
      const statusFilter = statusFilterEl.value.trim();
      const numberFilter = numberFilterEl.value.trim();
      const jobs = state.jobs.filter(job => {{
        if (statusFilter && job.response_status !== statusFilter) return false;
        if (numberFilter && !String(job.number).includes(numberFilter)) return false;
        return true;
      }});

      rowsEl.innerHTML = jobs.map(job => {{
        const statusClass = `status-${{job.response_status || 'unknown'}}`;
        const stamps = [
          ['submitted', job.submitted_at],
          ['terminal', job.terminal_at],
          ['failed', job.failed_at],
          ['cancelled', job.cancelled_at],
          ['timeout', job.timeout_exceeded_at],
        ].filter(([_, v]) => v).map(([k,v]) => `<div><span class=\"muted\">${{k}}:</span> <span class=\"mono\">${{esc(v)}}</span></div>`).join('');
        const resultReady = Boolean(job.output_saved) && Boolean(job.output_exists);
        const resultCell = job.output_path
          ? (resultReady
              ? `<a href=\"/result?number=${{encodeURIComponent(job.number)}}\" target=\"_blank\">view</a><div class=\"mono muted\">${{esc(job.output_path)}}</div>`
              : `<span class=\"muted\">pending</span><div class=\"mono muted\">${{esc(job.output_path)}}</div>`)
          : '<span class=\"muted\">—</span>';
        const errors = [job.last_error, job.cancel_error, job.failure_reason].filter(Boolean).map(esc).join('<br/>');
        return `<tr>
          <td class=\"mono\">${{esc(job.number)}}</td>
          <td><span class=\"${{statusClass}}\">${{esc(job.response_status)}}</span></td>
          <td>${{esc(job.model_status || '—')}}</td>
          <td>${{stamps || '<span class=\"muted\">—</span>'}}</td>
          <td>${{resultCell}}</td>
          <td class=\"mono\">${{esc(job.response_id)}}</td>
          <td>${{errors || '<span class=\"muted\">—</span>'}}</td>
        </tr>`;
      }}).join('');

      const statusChips = Object.keys(state.counts).sort().map(status =>
        `<div class=\"chip\">${{esc(status)}}: ${{state.counts[status]}}</div>`
      ).join('');
      statsEl.innerHTML = statusChips;
      metaEl.textContent = `jobs=${{state.jobs.length}} | refreshed=${{new Date().toLocaleTimeString()}}`;
    }}

    async function refresh() {{
      try {{
        const res = await fetch('/api/jobs');
        if (!res.ok) throw new Error(`HTTP ${{res.status}}`);
        state = await res.json();
        updateStatusOptions(state.counts || {{}});
        render();
      }} catch (error) {{
        metaEl.textContent = `Refresh error: ${{error}}`;
      }}
    }}

    statusFilterEl.addEventListener('change', render);
    numberFilterEl.addEventListener('input', render);
    refresh();
    setInterval(refresh, {refresh_ms});
  </script>
</body>
</html>
"""


def run_web_dashboard(args: argparse.Namespace) -> None:
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self) -> None:
            parsed = urlparse(self.path)
            if parsed.path == "/":
                body = web_index_html(args.web_refresh_seconds).encode("utf-8")
                self.send_response(200)
                self.send_header("Content-Type", "text/html; charset=utf-8")
                self.send_header("Content-Length", str(len(body)))
                self.end_headers()
                self.wfile.write(body)
                return

            if parsed.path == "/api/jobs":
                state = load_state(args.state_file)
                jobs = jobs_for_web(state)
                payload = {
                    "jobs": jobs,
                    "counts": counts_for_jobs(jobs),
                    "state_file": str(args.state_file),
                }
                body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
                self.send_response(200)
                self.send_header("Content-Type", "application/json; charset=utf-8")
                self.send_header("Cache-Control", "no-cache")
                self.send_header("Content-Length", str(len(body)))
                self.end_headers()
                self.wfile.write(body)
                return

            if parsed.path == "/result":
                query = parse_qs(parsed.query)
                number = ""
                if "number" in query and query["number"]:
                    number = query["number"][0].strip()
                state = load_state(args.state_file)
                jobs = [job for job in state.get("jobs", []) if isinstance(job, dict)]
                job = next((job for job in jobs if str(job.get("number", "")).strip() == number), None)
                if job is None:
                    self.send_error(404, "job not found")
                    return
                output_path = Path(str(job.get("output_path", "")).strip())
                if not output_path.exists() or not output_path.is_file():
                    self.send_error(404, "result file not found")
                    return
                text = output_path.read_text(encoding="utf-8", errors="replace")
                title = f"Problem {html.escape(number)} result"
                rendered = (
                    "<!doctype html><html><head><meta charset='utf-8'>"
                    f"<title>{title}</title>"
                    "<style>body{font-family:system-ui,-apple-system,sans-serif;margin:20px;}"
                    "pre{white-space:pre-wrap;border:1px solid #ddd;padding:12px;background:#fafafa;}"
                    "a{color:#0056b3;}</style></head><body>"
                    "<p><a href='/'>← Back to dashboard</a></p>"
                    f"<h2>{title}</h2>"
                    f"<div><code>{html.escape(str(output_path))}</code></div>"
                    f"<pre>{html.escape(text)}</pre>"
                    "</body></html>"
                ).encode("utf-8")
                self.send_response(200)
                self.send_header("Content-Type", "text/html; charset=utf-8")
                self.send_header("Content-Length", str(len(rendered)))
                self.end_headers()
                self.wfile.write(rendered)
                return

            self.send_error(404, "not found")

        def log_message(self, format: str, *values: Any) -> None:
            return

    server = ThreadingHTTPServer((args.web_host, args.web_port), Handler)
    print(
        f"Web dashboard running at http://{args.web_host}:{args.web_port} (state: {args.state_file})",
        file=sys.stderr,
    )
    print("Press Ctrl+C to stop.", file=sys.stderr)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()


def main() -> None:
    args = parse_args()
    if args.submit_interval_seconds < 0:
        print("--submit-interval-seconds must be >= 0", file=sys.stderr)
        raise SystemExit(2)
    if args.submit_max_retries < 0:
        print("--submit-max-retries must be >= 0", file=sys.stderr)
        raise SystemExit(2)
    if args.submit_retry_seconds < 0:
        print("--submit-retry-seconds must be >= 0", file=sys.stderr)
        raise SystemExit(2)
    if args.max_active_jobs < 0:
        print("--max-active-jobs must be >= 0", file=sys.stderr)
        raise SystemExit(2)
    if args.submit_wait_seconds < 0:
        print("--submit-wait-seconds must be >= 0", file=sys.stderr)
        raise SystemExit(2)
    if args.web_port <= 0 or args.web_port > 65535:
        print("--web-port must be in 1..65535", file=sys.stderr)
        raise SystemExit(2)
    if args.web_refresh_seconds <= 0:
        print("--web-refresh-seconds must be > 0", file=sys.stderr)
        raise SystemExit(2)

    if args.command == "submit":
        api_key = os.getenv("OPENAI_API_KEY", "").strip()
        if not api_key:
            print("Missing OPENAI_API_KEY environment variable.", file=sys.stderr)
            raise SystemExit(1)
        run_submit(args, api_key)
        return
    if args.command == "dashboard":
        api_key = os.getenv("OPENAI_API_KEY", "").strip()
        if not api_key:
            print("Missing OPENAI_API_KEY environment variable.", file=sys.stderr)
            raise SystemExit(1)
        run_dashboard(args, api_key)
        return
    if args.command == "web-dashboard":
        run_web_dashboard(args)
        return
    raise SystemExit(f"Unknown command: {args.command}")


if __name__ == "__main__":
    main()
