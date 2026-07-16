"""Tests for CLI output formatting."""

from app.cli.output import (
    print_capacity_result,
    print_mcp_call,
    print_risk_result,
    print_sprint_builder_result,
)


# test_print_sprint_builder_result_formats_tasks - test numbered task output
def test_print_sprint_builder_result_formats_tasks(capsys) -> None:
    print_sprint_builder_result(
        "OAuth login",
        [
            {"title": "Add callback route", "assignee": "Sam", "story_points": 3},
            {"title": "Store tokens", "assignee": "Alex", "story_points": 5},
        ],
    )
    captured = capsys.readouterr().out
    assert "[sprint_builder]" in captured
    assert "Feature: OAuth login" in captured
    assert "1. Add callback route — 3 SP (Sam)" in captured
    assert "2. Store tokens — 5 SP (Alex)" in captured


# test_print_capacity_result_avoids_double_period - test capacity formatting
def test_print_capacity_result_avoids_double_period(capsys) -> None:
    print_capacity_result(
        "Sprint is at 16/40 SP. Under capacity by 24 SP.",
        "Sprint has room for additional items",
    )
    captured = capsys.readouterr().out
    assert "Capacity: Sprint is at 16/40 SP. Under capacity by 24 SP" in captured
    assert "24 SP.." not in captured
    assert "Recommendation: Sprint has room for additional items" in captured


# test_print_mcp_call_indents_output - test indented MCP logging
def test_print_mcp_call_indents_output(capsys) -> None:
    print_mcp_call("check_capacity", {"velocity": 40}, "Sprint is at 16/40 SP.")
    captured = capsys.readouterr().out
    assert "MCP: check_capacity(velocity=40)" in captured
    assert "Sprint is at 16/40 SP." in captured


# test_print_risk_result_formats_numbered_lines - test risk output indentation
def test_print_risk_result_formats_numbered_lines(capsys) -> None:
    print_risk_result("1. DB migration — high risk.\n2. Auth refresh — medium risk.")
    captured = capsys.readouterr().out
    assert "[risk_assessor]" in captured
    assert "1. DB migration — high risk." in captured
