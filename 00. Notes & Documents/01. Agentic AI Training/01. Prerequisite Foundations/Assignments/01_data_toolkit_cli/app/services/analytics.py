"""Sprint task analytics service."""

from __future__ import annotations

import json
from pathlib import Path

VALID_STATUSES = frozenset({"todo", "in_progress", "done", "blocked"})


class TaskDataError(Exception):
    """Raised when task data cannot be loaded or parsed."""


def load_tasks(path: str) -> list[dict]:
    """Read and parse a JSON file containing a list of task objects."""
    file_path = Path(path)
    if not file_path.is_file():
        raise TaskDataError(f"Task file not found: {path}")

    try:
        raw = file_path.read_text(encoding="utf-8")
        data = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise TaskDataError(f"Invalid JSON in task file: {exc.msg}") from exc
    except OSError as exc:
        raise TaskDataError(f"Could not read task file: {exc}") from exc

    if not isinstance(data, list):
        raise TaskDataError("Task file must contain a JSON array of tasks.")

    return data


def count_by_status(tasks: list[dict]) -> dict[str, int]:
    """Return a count of tasks per status."""
    counts: dict[str, int] = {status: 0 for status in sorted(VALID_STATUSES)}
    for task in tasks:
        status = task.get("status")
        if status in VALID_STATUSES:
            counts[status] += 1
    return counts


def total_points(tasks: list[dict], status: str | None = None) -> int:
    """Sum story_points across all tasks, or only those matching status."""
    total = 0
    for task in tasks:
        if status is not None and task.get("status") != status:
            continue
        total += int(task.get("story_points", 0))
    return total


def assignee_load(tasks: list[dict]) -> dict[str, int]:
    """Return total open (non-done) story points per assignee, highest first."""
    loads: dict[str, int] = {}
    for task in tasks:
        if task.get("status") == "done":
            continue
        assignee = str(task.get("assignee", "unassigned"))
        loads[assignee] = loads.get(assignee, 0) + int(task.get("story_points", 0))
    return dict(sorted(loads.items(), key=lambda item: (-item[1], item[0])))


def filter_by_tag(tasks: list[dict], tag: str) -> list[dict]:
    """Return tasks whose tags list contains the given tag (case-insensitive)."""
    needle = tag.casefold()
    return [
        task
        for task in tasks
        if any(str(item).casefold() == needle for item in task.get("tags", []))
    ]
