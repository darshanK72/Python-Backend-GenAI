"""Integration tests for strategy exports and data fixtures."""

from __future__ import annotations

from app.config import DEFAULT_REPORTS_FILE
from app.main import fewshot_extract, naive_extract, structured_extract
from app.services.report_loader import load_reports


def test_default_reports_fixture_is_available() -> None:
    reports = load_reports(DEFAULT_REPORTS_FILE)

    assert len(reports) == 5


def test_main_exports_strategy_functions() -> None:
    assert callable(naive_extract)
    assert callable(structured_extract)
    assert callable(fewshot_extract)
