"""Load committed bug report fixtures."""

from __future__ import annotations

import json
from pathlib import Path

from app.config import DEFAULT_REPORTS_FILE


class ReportsDataError(ValueError):
    """Raised when reports.json is missing or invalid."""


def load_reports(path: Path | None = None) -> list[str]:
    """Load at least five bug report strings from JSON."""
    file_path = path or DEFAULT_REPORTS_FILE
    if not file_path.is_file():
        raise ReportsDataError(f"Reports file not found: {file_path}")

    with file_path.open(encoding="utf-8") as handle:
        data = json.load(handle)

    if not isinstance(data, list) or len(data) < 5:
        raise ReportsDataError("reports.json must contain at least 5 sample reports.")

    return [str(item) for item in data]
