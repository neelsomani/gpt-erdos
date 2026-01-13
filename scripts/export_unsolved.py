#!/usr/bin/env python3
"""Export unsolved Erdos problems with LaTeX sources."""

from __future__ import annotations

import argparse
import html
import json
import sys
import time
from pathlib import Path
from typing import Iterable
from html.parser import HTMLParser
from urllib.error import HTTPError, URLError
from urllib.request import urlopen

import yaml


UNSOLVED_STATES = {"open", "falsifiable"}


class ProblemHTMLParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self._content_depth = 0
        self._additional_depth = 0
        self._ignored_additional_depth = 0
        self._content_parts: list[str] = []
        self._additional_parts: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attrs_dict = dict(attrs)
        if tag == "div":
            if attrs_dict.get("id") == "content":
                self._content_depth = max(self._content_depth, 1)
            elif self._content_depth > 0:
                self._content_depth += 1

            class_attr = attrs_dict.get("class")
            if class_attr:
                classes = class_attr.split()
                if "problem-additional-text" in classes:
                    style = (attrs_dict.get("style") or "").replace(" ", "").lower()
                    if "text-align:center" in style:
                        self._ignored_additional_depth = max(self._ignored_additional_depth, 1)
                    else:
                        self._additional_depth = max(self._additional_depth, 1)
                elif self._ignored_additional_depth > 0:
                    self._ignored_additional_depth += 1
                elif self._additional_depth > 0:
                    self._additional_depth += 1
        elif tag == "br":
            self._append("\n")
        elif tag in {"p", "h3", "li"}:
            self._append("\n")

    def handle_endtag(self, tag: str) -> None:
        if tag == "div":
            if self._content_depth > 0:
                self._content_depth -= 1
            if self._ignored_additional_depth > 0:
                self._ignored_additional_depth -= 1
            if self._additional_depth > 0:
                self._additional_depth -= 1

    def handle_data(self, data: str) -> None:
        self._append(data)

    def _append(self, text: str) -> None:
        if self._content_depth > 0:
            self._content_parts.append(text)
        if self._additional_depth > 0:
            self._additional_parts.append(text)

    def extract_sections(self) -> tuple[str, str]:
        content = _normalize_text("".join(self._content_parts))
        additional = _normalize_text("".join(self._additional_parts))
        if additional:
            lines = [line for line in additional.splitlines() if line.strip() != "Back to the problem"]
            additional = _normalize_text("\n".join(lines))
        return content, additional


def _normalize_text(text: str) -> str:
    text = html.unescape(text)
    lines = [line.strip() for line in text.splitlines()]
    normalized: list[str] = []
    last_blank = False
    for line in lines:
        if not line:
            if not last_blank:
                normalized.append("")
            last_blank = True
        else:
            normalized.append(line)
            last_blank = False
    return "\n".join(normalized).strip()


def extract_problem_sections(source: str) -> tuple[str, str]:
    parser = ProblemHTMLParser()
    parser.feed(source)
    return parser.extract_sections()


def extract_problem_text(source: str) -> str:
    content, additional = extract_problem_sections(source)
    if content and additional:
        return f"{content}\n\n{additional}"
    if content:
        return content
    if additional:
        return additional
    return source


def load_problems(path: Path) -> list[dict]:
    with path.open("r", encoding="utf-8") as handle:
        data = yaml.safe_load(handle)
    if not isinstance(data, list):
        raise ValueError("Expected problems.yaml to contain a list of problems")
    return data


def iter_unsolved(problems: Iterable[dict]) -> Iterable[dict]:
    for problem in problems:
        status = problem.get("status", {})
        state = status.get("state")
        if state in UNSOLVED_STATES:
            yield {
                "number": str(problem.get("number")),
                "state": state,
            }


def fetch_latex(problem_number: str, base_url: str, timeout: float) -> tuple[str, str]:
    url = f"{base_url.rstrip('/')}/{problem_number}"
    try:
        with urlopen(url, timeout=timeout) as response:
            payload = response.read().decode("utf-8")
            content, additional = extract_problem_sections(payload)
            if not content and not additional:
                content = payload
            return content, additional
    except (HTTPError, URLError) as exc:
        raise RuntimeError(f"Failed to fetch LaTeX for problem {problem_number}: {exc}")


def write_jsonl(records: Iterable[dict], output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8") as handle:
        for record in records:
            handle.write(json.dumps(record, ensure_ascii=False))
            handle.write("\n")


def build_dataset(
    input_path: Path,
    output_path: Path,
    base_url: str,
    timeout: float,
    delay: float,
) -> None:
    problems = load_problems(input_path)
    unsolved = list(iter_unsolved(problems))
    total = len(unsolved)
    records: list[dict] = []
    try:
        for index, problem in enumerate(unsolved, start=1):
            print(
                f"[{index}/{total}] Fetching LaTeX for problem {problem['number']}...",
                file=sys.stderr,
                flush=True,
            )
            latex, additional_text = fetch_latex(problem["number"], base_url, timeout)
            records.append(
                {
                    "number": problem["number"],
                    "state": problem["state"],
                    "latex": latex,
                    "additional_text": additional_text,
                }
            )
            if delay > 0:
                time.sleep(delay)
    except BaseException:
        if records:
            print(
                f"Error encountered. Writing {len(records)} records to {output_path}.",
                file=sys.stderr,
            )
            write_jsonl(records, output_path)
        raise
    write_jsonl(records, output_path)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Export unsolved Erdos problems with LaTeX sources.",
    )
    parser.add_argument(
        "--input",
        type=Path,
        default=Path("data/problems.yaml"),
        help="Path to problems.yaml.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("data/unsolved_problems.jsonl"),
        help="Output JSONL path.",
    )
    parser.add_argument(
        "--base-url",
        default="https://www.erdosproblems.com/latex",
        help="Base URL for the LaTeX endpoint.",
    )
    parser.add_argument(
        "--timeout",
        type=float,
        default=20.0,
        help="HTTP timeout in seconds.",
    )
    parser.add_argument(
        "--delay",
        type=float,
        default=1.0,
        help="Delay in seconds between requests.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    try:
        build_dataset(
            args.input,
            args.output,
            args.base_url,
            args.timeout,
            args.delay,
        )
    except Exception as exc:
        print(str(exc), file=sys.stderr)
        raise SystemExit(1)


if __name__ == "__main__":
    main()
