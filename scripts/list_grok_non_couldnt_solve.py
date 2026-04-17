#!/usr/bin/env python3
"""List problem numbers whose Grok output does not contain failure phrases."""

from __future__ import annotations

import argparse
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Scan data/solutions/*/grok_output.md and print problem numbers "
            "that do not contain 'couldn't solve', 'could not solve', "
            "'could not repair', or 'couldn't repair'."
        )
    )
    parser.add_argument(
        "--solutions-dir",
        type=Path,
        default=Path("data/solutions"),
        help="Directory containing per-problem solution folders.",
    )
    parser.add_argument(
        "--filename",
        default="grok_output.md",
        help="Filename to scan in each problem folder.",
    )
    return parser.parse_args()


def problem_sort_key(value: str):
    return (0, int(value)) if value.isdigit() else (1, value)


def main() -> None:
    args = parse_args()
    phrases = (
        "couldn't solve",
        "could not solve",
        "could not repair",
        "couldn't repair",
        "could not prove",
        "remains open",
    )

    if not args.solutions_dir.exists():
        raise SystemExit(f"Solutions directory not found: {args.solutions_dir}")

    numbers: list[str] = []
    total_problem_dirs = 0
    generated_count = 0
    flagged_count = 0
    missing_count = 0

    for problem_dir in args.solutions_dir.iterdir():
        if not problem_dir.is_dir():
            continue
        total_problem_dirs += 1
        output_path = problem_dir / args.filename
        if not output_path.exists():
            missing_count += 1
            continue
        generated_count += 1

        text = output_path.read_text(encoding="utf-8", errors="replace").lower()
        if any(phrase in text for phrase in phrases):
            flagged_count += 1
            continue
        numbers.append(problem_dir.name)

    for number in sorted(numbers, key=problem_sort_key):
        print(number)

    print("---")
    print(f"Problem directories: {total_problem_dirs}")
    print(f"Generated files found: {generated_count}")
    print(f"Flagged as unsolved/open: {flagged_count}")
    print(f"Passed filter: {len(numbers)}")
    print(f"Missing {args.filename}: {missing_count}")
    if generated_count > 0:
        rate = (flagged_count / generated_count) * 100
        print(f"Flagged rate: {rate:.1f}%")


if __name__ == "__main__":
    main()
