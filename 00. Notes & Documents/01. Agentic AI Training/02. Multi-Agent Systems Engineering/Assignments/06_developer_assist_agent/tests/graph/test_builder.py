"""Tests for the LangGraph ReAct builder."""

from __future__ import annotations

from unittest.mock import MagicMock

from app.config import MAX_TOOL_CALLS
from app.graph.builder import build_graph, route_after_act, route_after_reason
from app.graph.state import initial_state
from app.services.llm_service import LLMService


def test_route_after_reason_end() -> None:
    state = initial_state("test")
    state["final_answer"] = "done"
    assert route_after_reason(state) == "end"


def test_route_after_reason_act() -> None:
    state = initial_state("test")
    state["pending_action"] = "story_estimator"
    assert route_after_reason(state) == "act"


def test_route_after_act_returns_reason() -> None:
    assert route_after_act(initial_state("test")) == "reason"


def test_graph_runs_react_loop_with_final_answer(test_settings) -> None:
    client = MagicMock()
    client.chat.completions.create.side_effect = [
        MagicMock(
            choices=[
                MagicMock(
                    message=MagicMock(
                        content=(
                            "Thought: Need an estimate.\n"
                            "Action: story_estimator\n"
                            "Action Input: CSV export"
                        )
                    )
                )
            ]
        ),
        MagicMock(
            choices=[
                MagicMock(
                    message=MagicMock(
                        content="5 points — export is straightforward. No backend changes needed."
                    )
                )
            ]
        ),
        MagicMock(
            choices=[
                MagicMock(
                    message=MagicMock(
                        content=(
                            "Thought: Enough evidence.\n"
                            "Final Answer: Estimate is 5 story points for CSV export."
                        )
                    )
                )
            ]
        ),
    ]
    service = LLMService(settings=test_settings, client=client)
    graph = build_graph(service)
    result = graph.invoke(initial_state("Estimate CSV export effort"))

    assert result["tool_call_count"] == 1
    assert "5 story points" in result["final_answer"]
    assert result["stopped_reason"] == "final_answer"


def test_graph_stops_at_max_tool_calls(test_settings) -> None:
    client = MagicMock()
    action_response = MagicMock(
        choices=[
            MagicMock(
                message=MagicMock(
                    content=(
                        "Thought: Need more data.\n"
                        "Action: story_estimator\n"
                        "Action Input: keep looping"
                    )
                )
            )
        ]
    )
    tool_response = MagicMock(
        choices=[
            MagicMock(
                message=MagicMock(
                    content="5 points — still working. More detail needed."
                )
            )
        ]
    )
    finalize_response = MagicMock(
        choices=[
            MagicMock(
                message=MagicMock(
                    content="Final Answer: Best effort answer after tool budget exhausted."
                )
            )
        ]
    )
    client.chat.completions.create.side_effect = [
        action_response,
        tool_response,
    ] * MAX_TOOL_CALLS + [finalize_response]

    service = LLMService(settings=test_settings, client=client)
    graph = build_graph(service)
    result = graph.invoke(initial_state("Loop until capped"))

    assert result["tool_call_count"] == MAX_TOOL_CALLS
    assert result["stopped_reason"] == "max_iterations"
    assert "Best effort answer" in result["final_answer"]
