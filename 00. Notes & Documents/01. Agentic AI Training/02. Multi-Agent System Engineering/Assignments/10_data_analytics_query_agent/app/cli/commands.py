"""CLI command handlers."""

from __future__ import annotations

import sys

from app.cli.output import print_answer, print_question
from app.graph.builder import build_graph
from app.graph.state import AnalyticsState, initial_state
from app.services.database import get_sql_database
from app.services.llm_service import LLMService

# DEMO_QUERIES - evaluator sample questions for the demo command
DEMO_QUERIES = [
    "How many tasks are currently blocked?",
    "List all tasks along with the name of the team member assigned to each",
    "Show me all high or critical priority projects",
    "What is the average story points per assignee?",
]


# run_query - execute the reflection-loop graph for a single question
def run_query(
    question: str,
    *,
    service: LLMService | None = None,
) -> AnalyticsState:
    """Run the analytics query pipeline and return the final graph state."""
    llm = service or LLMService()
    graph = build_graph(llm)
    schema_info = get_sql_database().get_table_info()
    print_question(question)
    result = graph.invoke(initial_state(question, schema_info))
    print_answer(result["answer"])
    return result


# cmd_ask - ask one question and return an exit code
def cmd_ask(
    question: str,
    *,
    service: LLMService | None = None,
) -> int:
    """Ask one analytics question and return an exit code."""
    try:
        run_query(question, service=service)
    except (RuntimeError, FileNotFoundError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1
    return 0


# cmd_demo - run all evaluator sample queries and return an exit code
def cmd_demo(*, service: LLMService | None = None) -> int:
    """Run all demo queries and return an exit code."""
    for index, question in enumerate(DEMO_QUERIES, start=1):
        print(f"=== Demo query {index}/{len(DEMO_QUERIES)} ===")
        try:
            run_query(question, service=service)
        except (RuntimeError, FileNotFoundError) as exc:
            print(f"Error: {exc}", file=sys.stderr)
            return 1
    return 0
