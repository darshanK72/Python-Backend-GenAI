"""Console output for corrective RAG traces."""

from __future__ import annotations

from app.graph.state import RAGState


# print_question - print the question header
def print_question(question: str) -> None:
    """Print the question header."""
    print(f"\n{'=' * 60}")
    print("  Engineering KB Q&A")
    print(f"{'=' * 60}")
    print(f"\nQuestion: {question}\n")


# print_retrieved - print how many chunks the retriever returned
def print_retrieved(count: int) -> None:
    """Print how many chunks the retriever returned."""
    print(f"[retriever] retrieved {count} chunks\n")


# print_grading_trace - print per-chunk relevant/irrelevant decisions
def print_grading_trace(trace: list[str]) -> None:
    """Print per-chunk relevant/irrelevant decisions."""
    print("[grader] grading trace:")
    for line in trace:
        print(f"  {line}")
    print()


# print_answer - print the final generator answer
def print_answer(answer: str) -> None:
    """Print the final generator answer."""
    print("[generator]")
    for line in answer.splitlines():
        print(f"  {line}" if line else "")
    print()


# print_run_summary - print the final answer after a graph run
def print_run_summary(state: RAGState) -> None:
    """Print the final answer after a graph run."""
    print_answer(state["answer"])
