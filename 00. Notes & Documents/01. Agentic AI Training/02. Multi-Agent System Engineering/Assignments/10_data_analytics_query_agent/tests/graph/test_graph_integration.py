"""Integration tests for the reflection loop."""

from __future__ import annotations

from unittest.mock import MagicMock

from app.config import FAILURE_MESSAGE
from app.graph.builder import build_graph
from app.graph.state import initial_state
from app.services.llm_service import LLMService


# test_graph_retries_after_invalid_sql - test one retry then successful execution
def test_graph_retries_after_invalid_sql(test_settings, temp_db, mock_client) -> None:
    bad_sql = "SELECT assigneed FROM tasks WHERE status = 'blocked'"
    good_sql = "SELECT COUNT(*) FROM tasks WHERE status = 'blocked'"
    mock_client.chat.completions.create.side_effect = [
        _response(bad_sql),
        _response(good_sql),
        _response("There are 2 blocked tasks."),
    ]
    llm = LLMService(settings=test_settings, client=mock_client)
    graph = build_graph(llm, db_path=temp_db)
    result = graph.invoke(
        initial_state("How many tasks are currently blocked?", "schema")
    )
    assert result["retry_count"] == 1
    assert "COUNT(*)" in result["sql_query"]
    assert result["rows"] == [(2,)]
    assert "Summary:" in result["answer"]


# test_graph_stops_after_max_retries - test failure message after three failed generations
def test_graph_stops_after_max_retries(test_settings, temp_db, mock_client) -> None:
    bad_sql = "SELECT assigneed FROM tasks"
    mock_client.chat.completions.create.side_effect = [
        _response(bad_sql),
        _response(bad_sql),
        _response(bad_sql),
    ]
    llm = LLMService(settings=test_settings, client=mock_client)
    graph = build_graph(llm, db_path=temp_db)
    result = graph.invoke(initial_state("Count tasks", "schema"))
    assert result["answer"] == FAILURE_MESSAGE
    assert result["retry_count"] == 3


# test_graph_rejects_delete_intent - test mutation questions fail with forbidden-verb error
def test_graph_rejects_delete_intent(test_settings, temp_db, mock_client) -> None:
    llm = LLMService(settings=test_settings, client=mock_client)
    graph = build_graph(llm, db_path=temp_db)
    result = graph.invoke(
        initial_state("delete team member Alice Chen", "schema")
    )
    mock_client.chat.completions.create.assert_not_called()
    assert "forbidden verb DELETE" in result["answer"]
    assert result["rows"] == []
    assert result["is_valid"] is False


# _response - build a mocked chat completion response
def _response(content: str) -> MagicMock:
    return MagicMock(
        choices=[MagicMock(message=MagicMock(content=content))]
    )
