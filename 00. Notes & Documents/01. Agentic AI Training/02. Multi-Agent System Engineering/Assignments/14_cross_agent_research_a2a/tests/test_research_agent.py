"""Tests for ResearchAgent A2A endpoints."""

from unittest.mock import patch

from fastapi.testclient import TestClient

from research_agent import app, run_research
from tests.conftest import SAMPLE_RESEARCH


# test_agent_card_endpoint - test AgentCard discovery returns required A2A fields
def test_agent_card_endpoint() -> None:
    client = TestClient(app)
    response = client.get("/.well-known/agent.json")
    assert response.status_code == 200
    card = response.json()
    assert card["name"] == "ResearchAgent"
    assert card["version"] == "1.0"
    assert card["url"] == "http://localhost:8001"
    assert card["skills"][0]["name"] == "research"


# test_tasks_send_and_get - test task delegation stores results for polling
def test_tasks_send_and_get() -> None:
    client = TestClient(app)
    payload = {
        "id": "task-123",
        "message": {"role": "user", "content": "Event-driven architecture"},
    }
    with patch("research_agent.run_research", return_value=SAMPLE_RESEARCH):
        response = client.post("/tasks/send", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "completed"
    assert "3 Key Facts" in data["output"]

    stored = client.get("/tasks/task-123")
    assert stored.status_code == 200
    assert stored.json()["id"] == "task-123"


# test_run_research_uses_structured_format - test research prompt path returns structured text
def test_run_research_uses_structured_format(test_settings, mock_client) -> None:
    from app.services.llm_service import LLMService

    output = run_research(
        "test topic",
        service=LLMService(settings=test_settings, client=mock_client),
    )
    assert "3 Key Facts" in output
