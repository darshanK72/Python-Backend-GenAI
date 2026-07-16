"""Brief generator graph state."""

from __future__ import annotations

from typing import TypedDict


class BriefState(TypedDict):
    """Shared LangGraph state for the technical brief pipeline."""

    topic: str
    facts: list[str]
    insights: list[str]
    claims: list[str]
    claim_count: int
    retry_count: int
    article: str
    research_incomplete: bool


# initial_state - build the starting state for a new brief run
def initial_state(topic: str) -> BriefState:
    """Build the starting state for a new brief run."""
    return BriefState(
        topic=topic,
        facts=[],
        insights=[],
        claims=[],
        claim_count=0,
        retry_count=0,
        article="",
        research_incomplete=False,
    )
