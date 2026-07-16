"""Tests for POST /summarise and POST /classify."""

from __future__ import annotations

from unittest.mock import MagicMock

from fastapi.testclient import TestClient

from app.dependencies import get_llm_service
from app.main import app
from app.schemas.llm import ClassifyResult, SummariseResult
from app.services.llm_service import LLMService
from tests.conftest import make_chat_response

VALID_SUMMARY_JSON = (
    '{"summary":"Team discussed sprint blockers and release timing.",'
    '"word_count":8}'
)
VALID_CLASSIFY_JSON = (
    '{"category":"bug","confidence":0.93,'
    '"rationale":"Reports a reproducible crash."}'
)


# test_unauthed_summarise_is_401 - test that unauthenticated summarise returns 401
def test_unauthed_summarise_is_401(client: TestClient) -> None:
    response = client.post("/summarise", json={"text": "Some text to summarise."})
    assert response.status_code == 401


# test_unauthed_classify_is_401 - test that unauthenticated classify returns 401
def test_unauthed_classify_is_401(client: TestClient) -> None:
    response = client.post("/classify", json={"text": "Can we add dark mode?"})
    assert response.status_code == 401


# test_invalid_api_key_is_401 - test that an invalid API key returns 401
def test_invalid_api_key_is_401(client: TestClient) -> None:
    response = client.post(
        "/summarise",
        headers={"X-API-Key": "wrong-key"},
        json={"text": "Some text."},
    )
    assert response.status_code == 401


# test_empty_text_is_422 - test that empty text returns 422
def test_empty_text_is_422(client: TestClient, auth_headers: dict[str, str]) -> None:
    response = client.post(
        "/summarise",
        headers=auth_headers,
        json={"text": ""},
    )
    assert response.status_code == 422


# test_summarise_returns_expected_shape - test that summarise returns summary and word_count
def test_summarise_returns_expected_shape(
    llm_service: LLMService,
    auth_headers: dict[str, str],
    sample_summarise_result: SummariseResult,
) -> None:
    llm_service.summarise_text = MagicMock(return_value=sample_summarise_result)
    app.dependency_overrides[get_llm_service] = lambda: llm_service

    with TestClient(app) as client:
        response = client.post(
            "/summarise",
            headers=auth_headers,
            json={"text": "A long paragraph that should be summarised."},
        )

    assert response.status_code == 200
    payload = response.json()
    assert payload["summary"] == "Short summary."
    assert payload["word_count"] == 2


# test_classify_bug_report - test that classify returns category, confidence, and rationale
def test_classify_bug_report(
    llm_service: LLMService,
    auth_headers: dict[str, str],
    sample_classify_result: ClassifyResult,
) -> None:
    llm_service.classify_text = MagicMock(return_value=sample_classify_result)
    app.dependency_overrides[get_llm_service] = lambda: llm_service

    with TestClient(app) as client:
        response = client.post(
            "/classify",
            headers=auth_headers,
            json={"text": "The app crashes when I tap save on settings."},
        )

    assert response.status_code == 200
    payload = response.json()
    assert payload["category"] == "bug"
    assert payload["confidence"] == 0.92


# test_summarise_llm_invalid_json_returns_502 - test that invalid JSON from the LLM returns 502
def test_summarise_llm_invalid_json_returns_502(
    llm_service: LLMService,
    mock_client: MagicMock,
    auth_headers: dict[str, str],
) -> None:
    mock_client.chat.completions.create.side_effect = [
        make_chat_response("not json"),
        make_chat_response("still not json"),
    ]
    app.dependency_overrides[get_llm_service] = lambda: llm_service

    with TestClient(app) as client:
        response = client.post(
            "/summarise",
            headers=auth_headers,
            json={"text": "Some paragraph."},
        )

    assert response.status_code == 502
    assert "invalid JSON" in response.json()["detail"]


# test_classify_invalid_category_returns_502 - test that an invalid category returns 502
def test_classify_invalid_category_returns_502(
    llm_service: LLMService,
    mock_client: MagicMock,
    auth_headers: dict[str, str],
) -> None:
    mock_client.chat.completions.create.return_value = make_chat_response(
        '{"category":"urgent","confidence":0.5,"rationale":"Seems urgent."}',
    )
    app.dependency_overrides[get_llm_service] = lambda: llm_service

    with TestClient(app) as client:
        response = client.post(
            "/classify",
            headers=auth_headers,
            json={"text": "Fix this now."},
        )

    assert response.status_code == 502
    assert "invalid classification" in response.json()["detail"].lower()


# test_summarise_parses_valid_json_from_service - test that summarise parses valid JSON from the LLM
def test_summarise_parses_valid_json_from_service(
    llm_service: LLMService,
    mock_client: MagicMock,
    auth_headers: dict[str, str],
) -> None:
    mock_client.chat.completions.create.return_value = make_chat_response(VALID_SUMMARY_JSON)
    app.dependency_overrides[get_llm_service] = lambda: llm_service

    with TestClient(app) as client:
        response = client.post(
            "/summarise",
            headers=auth_headers,
            json={"text": "Long paragraph about sprint planning and blockers."},
        )

    assert response.status_code == 200
    payload = response.json()
    assert payload["word_count"] == 8
    assert "sprint" in payload["summary"].lower()


# test_classify_parses_valid_json_from_service - test that classify parses valid JSON from the LLM
def test_classify_parses_valid_json_from_service(
    llm_service: LLMService,
    mock_client: MagicMock,
    auth_headers: dict[str, str],
) -> None:
    mock_client.chat.completions.create.return_value = make_chat_response(VALID_CLASSIFY_JSON)
    app.dependency_overrides[get_llm_service] = lambda: llm_service

    with TestClient(app) as client:
        response = client.post(
            "/classify",
            headers=auth_headers,
            json={"text": "The app crashes when I tap save on the settings page."},
        )

    assert response.status_code == 200
    assert response.json()["category"] == "bug"
