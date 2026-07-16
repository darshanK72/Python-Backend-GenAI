"""Tests for CLI runner and exit codes."""

from pathlib import Path

from app.cli.runner import main

# test_main_without_args_prints_usage_and_exits_nonzero - test that the main function prints the usage and exits with a non-zero code when no arguments are provided
def test_main_without_args_prints_usage_and_exits_nonzero(capsys) -> None:
    exit_code = main([])
    output = capsys.readouterr()

    assert exit_code == 1
    assert "Usage:" in output.err
    assert "summary" in output.err
    assert "Commands:" in output.err

# test_main_help_exits_zero - test that the main function exits with a zero code when the help command is provided
def test_main_help_exits_zero(capsys) -> None:
    exit_code = main(["--help"])
    output = capsys.readouterr()

    assert exit_code == 0
    assert "Usage:" in output.out
    assert "summary" in output.out
    assert "points" in output.out

# test_main_help_command_exits_zero - test that the main function exits with a zero code when the help command is provided
def test_main_help_command_exits_zero(capsys) -> None:
    exit_code = main(["help"])
    output = capsys.readouterr()

    assert exit_code == 0
    assert "Commands:" in output.out
    assert "summary" in output.out

# test_main_unknown_command_exits_nonzero - test that the main function exits with a non-zero code when an unknown command is provided
def test_main_unknown_command_exits_nonzero(tasks_file: Path, capsys) -> None:
    exit_code = main(["nope"], tasks_file=tasks_file)
    output = capsys.readouterr()

    assert exit_code == 1
    assert "not a toolkit command" in output.err.lower()
    assert "Commands:" in output.err
    assert "summary" in output.err
    assert "points" in output.err
    assert "load" in output.err
    assert "tag" in output.err

# test_main_unknown_command_suggests_similar_commands - test that the main function suggests similar commands when an unknown command is provided
def test_main_unknown_command_suggests_similar_commands(tasks_file: Path, capsys) -> None:
    exit_code = main(["summry"], tasks_file=tasks_file)
    output = capsys.readouterr()

    assert exit_code == 1
    assert "most similar commands" in output.err.lower()
    assert "summary" in output.err

# test_main_tag_without_name_exits_nonzero - test that the main function exits with a non-zero code when the tag command is provided without a name
def test_main_tag_without_name_exits_nonzero(tasks_file: Path, capsys) -> None:
    exit_code = main(["tag"], tasks_file=tasks_file)
    output = capsys.readouterr()

    assert exit_code == 1
    assert "requires a tag name" in output.err.lower()
    assert "Commands:" in output.err

# test_main_missing_tasks_file_exits_nonzero - test that the main function exits with a non-zero code when the tasks file is missing
def test_main_missing_tasks_file_exits_nonzero(tmp_path: Path, capsys) -> None:
    missing = tmp_path / "missing.json"
    exit_code = main(["summary"], tasks_file=missing)
    output = capsys.readouterr()

    assert exit_code == 1
    assert "Error:" in output.err
    assert "not found" in output.err.lower()

# test_main_summary_succeeds - test that the main function succeeds when the summary command is provided
def test_main_summary_succeeds(tasks_file: Path, capsys) -> None:
    exit_code = main(["summary"], tasks_file=tasks_file)
    output = capsys.readouterr()

    assert exit_code == 0
    assert "Task summary" in output.out

# test_main_points_succeeds - test that the main function succeeds when the points command is provided
def test_main_points_succeeds(tasks_file: Path, capsys) -> None:
    exit_code = main(["points"], tasks_file=tasks_file)
    assert exit_code == 0
    assert "Total story points:" in capsys.readouterr().out

# test_main_load_succeeds - test that the main function succeeds when the load command is provided
def test_main_load_succeeds(tasks_file: Path, capsys) -> None:
    exit_code = main(["load"], tasks_file=tasks_file)
    assert exit_code == 0
    assert "Open story points by assignee" in capsys.readouterr().out

# test_main_tag_succeeds - test that the main function succeeds when the tag command is provided
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
