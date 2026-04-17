#!/usr/bin/env python3
"""Generate Grok responses for unsolved Erdos problems."""

from __future__ import annotations

import argparse
import json
import os
import sys
import time
from pathlib import Path
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


DEFAULT_SYSTEM_PROMPT = (
    "You are Grok, helping with open Erdős problems. "
    "Provide a careful mathematical solution in Markdown. "
    "Do not simply state relevant known results. "
    "If you cannot solve a problem after trying hard, then just say you couldn't solve it."
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate Grok outputs for each problem in data/unsolved.jsonl.",
    )
    parser.add_argument(
        "--input",
        type=Path,
        default=Path("data/unsolved.jsonl"),
        help="Input JSONL with unsolved problems.",
    )
    parser.add_argument(
        "--solutions-dir",
        type=Path,
        default=Path("data/solutions"),
        help="Base directory for per-problem outputs.",
    )
    parser.add_argument(
        "--output-filename",
        default="grok_output.md",
        help="Output filename under each problem directory.",
    )
    parser.add_argument(
        "--api-base",
        default="https://api.x.ai/v1",
        help="Grok API base URL.",
    )
    parser.add_argument(
        "--model",
        default="grok-4.20-0309-reasoning",
        help="Model name for the chat completions request.",
    )
    parser.add_argument(
        "--temperature",
        type=float,
        default=0.2,
        help="Sampling temperature.",
    )
    parser.add_argument(
        "--timeout",
        type=float,
        default=120.0,
        help="HTTP timeout in seconds.",
    )
    parser.add_argument(
        "--max-problems",
        type=int,
        default=0,
        help="Max number of problems to process (0 means all).",
    )
    parser.add_argument(
        "--delay",
        type=float,
        default=0.0,
        help="Delay in seconds between successful requests.",
    )
    parser.add_argument(
        "--retries",
        type=int,
        default=4,
        help="Maximum retries per request on transient failures.",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite existing output files.",
    )
    parser.add_argument(
        "--system-prompt",
        default=DEFAULT_SYSTEM_PROMPT,
        help="System prompt sent to the model.",
    )
    return parser.parse_args()


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    with path.open("r", encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, start=1):
            stripped = line.strip()
            if not stripped:
                continue
            try:
                value = json.loads(stripped)
            except json.JSONDecodeError as exc:
                raise ValueError(f"Invalid JSONL at line {line_number}: {exc}") from exc
            if not isinstance(value, dict):
                raise ValueError(f"Expected JSON object at line {line_number}")
            records.append(value)
    return records


def build_user_prompt(problem: dict[str, Any]) -> str:
    number = str(problem.get("number", "")).strip()
    latex = str(problem.get("latex", "")).strip()
    parts = [
        f"Problem number: {number}" if number else "Problem number: (unknown)",
        "",
        "Problem statement (LaTeX):",
        latex or "(missing)",
        "",
        "Task:",
        "Provide your best mathematical response to this problem in Markdown.",
    ]
    return "\n".join(parts)


def extract_message_content(message: Any) -> str:
    if isinstance(message, str):
        return message.strip()
    if isinstance(message, list):
        parts: list[str] = []
        for item in message:
            if not isinstance(item, dict):
                continue
            if item.get("type") == "text":
                text = item.get("text")
                if isinstance(text, str):
                    parts.append(text)
        return "\n".join(parts).strip()
    return ""


def call_grok(
    *,
    api_base: str,
    api_key: str,
    model: str,
    system_prompt: str,
    user_prompt: str,
    temperature: float,
    timeout: float,
    retries: int,
) -> str:
    url = f"{api_base.rstrip('/')}/chat/completions"
    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        "temperature": temperature,
    }
    body = json.dumps(payload).encode("utf-8")

    last_error: Exception | None = None
    for attempt in range(1, retries + 1):
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
            if exc.code in {429, 500, 502, 503, 504} and attempt < retries:
                wait_seconds = min(60, 2**attempt)
                print(
                    f"HTTP {exc.code}. Retrying in {wait_seconds}s ({attempt}/{retries})...",
                    file=sys.stderr,
                )
                time.sleep(wait_seconds)
                continue
            detail = ""
            try:
                detail = exc.read().decode("utf-8", errors="replace")
            except Exception:
                detail = ""
            raise RuntimeError(f"Grok API HTTP {exc.code}: {detail}") from exc
        except (URLError, TimeoutError, json.JSONDecodeError) as exc:
            last_error = exc
            if attempt < retries:
                wait_seconds = min(60, 2**attempt)
                print(
                    f"Transient error. Retrying in {wait_seconds}s ({attempt}/{retries})...",
                    file=sys.stderr,
                )
                time.sleep(wait_seconds)
                continue
            break

        choices = response_data.get("choices")
        if not isinstance(choices, list) or not choices:
            raise RuntimeError("Grok API response missing choices")
        message = choices[0].get("message", {})
        content = extract_message_content(message.get("content"))
        if not content:
            raise RuntimeError("Grok API returned empty content")
        return content

    if last_error is not None:
        raise RuntimeError(f"Grok API request failed: {last_error}") from last_error
    raise RuntimeError("Grok API request failed")


def write_output(path: Path, number: str, response_text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    header = f"# Grok Response for Problem {number}\n\n"
    path.write_text(header + response_text.strip() + "\n", encoding="utf-8")


def main() -> None:
    args = parse_args()
    api_key = os.getenv("XAI_API_KEY", "").strip()
    if not api_key:
        print("Missing XAI_API_KEY environment variable.", file=sys.stderr)
        raise SystemExit(1)
    if not args.input.exists():
        print(f"Input file not found: {args.input}", file=sys.stderr)
        raise SystemExit(1)

    records = load_jsonl(args.input)
    if args.max_problems > 0:
        records = records[: args.max_problems]

    total = len(records)
    processed = 0
    skipped = 0

    for index, record in enumerate(records, start=1):
        number = str(record.get("number", "")).strip()
        if not number:
            print(f"[{index}/{total}] Skipping record without number.", file=sys.stderr)
            skipped += 1
            continue

        output_path = args.solutions_dir / number / args.output_filename
        if output_path.exists() and not args.force:
            print(f"[{index}/{total}] Skipping {number} (already exists).", file=sys.stderr)
            skipped += 1
            continue

        prompt = build_user_prompt(record)
        print(f"[{index}/{total}] Requesting Grok response for {number}...", file=sys.stderr)
        response_text = call_grok(
            api_base=args.api_base,
            api_key=api_key,
            model=args.model,
            system_prompt=args.system_prompt,
            user_prompt=prompt,
            temperature=args.temperature,
            timeout=args.timeout,
            retries=args.retries,
        )
        write_output(output_path, number, response_text)
        processed += 1

        if args.delay > 0 and index < total:
            time.sleep(args.delay)

    print(
        f"Done. Processed={processed}, Skipped={skipped}, Total={total}.",
        file=sys.stderr,
    )


if __name__ == "__main__":
    main()
