"""Tests for CLI runner and exit codes."""

from pathlib import Path

import pytest

from app.cli.runner import main


def test_main_without_args_prints_usage_and_exits_nonzero(capsys) -> None:
    exit_code = main([])
    output = capsys.readouterr()

    assert exit_code == 1
    assert "Usage:" in output.err
    assert "summary" in output.err


def test_main_unknown_command_exits_nonzero(tasks_file: Path, capsys) -> None:
    exit_code = main(["nope"], tasks_file=tasks_file)
    output = capsys.readouterr()

    assert exit_code == 1
    assert "unknown command" in output.err.lower()


def test_main_tag_without_name_exits_nonzero(tasks_file: Path, capsys) -> None:
    exit_code = main(["tag"], tasks_file=tasks_file)
    output = capsys.readouterr()

    assert exit_code == 1
    assert "requires a tag name" in output.err


def test_main_missing_tasks_file_exits_nonzero(tmp_path: Path, capsys) -> None:
    missing = tmp_path / "missing.json"
    exit_code = main(["summary"], tasks_file=missing)
    output = capsys.readouterr()

    assert exit_code == 1
    assert "Error:" in output.err
    assert "not found" in output.err.lower()


def test_main_summary_succeeds(tasks_file: Path, capsys) -> None:
    exit_code = main(["summary"], tasks_file=tasks_file)
    output = capsys.readouterr()

    assert exit_code == 0
    assert "Task summary" in output.out


def test_main_points_succeeds(tasks_file: Path, capsys) -> None:
    exit_code = main(["points"], tasks_file=tasks_file)
    assert exit_code == 0
    assert "Total story points:" in capsys.readouterr().out


def test_main_load_succeeds(tasks_file: Path, capsys) -> None:
    exit_code = main(["load"], tasks_file=tasks_file)
    assert exit_code == 0
    assert "Open story points by assignee" in capsys.readouterr().out


def test_main_tag_succeeds(tasks_file: Path, capsys) -> None:
    path = tasks_file
    path.write_text(
        '[{"id": 1, "title": "Auth task", "assignee": "A", "story_points": 2, '
        '"status": "todo", "tags": ["auth"]}]',
        encoding="utf-8",
    )
    exit_code = main(["tag", "auth"], tasks_file=path)
    output = capsys.readouterr()

    assert exit_code == 0
    assert "Auth task" in output.out
