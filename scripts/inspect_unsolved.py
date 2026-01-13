#!/usr/bin/env python3
"""Inspect extracted problem text from unsolved JSONL."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from export_unsolved import extract_problem_sections


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Inspect extracted problem text from unsolved JSONL.",
    )
    parser.add_argument(
        "--input",
        type=Path,
        default=Path("data/unsolved.jsonl"),
        help="Input JSONL path.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=None,
        help="Optional JSONL output path with extracted text.",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=5,
        help="Limit number of records to inspect.",
    )
    parser.add_argument(
        "--keep-raw",
        action="store_true",
        help="Include raw HTML as raw_html in output.",
    )
    return parser.parse_args()


def iter_records(path: Path) -> list[dict]:
    records: list[dict] = []
    with path.open("r", encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if not line:
                continue
            records.append(json.loads(line))
    return records


def inspect_records(records: list[dict], limit: int, keep_raw: bool) -> list[dict]:
    output: list[dict] = []
    for record in records[:limit]:
        raw = record.get("latex", "")
        content, additional = extract_problem_sections(raw)
        new_record = {**record, "latex": content or raw}
        if additional:
            new_record["additional_text"] = additional
        if keep_raw:
            new_record["raw_html"] = raw
        output.append(new_record)
    return output


def main() -> None:
    args = parse_args()
    records = iter_records(args.input)
    inspected = inspect_records(records, args.limit, args.keep_raw)

    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        with args.output.open("w", encoding="utf-8") as handle:
            for record in inspected:
                handle.write(json.dumps(record, ensure_ascii=False))
                handle.write("\n")
    else:
        for record in inspected:
            number = record.get("number", "?")
            print(f"# {number}")
            print(record.get("latex", ""))
            additional = record.get("additional_text")
            if additional:
                print("\n[Additional]\n")
                print(additional)
            print("\n---\n")


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(str(exc), file=sys.stderr)
        raise SystemExit(1)
