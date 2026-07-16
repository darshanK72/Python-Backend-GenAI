"""Build and compile the analytics reflection LangGraph."""

from __future__ import annotations

import sqlite3
from pathlib import Path

from langgraph.graph import END, START, StateGraph

from app.config import DB_PATH, MAX_RETRIES
from app.graph.nodes import (
    make_executor_node,
    make_failure_node,
    make_generator_node,
    make_summarizer_node,
    make_validator_node,
)
from app.graph.state import AnalyticsState
from app.services.database import get_connection, load_schema_map
from app.services.llm_service import LLMService
from app.services.sql_validator import is_forbidden_verb_error


# route_after_validator - route to executor, retry generator, or failure
def route_after_validator(state: AnalyticsState) -> str:
    """Route to executor, retry generator, or failure based on validation."""
    if state["is_valid"]:
        return "executor"
    # Forbidden verbs are not fixable schema mistakes — do not retry as SELECT.
    if is_forbidden_verb_error(state["validation_error"]):
        return "failure"
    if state["retry_count"] <= MAX_RETRIES:
        return "generator"
    return "failure"


# build_graph - compile the generate → validate → execute/retry StateGraph
def build_graph(
    service: LLMService | None = None,
    db_path: Path = DB_PATH,
    conn: sqlite3.Connection | None = None,
):
    """Compile the generate → validate → execute/retry StateGraph."""
    llm = service or LLMService()
    connection = conn or get_connection(db_path)
    schema = load_schema_map(connection)

    builder = StateGraph(AnalyticsState)
    builder.add_node("generator", make_generator_node(llm))
    builder.add_node("validator", make_validator_node(connection, schema))
    builder.add_node("executor", make_executor_node(connection))
    builder.add_node("summarizer", make_summarizer_node(llm))
    builder.add_node("failure", make_failure_node())

    builder.add_edge(START, "generator")
    builder.add_edge("generator", "validator")
    builder.add_conditional_edges(
        "validator",
        route_after_validator,
        {
            "executor": "executor",
            "generator": "generator",
            "failure": "failure",
        },
    )
    builder.add_edge("executor", "summarizer")
    builder.add_edge("summarizer", END)
    builder.add_edge("failure", END)
    return builder.compile()
