"""Tests for report fixture loading."""

from __future__ import annotations

import json

import pytest

from app.config import DEFAULT_REPORTS_FILE
from app.services.report_loader import ReportsDataError, load_reports


# test_load_reports_from_default_file - test that load_reports reads the committed fixture file
def test_load_reports_from_default_file() -> None:
    reports = load_reports(DEFAULT_REPORTS_FILE)

    assert len(reports) >= 5
    assert all(isinstance(report, str) for report in reports)


# test_load_reports_missing_file - test that load_reports raises when the file is missing
def test_load_reports_missing_file(tmp_path) -> None:
    with pytest.raises(ReportsDataError, match="not found"):
        load_reports(tmp_path / "missing.json")


# test_load_reports_requires_five_entries - test that load_reports requires at least five reports
def test_load_reports_requires_five_entries(tmp_path) -> None:
    path = tmp_path / "reports.json"
    path.write_text(json.dumps(["only one"]), encoding="utf-8")

    with pytest.raises(ReportsDataError, match="at least 5"):
        load_reports(path)
