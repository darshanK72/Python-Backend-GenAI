"""Corrective RAG graph state."""

from __future__ import annotations

from typing import TypedDict


class DocChunk(TypedDict):
    """A single retrieved or graded document chunk."""

    doc_title: str
    chunk_index: int
    content: str


class RAGState(TypedDict):
    """Shared LangGraph state for the corrective RAG pipeline."""

    question: str
    retrieved_docs: list[DocChunk]
    relevant_docs: list[DocChunk]
    grading_trace: list[str]
    answer: str


# initial_state - build the starting state for a new Q&A run
def initial_state(question: str) -> RAGState:
    """Build the starting state for a new Q&A run."""
    return RAGState(
        question=question,
        retrieved_docs=[],
        relevant_docs=[],
        grading_trace=[],
        answer="",
    )
