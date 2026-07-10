"""ReAct agent state schema."""

from __future__ import annotations

from typing import TypedDict


class AgentState(TypedDict):
    """Shared LangGraph state for the developer assist ReAct loop."""

    question: str
    scratchpad: str
    tool_call_count: int
    pending_action: str
    pending_action_input: str
    final_answer: str
    stopped_reason: str


def initial_state(question: str) -> AgentState:
    """Build the starting state for a new agent run."""
    return AgentState(
        question=question,
        scratchpad="",
        tool_call_count=0,
        pending_action="",
        pending_action_input="",
        final_answer="",
        stopped_reason="",
    )
