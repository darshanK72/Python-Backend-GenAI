"""Tests for report fixture loading."""

from __future__ import annotations

import json

import pytest

from app.config import DEFAULT_REPORTS_FILE
from app.services.report_loader import ReportsDataError, load_reports


def test_load_reports_from_default_file() -> None:
    reports = load_reports(DEFAULT_REPORTS_FILE)

    assert len(reports) >= 5
    assert all(isinstance(report, str) for report in reports)


def test_load_reports_missing_file(tmp_path) -> None:
    with pytest.raises(ReportsDataError, match="not found"):
        load_reports(tmp_path / "missing.json")


def test_load_reports_requires_five_entries(tmp_path) -> None:
    path = tmp_path / "reports.json"
    path.write_text(json.dumps(["only one"]), encoding="utf-8")

    with pytest.raises(ReportsDataError, match="at least 5"):
        load_reports(path)
