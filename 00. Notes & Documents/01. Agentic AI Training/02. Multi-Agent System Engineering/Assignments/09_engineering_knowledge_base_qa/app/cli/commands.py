"""CLI command handlers."""

from __future__ import annotations

import sys

from app.cli.output import print_question, print_run_summary
from app.graph.builder import build_graph
from app.graph.state import RAGState, initial_state
from app.services.llm_service import LLMService
from app.services.vector_store import VectorStore

# DEMO_QUERIES - evaluator sample questions for the demo command
DEMO_QUERIES = [
    "What is trunk-based development and why do teams adopt it?",
    "How does technical debt accumulate and how should teams address it?",
    "What is the difference between microservices and a monolith?",
    "What are the current interest rates set by the Federal Reserve?",
]


# run_query - execute the corrective RAG graph for a single question
def run_query(
    question: str,
    *,
    service: LLMService | None = None,
    store: VectorStore | None = None,
) -> RAGState:
    """Run the knowledge-base Q&A pipeline and return the final graph state."""
    llm = service or LLMService()
    graph = build_graph(llm, store)
    print_question(question)
    result = graph.invoke(initial_state(question))
    print_run_summary(result)
    return result


# cmd_ask - ask one question and return an exit code
def cmd_ask(
    question: str,
    *,
    service: LLMService | None = None,
    store: VectorStore | None = None,
) -> int:
    """Ask one question and return an exit code."""
    try:
        run_query(question, service=service, store=store)
    except (RuntimeError, FileNotFoundError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1
    return 0


# cmd_demo - run all evaluator sample queries and return an exit code
def cmd_demo(
    *,
    service: LLMService | None = None,
    store: VectorStore | None = None,
) -> int:
    """Run all demo queries and return an exit code."""
    for index, question in enumerate(DEMO_QUERIES, start=1):
        print(f"=== Demo query {index}/{len(DEMO_QUERIES)} ===")
        try:
            run_query(question, service=service, store=store)
        except (RuntimeError, FileNotFoundError) as exc:
            print(f"Error: {exc}", file=sys.stderr)
            return 1
    return 0
