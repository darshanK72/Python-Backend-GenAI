"""CLI command handlers."""

from __future__ import annotations

import sys
from pathlib import Path

from app.cli.output import print_question, print_run_summary
from app.config import DEFAULT_SAMPLE_DOC
from app.graph.builder import build_graph
from app.graph.state import AgentState, initial_state
from app.services.llm_service import LLMService


# run_agent - execute the ReAct LangGraph for a single question
def run_agent(question: str, *, service: LLMService | None = None) -> AgentState:
    """Run the developer assist agent and return the final graph state."""
    llm = service or LLMService()
    graph = build_graph(llm)
    print_question(question)
    result = graph.invoke(initial_state(question))
    if not result.get("final_answer"):
        print_run_summary(result)
    return result


# load_sample_doc - read the committed sample documentation file
def load_sample_doc(path: Path | None = None) -> str:
    """Load the sample LangGraph documentation used by the demo command."""
    doc_path = path or DEFAULT_SAMPLE_DOC
    if not doc_path.is_file():
        raise FileNotFoundError(f"Sample documentation not found: {doc_path}")
    return doc_path.read_text(encoding="utf-8")


# demo_queries - return the four evaluator sample queries
def demo_queries(sample_doc_path: Path | None = None) -> list[str]:
    """Return the four evaluator sample queries."""
    sample_doc = load_sample_doc(sample_doc_path)
    return [
        "Estimate the effort for adding a CSV export feature to the admin dashboard",
        "What stack should I use to build a real-time notification system?",
        f"Summarise this doc: {sample_doc}",
        "I need to add OAuth login — what tech should I use and how much effort will it take?",
    ]


# cmd_ask - run the agent for a single user question
def cmd_ask(question: str, *, service: LLMService | None = None) -> int:
    """Ask the agent one question and return an exit code."""
    try:
        run_agent(question, service=service)
    except RuntimeError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1
    return 0


# cmd_demo - run all four evaluator sample queries
def cmd_demo(
    *,
    sample_doc_path: Path | None = None,
    service: LLMService | None = None,
) -> int:
    """Run all demo queries and return an exit code."""
    try:
        queries = demo_queries(sample_doc_path)
    except FileNotFoundError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1

    for index, query in enumerate(queries, start=1):
        print(f"=== Demo query {index}/{len(queries)} ===")
        try:
            run_agent(query, service=service)
        except RuntimeError as exc:
            print(f"Error: {exc}", file=sys.stderr)
            return 1
    return 0
