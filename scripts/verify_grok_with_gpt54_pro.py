#!/usr/bin/env python3
"""Verify Grok candidate solutions with GPT-5.4 Pro via Responses API."""

from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
import json
import os
import re
import sys
import threading
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


SYSTEM_PROMPT = (
    "Evaluate the proof and decide whether it is correct. "
    "At the very end, output exactly one line: "
    "Verdict: Correct or Verdict: Reparable or Verdict: False"
)

FAILURE_PHRASES = (
    "couldn't solve",
    "could not solve",
    "unable to solve",
    "could not repair",
    "couldn't repair",
    "could not resolve",
    "couldn't resolve",
    "could not prove",
    "remains open",
    "remains elusive",
    "remains unsolved",
)

VERDICT_RE = re.compile(r"^Verdict:\s*(Correct|Reparable|False)\s*$", re.IGNORECASE)
LOG_LOCK = threading.Lock()


def log_stderr(message: str) -> None:
    with LOG_LOCK:
        print(message, file=sys.stderr, flush=True)


def render_progress_bar(done: int, total: int, width: int = 30) -> str:
    if total <= 0:
        return "[------------------------------]"
    clamped_done = max(0, min(done, total))
    filled = int(width * clamped_done / total)
    return "[" + ("#" * filled) + ("-" * (width - filled)) + "]"


def log_progress(*, processed: int, skipped: int, failed: int, total: int, in_flight: int) -> None:
    done = processed + skipped + failed
    left = max(0, total - done)
    bar = render_progress_bar(done, total)
    log_stderr(
        f"{bar} done={done}/{total} left={left} in_flight={in_flight} "
        f"ok={processed} failed={failed} skipped={skipped}"
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "For problems where Grok did not admit failure, send problem LaTeX + Grok output "
            "to GPT-5.4 Pro and record verdicts."
        )
    )
    parser.add_argument(
        "--solutions-dir",
        type=Path,
        default=Path("data/solutions"),
        help="Directory containing per-problem solution folders.",
    )
    parser.add_argument(
        "--grok-filename",
        default="grok_output.md",
        help="Filename containing Grok output in each problem directory.",
    )
    parser.add_argument(
        "--output-filename",
        default="gpt54_pro_verification.md",
        help="Verification output filename under each problem directory.",
    )
    parser.add_argument(
        "--problems-jsonl",
        type=Path,
        default=Path("data/unsolved.jsonl"),
        help="JSONL containing problem number and latex fields.",
    )
    parser.add_argument(
        "--summary-output",
        type=Path,
        default=Path("data/gpt54_pro_verdicts.jsonl"),
        help="Output JSONL summary for this run.",
    )
    parser.add_argument(
        "--api-base",
        default="https://api.openai.com/v1",
        help="OpenAI API base URL.",
    )
    parser.add_argument(
        "--model",
        default="gpt-5.4-pro",
        help="Responses API model.",
    )
    parser.add_argument(
        "--reasoning-effort",
        default="xhigh",
        choices=["medium", "high", "xhigh"],
        help="Reasoning effort for GPT-5.4 Pro.",
    )
    parser.add_argument(
        "--timeout",
        type=float,
        default=7200.0,
        help="HTTP timeout in seconds.",
    )
    parser.add_argument(
        "--retries",
        type=int,
        default=2,
        help="Maximum retries per request on transient failures.",
    )
    parser.add_argument(
        "--delay",
        type=float,
        default=0.0,
        help="Delay in seconds between successful requests.",
    )
    parser.add_argument(
        "--concurrency",
        type=int,
        default=30,
        help="Number of problems to verify in parallel.",
    )
    parser.add_argument(
        "--max-problems",
        type=int,
        default=0,
        help="Max number of filtered problems to process (0 means all).",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite existing verification files.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Only list how many problems would be processed; do not call the API.",
    )
    return parser.parse_args()


def problem_sort_key(value: str):
    return (0, int(value)) if value.isdigit() else (1, value)


