"""End-to-end CLI tests against committed sample data."""

from pathlib import Path

import pytest

from app.cli.runner import main
from app.config import DEFAULT_TASKS_FILE, PROJECT_ROOT
from app.services.analytics import load_tasks


def test_default_tasks_file_exists_and_has_twelve_tasks() -> None:
    tasks = load_tasks(str(DEFAULT_TASKS_FILE))
    assert len(tasks) >= 12


def test_summary_against_committed_data(capsys) -> None:
    exit_code = main(["summary"], tasks_file=DEFAULT_TASKS_FILE)
    output = capsys.readouterr().out

    assert exit_code == 0
    assert "total points" in output
    assert " 63" in output
    assert "open points" in output
    assert " 44" in output


def test_points_done_against_committed_data(capsys) -> None:
    exit_code = main(["points", "done"], tasks_file=DEFAULT_TASKS_FILE)
    assert exit_code == 0
    assert capsys.readouterr().out == "Story points (done): 19\n"


def test_load_bob_against_committed_data(capsys) -> None:
    exit_code = main(["load", "Bob"], tasks_file=DEFAULT_TASKS_FILE)
    assert exit_code == 0
    assert capsys.readouterr().out == "Open story points for Bob: 16\n"


def test_tag_auth_against_committed_data(capsys) -> None:
    exit_code = main(["tag", "auth"], tasks_file=DEFAULT_TASKS_FILE)
    output = capsys.readouterr().out

    assert exit_code == 0
    assert "Tasks tagged 'auth' (2)" in output
    assert "Design login screen" in output
    assert "Implement password reset" in output


def test_project_layout_has_expected_paths() -> None:
    assert (PROJECT_ROOT / "app" / "main.py").is_file()
    assert (PROJECT_ROOT / "data" / "tasks.json").is_file()
    assert (PROJECT_ROOT / "toolkit.py").is_file()
