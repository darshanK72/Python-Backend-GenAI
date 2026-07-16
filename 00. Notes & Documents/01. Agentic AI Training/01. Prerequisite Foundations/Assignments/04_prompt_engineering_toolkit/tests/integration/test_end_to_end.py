"""Integration tests for strategy exports and data fixtures."""

from __future__ import annotations

from app.config import DEFAULT_REPORTS_FILE
from app.services.report_loader import load_reports
from app.strategies.extraction import fewshot_extract, naive_extract, structured_extract


# test_default_reports_fixture_is_available - test that the committed reports fixture has five entries
def test_default_reports_fixture_is_available() -> None:
    reports = load_reports(DEFAULT_REPORTS_FILE)

    assert len(reports) >= 5


# test_strategy_functions_are_importable - test that strategy functions are importable from strategies module
def test_strategy_functions_are_importable() -> None:
    assert callable(naive_extract)
    assert callable(structured_extract)
    assert callable(fewshot_extract)
