"""Integration tests for the brief graph."""

from __future__ import annotations

from unittest.mock import MagicMock

from app.graph.builder import build_graph
from app.graph.state import initial_state
from app.services.llm_service import LLMService

# FACTS_PASS - researcher output with enough facts for the happy path
FACTS_PASS = """1. Event-driven systems decouple producers and consumers.
2. Messages are stored in durable logs before processing.
3. Consumers process events asynchronously at their own pace.
4. Event schemas enable contract testing between services.
5. Dead-letter queues capture failed event deliveries.
6. Idempotent handlers prevent duplicate side effects.
7. Event sourcing stores state as an append-only log.
"""

# ANALYST_PASS - analyst JSON with claim_count >= MIN_CLAIMS
ANALYST_PASS = """{
  "insights": ["Async decoupling improves resilience"],
  "claims": [
    "Event-driven systems decouple producers and consumers.",
    "Consumers process events asynchronously at their own pace.",
    "Dead-letter queues capture failed event deliveries.",
    "Idempotent handlers prevent duplicate side effects.",
    "Event sourcing stores state as an append-only log."
  ],
  "claim_count": 5
}"""

# ANALYST_FAIL - analyst JSON with claim_count below MIN_CLAIMS
ANALYST_FAIL = """{
  "insights": ["GraphQL is flexible"],
  "claims": [
    "GraphQL uses a single endpoint.",
    "REST maps resources to HTTP verbs.",
    "GraphQL clients request only needed fields."
  ],
  "claim_count": 3
}"""

# WRITER_OUTPUT - sample structured brief from the writer node
WRITER_OUTPUT = """## Overview
Event-driven architecture decouples services through asynchronous messages.

## Key Considerations
- Producers do not wait for consumers to finish processing.
- Schema contracts reduce integration breakage across teams.
- Dead-letter queues make failed deliveries observable.

## Recommendation
Adopt event-driven patterns when services need loose coupling and scalable async workflows.
"""


# test_happy_path_single_pass - test gate passes on first analyst pass
def test_happy_path_single_pass(test_settings) -> None:
    client = MagicMock()
    client.chat.completions.create.side_effect = [
        _response(FACTS_PASS),
        _response(ANALYST_PASS),
        _response(WRITER_OUTPUT),
    ]
    service = LLMService(settings=test_settings, client=client)
    result = build_graph(service).invoke(initial_state("Event-driven architecture"))

    assert result["claim_count"] == 5
    assert result["retry_count"] == 0
    assert "## Overview" in result["article"]
    assert result["research_incomplete"] is False


# test_retry_then_writer - test one researcher retry before the gate passes
def test_retry_then_writer(test_settings) -> None:
    client = MagicMock()
    client.chat.completions.create.side_effect = [
        _response("1. GraphQL is flexible.\n2. REST is common.\n"),
        _response(ANALYST_FAIL),
        _response("3. GraphQL reduces over-fetching.\n4. REST caches well on HTTP.\n"),
        _response(ANALYST_PASS),
        _response(WRITER_OUTPUT),
    ]
    service = LLMService(settings=test_settings, client=client)
    result = build_graph(service).invoke(initial_state("GraphQL vs REST APIs"))

    assert result["retry_count"] == 1
    assert result["claim_count"] == 5
    assert result["research_incomplete"] is False


# test_writer_runs_after_retry_limit_with_incomplete_note - test writer runs with incomplete note
def test_writer_runs_after_retry_limit_with_incomplete_note(test_settings) -> None:
    client = MagicMock()
    client.chat.completions.create.side_effect = [
        _response("1. GraphQL is flexible.\n"),
        _response(ANALYST_FAIL),
        _response("2. REST uses HTTP verbs.\n"),
        _response(ANALYST_FAIL),
        _response("3. GraphQL schemas are strongly typed.\n"),
        _response(ANALYST_FAIL),
        _response(WRITER_OUTPUT),
    ]
    service = LLMService(settings=test_settings, client=client)
    result = build_graph(service).invoke(initial_state("GraphQL vs REST APIs"))

    assert result["retry_count"] == 2
    assert result["research_incomplete"] is True
    assert "Research incomplete" in result["article"]


# _response - build a mocked chat completion response
def _response(content: str) -> MagicMock:
    return MagicMock(
        choices=[MagicMock(message=MagicMock(content=content))]
    )
