"""Unified assistant graph state."""

from __future__ import annotations

import operator
from typing import Annotated, TypedDict


class SessionEntry(TypedDict):
    """One turn recorded in session history."""

    turn: int
    query: str
    worker: str
    summary: str


class AssistantState(TypedDict):
    """LangGraph state for the unified engineering assistant."""

    messages: Annotated[list[dict[str, str]], operator.add]
    query: str
    route: str
    worker_result: str
    session_history: Annotated[list[SessionEntry], operator.add]
    thread_id: str
    turn: int
    finished: bool


# query_input - build the initial state payload for one user question
def query_input(query: str, thread_id: str, turn: int) -> dict:
    return {
        "query": query,
        "thread_id": thread_id,
        "turn": turn,
        "route": "",
        "worker_result": "",
        "finished": False,
        "messages": [{"role": "user", "content": query}],
    }
