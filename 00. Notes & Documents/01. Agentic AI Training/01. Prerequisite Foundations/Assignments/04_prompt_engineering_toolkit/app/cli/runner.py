"""CLI runner for the prompt engineering toolkit."""

from __future__ import annotations

import sys
from pathlib import Path

from app.cli.output import (
    is_valid_structured_result,
    print_naive_result,
    print_report_header,
    print_run_summary,
    print_structured_result,
)
from app.config import DEFAULT_REPORTS_FILE
from app.services.json_parser import StructuredParseError
from app.services.llm_service import LLMService
from app.services.report_loader import ReportsDataError, load_reports
from app.services.token_tracker import TokenTracker
from app.strategies.extraction import fewshot_extract, naive_extract, structured_extract


def run_toolkit(reports_file: Path | None = None, *, service: LLMService | None = None) -> int:
    """Run all three strategies over the committed reports."""
    try:
        reports = load_reports(reports_file)
    except ReportsDataError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1

    token_tracker = TokenTracker()
    llm = service or LLMService(token_tracker=token_tracker, emit_usage=True)

    structured_ok = 0
    fewshot_ok = 0

    for index, report in enumerate(reports, start=1):
        print_report_header(index, report)

        print_naive_result(naive_extract(report, service=llm))

        try:
            structured_result = structured_extract(report, service=llm)
            print_structured_result("structured", structured_result)
            if is_valid_structured_result(structured_result):
                structured_ok += 1
        except StructuredParseError as exc:
            print_structured_result("structured", None, error=str(exc))

        try:
            fewshot_result = fewshot_extract(report, service=llm)
            print_structured_result("few-shot", fewshot_result)
            if is_valid_structured_result(fewshot_result):
                fewshot_ok += 1
        except StructuredParseError as exc:
            print_structured_result("few-shot", None, error=str(exc))

    print_run_summary(
        structured_ok=structured_ok,
        fewshot_ok=fewshot_ok,
        total_reports=len(reports),
        token_tracker=token_tracker,
    )
    return 0


def main() -> int:
    return run_toolkit(DEFAULT_REPORTS_FILE)


if __name__ == "__main__":
    raise SystemExit(main())
