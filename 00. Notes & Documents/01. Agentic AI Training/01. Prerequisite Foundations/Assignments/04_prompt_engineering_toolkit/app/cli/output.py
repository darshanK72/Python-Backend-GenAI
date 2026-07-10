"""CLI output formatting."""

from __future__ import annotations

import json
from typing import Any

from app.schemas.extraction import SEVERITIES
from app.services.token_tracker import TokenTracker


def is_valid_structured_result(result: dict[str, Any]) -> bool:
    return result.get("severity") in SEVERITIES


def print_report_header(index: int, report: str) -> None:
    print(f"\n=== Report {index} ===")
    print(report)


def print_naive_result(result: str) -> None:
    print("\n[naive]")
    print(result)


def print_structured_result(label: str, result: dict[str, Any] | None, error: str | None = None) -> None:
    print(f"\n[{label}]")
    if error:
        print(f"Failed: {error}")
        return
    print(json.dumps(result, indent=2))


def print_run_summary(
    *,
    structured_ok: int,
    fewshot_ok: int,
    total_reports: int,
    token_tracker: TokenTracker,
) -> None:
    print("\n=== Summary ===")
    print(f"Structured valid outputs: {structured_ok}/{total_reports}")
    print(f"Few-shot valid outputs:   {fewshot_ok}/{total_reports}")
    print(f"Total tokens used:        {token_tracker.running_total}")