def load_latex_by_number(path: Path) -> dict[str, str]:
    if not path.exists():
        raise FileNotFoundError(f"Problems JSONL not found: {path}")
    mapping: dict[str, str] = {}
    with path.open("r", encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, start=1):
            stripped = line.strip()
            if not stripped:
                continue
            try:
                value = json.loads(stripped)
            except json.JSONDecodeError as exc:
                raise ValueError(f"Invalid JSON at line {line_number}: {exc}") from exc
            if not isinstance(value, dict):
                continue
            number = str(value.get("number", "")).strip()
            if not number:
                continue
            latex = str(value.get("latex", "")).strip()
            if latex:
                mapping[number] = latex
    return mapping


def list_filtered_problem_numbers(solutions_dir: Path, grok_filename: str) -> list[str]:
    if not solutions_dir.exists():
        raise FileNotFoundError(f"Solutions directory not found: {solutions_dir}")

    numbers: list[str] = []
    for problem_dir in solutions_dir.iterdir():
        if not problem_dir.is_dir():
            continue
        grok_path = problem_dir / grok_filename
        if not grok_path.exists():
            continue
        text = grok_path.read_text(encoding="utf-8", errors="replace").lower()
        if any(phrase in text for phrase in FAILURE_PHRASES):
            continue
        numbers.append(problem_dir.name)
    return sorted(numbers, key=problem_sort_key)


def build_user_prompt(number: str, latex: str, grok_solution: str) -> str:
    return (
        f"Problem number: {number}\n\n"
        "Problem statement (LaTeX):\n"
        f"{latex}\n\n"
        "Proposed proof:\n"
        f"{grok_solution}\n\n"
        "Is this proof correct? "
        "Make sure the last line is exactly one of: "
        "Verdict: Correct or Verdict: Reparable or Verdict: False"
    )


def extract_output_text(response_data: dict[str, Any]) -> str:
    output_text = response_data.get("output_text")
    if isinstance(output_text, str) and output_text.strip():
        return output_text.strip()

    output = response_data.get("output")
    pieces: list[str] = []
    if isinstance(output, list):
        for item in output:
            if not isinstance(item, dict):
                continue
            content = item.get("content")
            if not isinstance(content, list):
                continue
            for block in content:
                if not isinstance(block, dict):
                    continue
                text = block.get("text")
                if isinstance(text, str) and text.strip():
                    pieces.append(text.strip())
    return "\n\n".join(pieces).strip()


def extract_verdict(text: str) -> str | None:
    verdict: str | None = None
    for line in text.splitlines():
        match = VERDICT_RE.match(line.strip())
        if match:
            verdict = match.group(1).capitalize()
    return verdict


def call_responses_api(
    *,
    api_base: str,
    api_key: str,
    model: str,
    reasoning_effort: str,
    user_prompt: str,
    timeout: float,
    retries: int,
    request_label: str,
) -> tuple[str, str, dict[str, Any] | None]:
    url = f"{api_base.rstrip('/')}/responses"
    payload = {
        "model": model,
        "reasoning": {"effort": reasoning_effort},
        "input": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_prompt},
        ],
    }
    body = json.dumps(payload).encode("utf-8")

    last_error: Exception | None = None
    for attempt in range(1, retries + 1):
        log_stderr(f"{request_label} Waiting for API response (attempt {attempt}/{retries})...")
        request = Request(
            url,
            data=body,
            method="POST",
            headers={
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json",
            },
        )
        try:
            with urlopen(request, timeout=timeout) as response:
                response_data = json.loads(response.read().decode("utf-8"))
        except HTTPError as exc:
            if exc.code in {408, 409, 429, 500, 502, 503, 504} and attempt < retries:
                wait_seconds = min(60, 2**attempt)
                log_stderr(
                    f"{request_label} HTTP {exc.code}. Retrying in {wait_seconds}s "
                    f"({attempt}/{retries})..."
                )
                time.sleep(wait_seconds)
                continue
            detail = ""
            try:
                detail = exc.read().decode("utf-8", errors="replace")
            except Exception:
                detail = ""
            raise RuntimeError(f"Responses API HTTP {exc.code}: {detail}") from exc
        except (URLError, TimeoutError, json.JSONDecodeError) as exc:
            last_error = exc
            if attempt < retries:
                wait_seconds = min(60, 2**attempt)
                log_stderr(
                    f"{request_label} Transient error ({type(exc).__name__}: {exc}). "
                    f"Retrying in {wait_seconds}s ({attempt}/{retries})..."
                )
                time.sleep(wait_seconds)
                continue
            break

        text = extract_output_text(response_data)
        if not text:
            raise RuntimeError("Responses API returned empty content")
        verdict = extract_verdict(text)
        if not verdict:
            raise RuntimeError("Response missing required verdict line")
        usage = response_data.get("usage")
        return text, verdict, usage if isinstance(usage, dict) else None

    if last_error is not None:
        raise RuntimeError(f"Responses API request failed: {last_error}") from last_error
    raise RuntimeError("Responses API request failed")


