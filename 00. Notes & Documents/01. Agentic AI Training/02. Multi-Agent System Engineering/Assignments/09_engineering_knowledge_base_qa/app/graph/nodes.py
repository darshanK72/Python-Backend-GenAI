"""Corrective RAG graph nodes."""

from __future__ import annotations

from langchain_core.documents import Document

from app.cli.output import print_grading_trace, print_retrieved
from app.config import RETRIEVAL_K
from app.graph.state import DocChunk, RAGState
from app.schemas.prompts import (
    GENERATOR_SYSTEM,
    GENERATOR_USER,
    GRADER_SYSTEM,
    GRADER_USER,
    INSUFFICIENT_ANSWER,
    SINGLE_SOURCE_NOTE,
)
from app.services.llm_service import LLMService
from app.services.vector_store import VectorStore


# _to_chunk - convert a LangChain Document into a DocChunk TypedDict
def _to_chunk(document: Document) -> DocChunk:
    return DocChunk(
        doc_title=document.metadata.get("doc_title", "Unknown"),
        chunk_index=int(document.metadata.get("chunk_index", 0)),
        content=document.page_content,
    )


# make_retriever_node - create the FAISS similarity-search node
def make_retriever_node(store: VectorStore):
    """Create the FAISS similarity-search node."""

    def retriever_node(state: RAGState) -> RAGState:
        docs = store.similarity_search(state["question"], k=RETRIEVAL_K)
        retrieved = [_to_chunk(doc) for doc in docs]
        print_retrieved(len(retrieved))
        return RAGState(
            question=state["question"],
            retrieved_docs=retrieved,
            relevant_docs=[],
            grading_trace=[],
            answer="",
        )

    return retriever_node


# make_grader_node - create the relevance grading node
def make_grader_node(service: LLMService):
    """Create the relevance grading node."""

    def grader_node(state: RAGState) -> RAGState:
        relevant: list[DocChunk] = []
        trace: list[str] = []
        for chunk in state["retrieved_docs"]:
            verdict = service.chat(
                [
                    {"role": "system", "content": GRADER_SYSTEM},
                    {
                        "role": "user",
                        "content": GRADER_USER.format(
                            question=state["question"],
                            text=chunk["content"],
                        ),
                    },
                ],
                temperature=0.0,
            ).strip().lower()
            if "irrelevant" in verdict:
                is_relevant = False
            elif "relevant" in verdict:
                is_relevant = True
            else:
                is_relevant = False
            label = "relevant" if is_relevant else "irrelevant"
            trace.append(
                f"{chunk['doc_title']} (chunk {chunk['chunk_index']}): {label}"
            )
            if is_relevant:
                relevant.append(chunk)
        print_grading_trace(trace)
        return RAGState(
            question=state["question"],
            retrieved_docs=state["retrieved_docs"],
            relevant_docs=relevant,
            grading_trace=trace,
            answer="",
        )

    return grader_node


# make_generator_node - create the answer generation node with citation rules
def make_generator_node(service: LLMService):
    """Create the answer generation node with citation rules."""

    def generator_node(state: RAGState) -> RAGState:
        count = len(state["relevant_docs"])
        if count == 0:
            answer = INSUFFICIENT_ANSWER
        elif count == 1:
            answer = _generate_answer(state, service)
            if SINGLE_SOURCE_NOTE not in answer:
                answer = f"{answer}\n\n{SINGLE_SOURCE_NOTE}"
        else:
            answer = _generate_answer(state, service)
        return RAGState(
            question=state["question"],
            retrieved_docs=state["retrieved_docs"],
            relevant_docs=state["relevant_docs"],
            grading_trace=state["grading_trace"],
            answer=answer,
        )

    return generator_node


# _generate_answer - ask the LLM for a grounded answer with Sources citation
def _generate_answer(state: RAGState, service: LLMService) -> str:
    sources = []
    titles: list[str] = []
    seen_titles: set[str] = set()
    for chunk in state["relevant_docs"]:
        title = chunk["doc_title"]
        sources.append(f"[{title}] {chunk['content']}")
        if title not in seen_titles:
            titles.append(title)
            seen_titles.add(title)
    source_titles = ", ".join(f"[{title}]" for title in titles)
    raw = service.chat(
        [
            {"role": "system", "content": GENERATOR_SYSTEM},
            {
                "role": "user",
                "content": GENERATOR_USER.format(
                    question=state["question"],
                    sources="\n\n".join(sources),
                    source_titles=source_titles,
                ),
            },
        ],
        temperature=0.2,
    ).strip()
    if "Sources:" not in raw and titles:
        raw = f"{raw}\n\nSources: {source_titles}"
    return raw
