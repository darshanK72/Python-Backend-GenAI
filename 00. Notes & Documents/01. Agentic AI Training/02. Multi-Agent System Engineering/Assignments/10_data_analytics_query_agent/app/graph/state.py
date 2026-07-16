"""LangGraph state for the analytics query agent."""

from __future__ import annotations

from typing import TypedDict


class AnalyticsState(TypedDict):
    """Shared LangGraph state for the SQL reflection loop."""

    question: str
    schema_info: str
    sql_query: str
    validation_error: str
    retry_count: int
    is_valid: bool
    columns: list[str]
    rows: list[tuple]
    summary: str
    answer: str


# initial_state - build the starting state for a new analytics query
def initial_state(question: str, schema_info: str) -> AnalyticsState:
    """Build the starting state for a new analytics query."""
    return AnalyticsState(
        question=question,
        schema_info=schema_info,
        sql_query="",
        validation_error="",
        retry_count=0,
        is_valid=False,
        columns=[],
        rows=[],
        summary="",
        answer="",
    )
