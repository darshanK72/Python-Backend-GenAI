"""Tests for CLI output helpers."""

from __future__ import annotations

from app.cli.output import is_valid_structured_result


# test_is_valid_structured_result_accepts_known_severity - test that known severities are accepted
def test_is_valid_structured_result_accepts_known_severity() -> None:
    assert is_valid_structured_result({"severity": "high"}) is True


# test_is_valid_structured_result_rejects_unknown_severity - test that unknown severities are rejected
def test_is_valid_structured_result_rejects_unknown_severity() -> None:
    assert is_valid_structured_result({"severity": "urgent"}) is False
