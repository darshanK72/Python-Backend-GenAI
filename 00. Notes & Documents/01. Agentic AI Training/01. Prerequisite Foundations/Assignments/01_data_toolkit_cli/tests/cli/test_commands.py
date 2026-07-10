"""Tests for CLI command output."""

from app.cli.commands import cmd_load, cmd_points, cmd_summary, cmd_tag


def test_cmd_summary_prints_counts_and_totals(sample_tasks: list[dict], capsys) -> None:
    cmd_summary(sample_tasks)
    output = capsys.readouterr().out

    assert "Task summary" in output
    assert "todo" in output
    assert "total points" in output
    assert "open points" in output
    assert " 13" in output  # open points for sample_tasks


def test_cmd_points_without_status(sample_tasks: list[dict], capsys) -> None:
    cmd_points(sample_tasks, None)
    assert capsys.readouterr().out == "Total story points: 16\n"


def test_cmd_points_with_status_filter(sample_tasks: list[dict], capsys) -> None:
    cmd_points(sample_tasks, "done")
    assert capsys.readouterr().out == "Story points (done): 3\n"


def test_cmd_load_lists_all_assignees(sample_tasks: list[dict], capsys) -> None:
    cmd_load(sample_tasks, None)
    output = capsys.readouterr().out

    assert "Open story points by assignee" in output
    assert "Alice" in output
    assert "Bob" not in output


def test_cmd_load_single_assignee(sample_tasks: list[dict], capsys) -> None:
    cmd_load(sample_tasks, "Alice")
    assert capsys.readouterr().out == "Open story points for Alice: 13\n"


def test_cmd_load_unknown_assignee_reports_zero(sample_tasks: list[dict], capsys) -> None:
    cmd_load(sample_tasks, "Zoe")
    assert capsys.readouterr().out == "Open story points for Zoe: 0\n"


def test_cmd_tag_lists_matching_tasks(sample_tasks: list[dict], capsys) -> None:
    cmd_tag(sample_tasks, "auth")
    output = capsys.readouterr().out

    assert "Tasks tagged 'auth' (1)" in output
    assert "Alpha" in output


def test_cmd_tag_reports_when_no_matches(sample_tasks: list[dict], capsys) -> None:
    cmd_tag(sample_tasks, "devops")
    assert capsys.readouterr().out == "No tasks found for tag 'devops'.\n"
