"""Supervisor graph state."""

from __future__ import annotations

from typing import TypedDict


class SprintState(TypedDict):
    """Shared LangGraph state for the sprint planning supervisor loop."""

    requests: list[str]
    request_index: int
    current_request: str
    route: str
    worker_result: str
    results: list[str]
    finished: bool


# initial_state - build the starting state for a new sprint session
def initial_state(requests: list[str]) -> SprintState:
    """Build the starting state for a new sprint session."""
    return SprintState(
        requests=requests,
        request_index=0,
        current_request=requests[0] if requests else "",
        route="",
        worker_result="",
        results=[],
        finished=False,
    )
