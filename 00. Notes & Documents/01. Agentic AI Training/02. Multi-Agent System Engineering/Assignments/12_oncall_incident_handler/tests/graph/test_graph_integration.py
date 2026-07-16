"""Integration tests for memory and routing."""

from __future__ import annotations

from unittest.mock import MagicMock

from app.cli.commands import thread_config
from app.config import THREAD_ID
from app.graph.main_graph.builder import build_graph
from app.graph.main_graph.state import incident_input
from app.services.incident_loader import load_incident
from app.services.llm_service import LLMService

# ROOT_CAUSE - mocked escalation root-cause output
ROOT_CAUSE = """Most likely cause: Connection pool saturation under peak load.
Evidence:
- 2340 affected users in ap-south-1
- payment-gateway DB connection pool exhausted
- critical severity incident"""

# REMEDIATION - mocked escalation remediation output
REMEDIATION = """1. [5 min] Scale connection pool limits.
2. [10 min] Drain unhealthy gateway pods.
3. [15 min] Fail over to read replica for auth checks.
4. [20 min] Validate pool metrics on dashboards.
5. [30 min] Post incident review with SRE."""

# RESPONSE_PLAN - mocked HIGH-severity response plan
RESPONSE_PLAN = """1. Rotate JWT signing keys immediately.
2. Invalidate active sessions for impacted region.
3. Monitor auth error rate for 30 minutes.
Estimated time to resolution: 45 minutes"""

# NOTIFICATION - mocked two-sentence notification
NOTIFICATION = "Summary sentence one. Summary sentence two."


# test_memory_cross_reference_on_third_incident - test INC-003 references INC-001 via memory
def test_memory_cross_reference_on_third_incident(test_settings, incident_paths) -> None:
    client = MagicMock()
    client.chat.completions.create.side_effect = [
        _response(ROOT_CAUSE),
        _response(REMEDIATION),
        _response(NOTIFICATION),
        _response(RESPONSE_PLAN),
        _response(NOTIFICATION),
        _response(NOTIFICATION),
    ]
    service = LLMService(settings=test_settings, client=client)
    graph = build_graph(service)
    config = thread_config(THREAD_ID)

    results = []
    for path in incident_paths:
        incident = load_incident(path)
        results.append(graph.invoke(incident_input(incident), config=config))

    snapshot = graph.get_state(config)
    history = snapshot.values["incident_history"]
    third = results[2]

    assert len(history) == 3
    assert "INC-001" in history[0]
    assert third["route"] == "medium_low"
    assert "INC-001" in third["cross_reference"]
    assert "payment-gateway" in third["cross_reference"]
    assert "INC-003 logged for monitoring" in third["log_message"]


# test_critical_incident_routes_to_escalation - test CRITICAL path invokes escalation sub-graph
def test_critical_incident_routes_to_escalation(test_settings, incident_paths) -> None:
    client = MagicMock()
    client.chat.completions.create.side_effect = [
        _response(ROOT_CAUSE),
        _response(REMEDIATION),
        _response(NOTIFICATION),
    ]
    service = LLMService(settings=test_settings, client=client)
    result = build_graph(service).invoke(
        incident_input(load_incident(incident_paths[0])),
        config=thread_config("test-critical"),
    )
    assert result["route"] == "critical"
    assert "🚨 PAGERDUTY ALERT" in result["escalation_output"]


# _response - build a mocked chat completion response
def _response(content: str) -> MagicMock:
    return MagicMock(
        choices=[MagicMock(message=MagicMock(content=content))]
    )
