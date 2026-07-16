"""Tests for report validation."""

from app.config import PROJECT_ROOT
from app.services.report_writer import validate_report_sections


# test_sample_delivery_report_has_all_sections - test committed report includes all headings
def test_sample_delivery_report_has_all_sections() -> None:
    report = (PROJECT_ROOT / "delivery_report.md").read_text(encoding="utf-8")
    assert validate_report_sections(report) == []


# test_validate_report_sections_detects_missing - test incomplete reports list gaps
def test_validate_report_sections_detects_missing() -> None:
    assert validate_report_sections("# Executive Summary only") == [
        "Technical Design",
        "Test Coverage",
        "Deployment Configuration",
        "Open Questions",
    ]