def write_verification(path: Path, number: str, verdict: str, response_text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    header = (
        f"# GPT-5.4 Pro Verification for Problem {number}\n\n"
        f"Verdict: {verdict}\n\n"
        "---\n\n"
    )
    path.write_text(header + response_text.strip() + "\n", encoding="utf-8")


def verify_problem(
    *,
    number: str,
    output_path: Path,
    prompt: str,
    args: argparse.Namespace,
    api_key: str,
    request_label: str,
) -> tuple[str, dict[str, Any] | None]:
    response_text, verdict, usage = call_responses_api(
        api_base=args.api_base,
        api_key=api_key,
        model=args.model,
        reasoning_effort=args.reasoning_effort,
        user_prompt=prompt,
        timeout=args.timeout,
        retries=args.retries,
        request_label=request_label,
    )
    write_verification(output_path, number, verdict, response_text)
    return verdict, usage


def main() -> None:
    args = parse_args()
    latex_by_number = load_latex_by_number(args.problems_jsonl)
    numbers = list_filtered_problem_numbers(args.solutions_dir, args.grok_filename)
    if args.max_problems > 0:
        numbers = numbers[: args.max_problems]

    total = len(numbers)
    if total == 0:
        log_stderr("No filtered problems found.")
        return

    if args.dry_run:
        log_stderr(f"Filtered problems: {total}")
        log_stderr("First 20: " + ", ".join(numbers[:20]) if numbers else "First 20: (none)")
        return

    api_key = os.getenv("OPENAI_API_KEY", "").strip()
    if not api_key:
        log_stderr("Missing OPENAI_API_KEY environment variable.")
        raise SystemExit(1)
    if args.concurrency < 1:
        log_stderr("--concurrency must be at least 1.")
        raise SystemExit(1)

    processed = 0
    skipped = 0
    failed = 0
    run_started_at = datetime.now(timezone.utc).isoformat()
    summary_records: list[dict[str, Any]] = []

    pending_tasks: list[tuple[int, str, Path, str]] = []
    log_stderr(
        f"Starting verification: total={total}, concurrency={args.concurrency}, model={args.model}."
    )
    log_progress(processed=processed, skipped=skipped, failed=failed, total=total, in_flight=0)

    for index, number in enumerate(numbers, start=1):
        problem_dir = args.solutions_dir / number
        grok_path = problem_dir / args.grok_filename
        output_path = problem_dir / args.output_filename

        if output_path.exists() and not args.force:
            log_stderr(f"[{index}/{total}] Skipping {number} (already verified).")
            skipped += 1
            log_progress(processed=processed, skipped=skipped, failed=failed, total=total, in_flight=0)
            continue

        latex = latex_by_number.get(number, "").strip()
        if not latex:
            log_stderr(f"[{index}/{total}] Failed {number}: missing latex in {args.problems_jsonl}.")
            failed += 1
            summary_records.append(
                {
                    "number": number,
                    "status": "failed",
                    "reason": "missing_latex",
                    "run_started_at": run_started_at,
                }
            )
            log_progress(processed=processed, skipped=skipped, failed=failed, total=total, in_flight=0)
            continue

        if not grok_path.exists():
            log_stderr(f"[{index}/{total}] Failed {number}: missing {args.grok_filename}.")
            failed += 1
            summary_records.append(
                {
                    "number": number,
                    "status": "failed",
                    "reason": "missing_grok_output",
                    "run_started_at": run_started_at,
                }
            )
            log_progress(processed=processed, skipped=skipped, failed=failed, total=total, in_flight=0)
            continue

        grok_solution = grok_path.read_text(encoding="utf-8", errors="replace").strip()
        prompt = build_user_prompt(number, latex, grok_solution)
        pending_tasks.append((index, number, output_path, prompt))

    if args.concurrency == 1:
        for index, number, output_path, prompt in pending_tasks:
            request_label = f"[{index}/{total}] {number}"
            log_stderr(f"[{index}/{total}] Starting {number} with {args.model}...")
            try:
                verdict, usage = verify_problem(
                    number=number,
                    output_path=output_path,
                    prompt=prompt,
                    args=args,
                    api_key=api_key,
                    request_label=request_label,
                )
                processed += 1
                log_stderr(f"[{index}/{total}] Completed {number}: verdict={verdict}.")
                summary_records.append(
                    {
                        "number": number,
                        "status": "processed",
                        "verdict": verdict,
                        "usage": usage,
                        "output_path": str(output_path),
                        "run_started_at": run_started_at,
                    }
                )
            except Exception as exc:
                failed += 1
                log_stderr(f"[{index}/{total}] Failed {number}: {type(exc).__name__}: {exc}")
                summary_records.append(
                    {
                        "number": number,
                        "status": "failed",
                        "reason": f"{type(exc).__name__}: {exc}",
                        "run_started_at": run_started_at,
                    }
                )
                log_progress(processed=processed, skipped=skipped, failed=failed, total=total, in_flight=0)
                continue

            log_progress(processed=processed, skipped=skipped, failed=failed, total=total, in_flight=0)

            if args.delay > 0 and index < total:
                time.sleep(args.delay)
    else:
        if args.delay > 0:
            log_stderr("--delay is ignored when --concurrency > 1.")
        with ThreadPoolExecutor(max_workers=args.concurrency) as executor:
            future_to_task = {}
            in_flight = 0
            queue_total = len(pending_tasks)
            submitted = 0
            for index, number, output_path, prompt in pending_tasks:
                request_label = f"[{index}/{total}] {number}"
                future = executor.submit(
                    verify_problem,
                    number=number,
                    output_path=output_path,
                    prompt=prompt,
                    args=args,
                    api_key=api_key,
                    request_label=request_label,
                )
                future_to_task[future] = (index, number, output_path)
                submitted += 1
                in_flight += 1
                queued_left = max(0, queue_total - submitted)
                log_stderr(
                    f"[{index}/{total}] Started {number}. in_flight={in_flight}, queue_left={queued_left}."
                )
                log_progress(
                    processed=processed,
                    skipped=skipped,
                    failed=failed,
                    total=total,
                    in_flight=in_flight,
                )

            for future in as_completed(future_to_task):
                index, number, output_path = future_to_task[future]
                in_flight = max(0, in_flight - 1)
                try:
                    verdict, usage = future.result()
                    processed += 1
                    log_stderr(f"[{index}/{total}] Completed {number}: verdict={verdict}.")
                    summary_records.append(
                        {
                            "number": number,
                            "status": "processed",
                            "verdict": verdict,
                            "usage": usage,
                            "output_path": str(output_path),
                            "run_started_at": run_started_at,
                        }
                    )
                except Exception as exc:
                    failed += 1
                    log_stderr(f"[{index}/{total}] Failed {number}: {type(exc).__name__}: {exc}")
                    summary_records.append(
                        {
                            "number": number,
                            "status": "failed",
                            "reason": f"{type(exc).__name__}: {exc}",
                            "run_started_at": run_started_at,
                        }
                    )
                log_progress(
                    processed=processed,
                    skipped=skipped,
                    failed=failed,
                    total=total,
                    in_flight=in_flight,
                )

    args.summary_output.parent.mkdir(parents=True, exist_ok=True)
    with args.summary_output.open("a", encoding="utf-8") as handle:
        for record in summary_records:
            handle.write(json.dumps(record, ensure_ascii=False))
            handle.write("\n")

    log_stderr(f"Done. Processed={processed}, Skipped={skipped}, Failed={failed}, Total={total}.")
    log_stderr(f"Summary appended to: {args.summary_output}")


if __name__ == "__main__":
    main()
