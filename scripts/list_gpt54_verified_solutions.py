#!/usr/bin/env python3
"""List problem numbers with selected GPT-5.4 Pro verification verdicts."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


VERDICT_RE = re.compile(r"^Verdict:\s*(Correct|Reparable|False)\s*$", re.IGNORECASE)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Scan verification files and print problem numbers whose verdict "
            "matches selected values (default: Correct, Reparable)."
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
        default="gpt54_pro_verification.md",
        help="Verification filename in each problem folder.",
    )
    parser.add_argument(
        "--include",
        nargs="+",
        default=["Correct", "Reparable"],
        help="Verdicts to include (choices: Correct Reparable False).",
    )
    return parser.parse_args()


def problem_sort_key(value: str):
    return (0, int(value)) if value.isdigit() else (1, value)


def normalize_verdict(value: str) -> str:
    lowered = value.strip().lower()
    if lowered == "correct":
        return "Correct"
    if lowered == "reparable":
        return "Reparable"
    if lowered == "false":
        return "False"
    raise ValueError(f"Unsupported verdict: {value}")


def extract_verdict(text: str) -> str | None:
    for line in text.splitlines():
        match = VERDICT_RE.match(line.strip())
        if match:
            return match.group(1).capitalize()
    return None


def main() -> None:
    args = parse_args()

    if not args.solutions_dir.exists():
        raise SystemExit(f"Solutions directory not found: {args.solutions_dir}")

    try:
        include = {normalize_verdict(value) for value in args.include}
    except ValueError as exc:
        raise SystemExit(str(exc)) from exc

    matches_by_verdict: dict[str, list[str]] = {
        "Correct": [],
        "Reparable": [],
        "False": [],
    }
    counts = {"Correct": 0, "Reparable": 0, "False": 0, "Unknown": 0}
    missing_count = 0

    for problem_dir in args.solutions_dir.iterdir():
        if not problem_dir.is_dir():
            continue

        verification_path = problem_dir / args.filename
        if not verification_path.exists():
            missing_count += 1
            continue

        text = verification_path.read_text(encoding="utf-8", errors="replace")
        verdict = extract_verdict(text)
        if verdict is None:
            counts["Unknown"] += 1
            continue

        counts[verdict] += 1
        if verdict in include:
            matches_by_verdict[verdict].append(problem_dir.name)

    include_sorted = sorted(include)
    for verdict in include_sorted:
        numbers = sorted(matches_by_verdict[verdict], key=problem_sort_key)
        print(f"{verdict}:")
        if numbers:
            print(", ".join(numbers))
        else:
            print("(none)")

    print("---")
    print(f"Included verdicts: {', '.join(include_sorted)}")
    print(f"Matched problems: {sum(len(matches_by_verdict[v]) for v in include)}")
    print(f"Correct: {counts['Correct']}")
    print(f"Reparable: {counts['Reparable']}")
    print(f"False: {counts['False']}")
    print(f"Unknown verdict format: {counts['Unknown']}")
    print(f"Missing {args.filename}: {missing_count}")


if __name__ == "__main__":
    main()
