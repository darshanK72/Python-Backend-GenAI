"""CLI runner for the developer assist agent."""

from __future__ import annotations

import sys
from pathlib import Path

from app.cli.output import print_question, print_run_summary
from app.config import DEFAULT_SAMPLE_DOC, USAGE
from app.graph.builder import build_graph
from app.graph.state import AgentState, initial_state
from app.services.llm_service import LLMService


def run_agent(question: str, *, service: LLMService | None = None) -> AgentState:
    llm = service or LLMService()
    graph = build_graph(llm)
    print_question(question)
    result = graph.invoke(initial_state(question))
    if not result.get("final_answer"):
        print_run_summary(result)
    return result


def load_sample_doc(path: Path | None = None) -> str:
    doc_path = path or DEFAULT_SAMPLE_DOC
    if not doc_path.is_file():
        raise FileNotFoundError(f"Sample documentation not found: {doc_path}")
    return doc_path.read_text(encoding="utf-8")


def demo_queries(sample_doc_path: Path | None = None) -> list[str]:
    sample_doc = load_sample_doc(sample_doc_path)
    return [
        "Estimate the effort for adding a CSV export feature to the admin dashboard",
        "What stack should I use to build a real-time notification system?",
        f"Summarise this doc: {sample_doc}",
        "I need to add OAuth login — what tech should I use and how much effort will it take?",
    ]


def run_demo(*, sample_doc_path: Path | None = None) -> int:
    try:
        queries = demo_queries(sample_doc_path)
    except FileNotFoundError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1

    for index, query in enumerate(queries, start=1):
        print(f"=== Demo query {index}/{len(queries)} ===")
        run_agent(query)
    return 0


def main(argv: list[str] | None = None) -> int:
    args = list(sys.argv[1:] if argv is None else argv)
    if not args:
        print(USAGE, file=sys.stderr)
        return 1

    if args[0].lower() == "demo":
        return run_demo()

    question = " ".join(args).strip()
    if not question:
        print(USAGE, file=sys.stderr)
        return 1

    try:
        run_agent(question)
    except RuntimeError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1
    return 0
