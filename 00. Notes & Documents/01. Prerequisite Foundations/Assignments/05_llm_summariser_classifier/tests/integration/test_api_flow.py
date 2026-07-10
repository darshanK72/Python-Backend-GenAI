"""Integration tests for secured LLM API flow."""

from __future__ import annotations

from unittest.mock import MagicMock

from fastapi.testclient import TestClient

from app.dependencies import get_llm_service
from app.main import app
from app.schemas.llm import ClassifyResult, SummariseResult
from app.services.llm_service import LLMService


def test_secured_summarise_and_classify_flow(
    llm_service: LLMService,
    auth_headers: dict[str, str],
) -> None:
    llm_service.summarise_text = MagicMock(
        return_value=SummariseResult(summary="Sprint update.", word_count=2),
    )
    llm_service.classify_text = MagicMock(
        return_value=ClassifyResult(
            category="question",
            confidence=0.81,
            rationale="Asks whether a feature exists.",
        ),
    )
    app.dependency_overrides[get_llm_service] = lambda: llm_service

    with TestClient(app) as client:
        health = client.get("/health")
        summarise = client.post(
            "/summarise",
            headers=auth_headers,
            json={"text": "Long sprint planning notes."},
        )
        classify = client.post(
            "/classify",
            headers=auth_headers,
            json={"text": "Is there an export option yet?"},
        )

    assert health.status_code == 200
    assert summarise.status_code == 200
    assert classify.status_code == 200
    assert classify.json()["category"] == "question"
