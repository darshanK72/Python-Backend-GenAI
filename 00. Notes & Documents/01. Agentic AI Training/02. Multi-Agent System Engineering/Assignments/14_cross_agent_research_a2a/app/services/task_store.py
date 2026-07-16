"""In-memory task store for the ResearchAgent A2A server."""

from __future__ import annotations

from typing import Any

# TASK_STORE - in-memory map of task_id → TaskResult for polling
TASK_STORE: dict[str, dict[str, Any]] = {}


# save_task - store a completed TaskResult by id
def save_task(result: dict[str, Any]) -> None:
    """Store a completed TaskResult by id."""
    TASK_STORE[result["id"]] = result


# get_task - fetch a stored TaskResult or None
def get_task(task_id: str) -> dict[str, Any] | None:
    """Fetch a stored TaskResult or None."""
    return TASK_STORE.get(task_id)


# clear_tasks - reset the in-memory store (tests)
def clear_tasks() -> None:
    """Reset the in-memory store (tests)."""
    TASK_STORE.clear()
