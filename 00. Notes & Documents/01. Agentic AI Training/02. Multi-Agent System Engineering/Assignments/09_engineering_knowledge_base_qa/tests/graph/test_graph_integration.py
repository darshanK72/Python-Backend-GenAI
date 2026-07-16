"""Integration tests for corrective RAG graph."""

from __future__ import annotations

from unittest.mock import MagicMock

from app.graph.builder import build_graph
from app.graph.state import initial_state
from app.schemas.prompts import INSUFFICIENT_ANSWER, SINGLE_SOURCE_NOTE
from app.services.llm_service import LLMService


# test_out_of_scope_returns_insufficient - test Federal Reserve query returns insufficient info
def test_out_of_scope_returns_insufficient(test_settings, mock_store, mock_client) -> None:
    mock_client.chat.completions.create.side_effect = [
        _response("irrelevant"),
    ]
    llm = LLMService(settings=test_settings, client=mock_client)
    result = build_graph(llm, mock_store).invoke(
        initial_state("What are the current interest rates set by the Federal Reserve?")
    )
    assert result["answer"] == INSUFFICIENT_ANSWER
    assert any("irrelevant" in line for line in result["grading_trace"])


# test_single_source_adds_note - test exactly one relevant doc appends the incompleteness note
def test_single_source_adds_note(test_settings, mock_store, mock_client) -> None:
    mock_client.chat.completions.create.side_effect = [
        _response("relevant"),
        _response(
            "Technical debt grows when refactoring is deferred.\n\n"
            "Sources: [Technical debt]"
        ),
    ]
    llm = LLMService(settings=test_settings, client=mock_client)
    result = build_graph(llm, mock_store).invoke(
        initial_state("How does technical debt accumulate and how should teams address it?")
    )
    assert SINGLE_SOURCE_NOTE in result["answer"]
    assert "Sources:" in result["answer"]


# test_multi_source_answer - test two or more relevant docs produce a cited answer
def test_multi_source_answer(test_settings, mock_store, mock_client) -> None:
    mock_client.chat.completions.create.side_effect = [
        _response("relevant"),
        _response("relevant"),
        _response(
            "Microservices deploy independently while monoliths ship as one unit.\n\n"
            "Sources: [Microservices], [Software engineering]"
        ),
    ]
    llm = LLMService(settings=test_settings, client=mock_client)
    result = build_graph(llm, mock_store).invoke(
        initial_state("What is the difference between microservices and a monolith?")
    )
    assert "Sources:" in result["answer"]
    assert SINGLE_SOURCE_NOTE not in result["answer"]
    assert len(result["relevant_docs"]) == 2


# _response - build a mocked chat completion response
def _response(content: str) -> MagicMock:
    return MagicMock(
        choices=[MagicMock(message=MagicMock(content=content))]
    )
