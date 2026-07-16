"""Writer agent graph state."""

from __future__ import annotations

from typing import Any, TypedDict


class WriterState(TypedDict):
    """LangGraph state for discovery → delegation → writer."""

    topic: str
    agent_card: dict[str, Any]
    task_id: str
    research_result: str
    article: str


# initial_state - build starting WriterState for a topic
def initial_state(topic: str) -> WriterState:
    """Build starting WriterState for a topic."""
    return WriterState(
        topic=topic,
        agent_card={},
        task_id="",
        research_result="",
        article="",
    )
