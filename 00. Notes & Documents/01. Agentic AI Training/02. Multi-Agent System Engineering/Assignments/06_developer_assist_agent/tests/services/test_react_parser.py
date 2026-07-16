"""Tests for ReAct response parsing."""

from __future__ import annotations

import pytest

from app.services.react_parser import ReActParseError, parse_react_response


# test_parse_action_response - test parsing Thought plus Action and Action Input
def test_parse_action_response() -> None:
    decision = parse_react_response(
        "Thought: Need an estimate.\n"
        "Action: story_estimator\n"
        "Action Input: CSV export for admin dashboard"
    )
    assert decision.thought == "Need an estimate."
    assert decision.action == "story_estimator"
    assert decision.action_input == "CSV export for admin dashboard"
    assert decision.final_answer == ""


# test_parse_final_answer_response - test parsing Thought plus Final Answer
def test_parse_final_answer_response() -> None:
    decision = parse_react_response(
        "Thought: I have enough context.\nFinal Answer: Use OAuth 2.0 with 5 points of effort."
    )
    assert decision.action is None
    assert decision.final_answer == "Use OAuth 2.0 with 5 points of effort."


# test_parse_unknown_action_raises - test that unknown tools raise ReActParseError
def test_parse_unknown_action_raises() -> None:
    with pytest.raises(ReActParseError):
        parse_react_response(
            "Thought: Bad tool.\nAction: unknown_tool\nAction Input: test"
        )
