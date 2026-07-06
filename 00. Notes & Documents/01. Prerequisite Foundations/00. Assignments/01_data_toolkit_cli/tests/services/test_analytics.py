"""Unit tests for analytics service."""

from pathlib import Path

import pytest

from app.services.analytics import (
    TaskDataError,
    assignee_load,
    count_by_status,
    filter_by_tag,
    load_tasks,
    total_points,
)


def test_load_tasks_reads_valid_json(tasks_file: Path) -> None:
    tasks = load_tasks(str(tasks_file))
    assert len(tasks) == 1
    assert tasks[0]["title"] == "T"


def test_load_tasks_missing_file_raises_clear_error(tmp_path: Path) -> None:
    with pytest.raises(TaskDataError, match="not found"):
        load_tasks(str(tmp_path / "missing.json"))


def test_load_tasks_malformed_json_raises_clear_error(tmp_path: Path) -> None:
    path = tmp_path / "bad.json"
    path.write_text("{not json", encoding="utf-8")
    with pytest.raises(TaskDataError, match="Invalid JSON"):
        load_tasks(str(path))


def test_load_tasks_rejects_non_array_json(tmp_path: Path) -> None:
    path = tmp_path / "object.json"
    path.write_text('{"id": 1}', encoding="utf-8")
    with pytest.raises(TaskDataError, match="JSON array"):
        load_tasks(str(path))


def test_count_by_status(sample_tasks: list[dict]) -> None:
    counts = count_by_status(sample_tasks)
    assert counts["todo"] == 1
    assert counts["done"] == 1
    assert counts["in_progress"] == 1
    assert counts["blocked"] == 0


def test_count_by_status_ignores_invalid_statuses() -> None:
    tasks = [{"status": "invalid"}, {"status": "todo"}]
    counts = count_by_status(tasks)
    assert counts["todo"] == 1
    assert sum(counts.values()) == 1


def test_total_points_all_and_filtered(sample_tasks: list[dict]) -> None:
    assert total_points(sample_tasks) == 16
    assert total_points(sample_tasks, status="done") == 3
    assert total_points(sample_tasks, status="todo") == 5


def test_total_points_treats_missing_story_points_as_zero() -> None:
    tasks = [{"story_points": 5}, {"status": "todo"}]
    assert total_points(tasks) == 5


def test_assignee_load_sorted_highest_first(sample_tasks: list[dict]) -> None:
    loads = assignee_load(sample_tasks)
    assert list(loads.items()) == [("Alice", 13)]


def test_assignee_load_excludes_done(sample_tasks: list[dict]) -> None:
    loads = assignee_load(sample_tasks)
    assert loads["Alice"] == 13
    assert "Bob" not in loads


def test_assignee_load_uses_unassigned_for_missing_assignee() -> None:
    tasks = [{"status": "todo", "story_points": 4}]
    loads = assignee_load(tasks)
    assert loads["unassigned"] == 4


def test_filter_by_tag_case_insensitive(sample_tasks: list[dict]) -> None:
    matches = filter_by_tag(sample_tasks, "backend")
    assert len(matches) == 2
    assert {task["id"] for task in matches} == {1, 3}


def test_filter_by_tag_returns_empty_when_no_match(sample_tasks: list[dict]) -> None:
    assert filter_by_tag(sample_tasks, "devops") == []
