"""Integration tests for the writer LangGraph."""

from __future__ import annotations

from unittest.mock import MagicMock

from app.graph.builder import build_graph
from app.graph.state import initial_state
from app.services.llm_service import LLMService
from tests.conftest import SAMPLE_ARTICLE, SAMPLE_RESEARCH


# test_writer_graph_discovers_delegates_and_writes - test full graph with mocked A2A + LLM
def test_writer_graph_discovers_delegates_and_writes(
    test_settings,
    mock_http_client,
) -> None:
    client = MagicMock()
    client.chat.completions.create.return_value = MagicMock(
        choices=[MagicMock(message=MagicMock(content=SAMPLE_ARTICLE))]
    )
    llm = LLMService(settings=test_settings, client=client)
    result = build_graph(llm, http_client=mock_http_client).invoke(
        initial_state("Event-driven architecture")
    )

    assert result["agent_card"]["name"] == "ResearchAgent"
    assert result["task_id"]
    assert "3 Key Facts" in result["research_result"]
    assert "event-driven" in result["article"].lower() or "Event-driven" in result["article"]


# test_a2a_client_discover_and_delegate - test httpx helpers parse AgentCard and task output
def test_a2a_client_discover_and_delegate(mock_http_client) -> None:
    from app.services.a2a_client import delegate_task, discover_agent

    card = discover_agent(client=mock_http_client)
    assert card["skills"][0]["name"] == "research"
    task_id, output = delegate_task("Observability", client=mock_http_client)
    assert task_id
    assert "Current Trends" in output
    assert SAMPLE_RESEARCH in output or "3 Key Facts" in output
