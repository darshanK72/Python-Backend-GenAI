"""Tests for session history storage."""

from app.services.session_store import append_entry, format_history


def test_format_history_empty(session_store_file) -> None:
    assert format_history("thread-1") == "No prior queries in this session"


def test_format_history_lists_entries(session_store_file) -> None:
    append_entry(
        "thread-1",
        {
            "turn": 1,
            "query": "microservices question",
            "worker": "rag",
            "summary": "Compared architectures",
        },
    )
    recap = format_history("thread-1")
    assert "microservices question" in recap
    assert "[rag]" in recap
