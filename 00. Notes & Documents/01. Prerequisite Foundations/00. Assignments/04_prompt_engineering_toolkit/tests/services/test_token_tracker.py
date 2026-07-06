"""Tests for token usage tracking."""

from __future__ import annotations

from types import SimpleNamespace

from app.services.token_tracker import TokenTracker


def test_record_accumulates_tokens() -> None:
    tracker = TokenTracker()
    tracker.record(SimpleNamespace(prompt_tokens=10, completion_tokens=5))
    tracker.record(SimpleNamespace(prompt_tokens=3, completion_tokens=2))

    assert tracker.prompt_tokens == 13
    assert tracker.completion_tokens == 7
    assert tracker.running_total == 20


def test_reset_clears_totals() -> None:
    tracker = TokenTracker()
    tracker.record(SimpleNamespace(prompt_tokens=1, completion_tokens=1))
    tracker.reset()

    assert tracker.running_total == 0


def test_format_last_call_includes_running_total() -> None:
    tracker = TokenTracker()
    tracker.record(SimpleNamespace(prompt_tokens=4, completion_tokens=6))
    usage = SimpleNamespace(prompt_tokens=2, completion_tokens=3)

    formatted = tracker.format_last_call(usage)

    assert "prompt=2" in formatted
    assert "completion=3" in formatted
    assert "running_total=10" in formatted
