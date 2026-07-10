"""Shared pytest fixtures."""

from __future__ import annotations

from pathlib import Path

import pytest

from app.config import DEFAULT_TASKS_FILE

SAMPLE_TASKS = [
    {
        "id": 1,
        "title": "Alpha",
        "assignee": "Alice",
        "story_points": 5,
        "status": "todo",
        "tags": ["Backend", "Auth"],
    },
    {
        "id": 2,
        "title": "Beta",
        "assignee": "Bob",
        "story_points": 3,
        "status": "done",
        "tags": ["frontend"],
    },
    {
        "id": 3,
        "title": "Gamma",
        "assignee": "Alice",
        "story_points": 8,
        "status": "in_progress",
        "tags": ["backend"],
    },
]


@pytest.fixture
def sample_tasks() -> list[dict]:
    return [task.copy() for task in SAMPLE_TASKS]


@pytest.fixture
def tasks_file(tmp_path: Path) -> Path:
    path = tmp_path / "tasks.json"
    path.write_text(
        '[{"id": 1, "title": "T", "assignee": "A", "story_points": 1, "status": "todo", "tags": []}]',
        encoding="utf-8",
    )
    return path


@pytest.fixture
def default_tasks_file() -> Path:
    assert DEFAULT_TASKS_FILE.is_file()
    return DEFAULT_TASKS_FILE
