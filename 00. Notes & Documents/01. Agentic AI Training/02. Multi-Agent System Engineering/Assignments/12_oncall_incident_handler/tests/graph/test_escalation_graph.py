"""Tests for the escalation sub-graph."""

from __future__ import annotations

from unittest.mock import MagicMock

from app.graph.escalation_graph.escalation_builder import build_escalation_graph
from app.graph.escalation_graph.escalation_state import initial_escalation_state
from app.services.llm_service import LLMService

# ROOT_CAUSE - mocked root-cause analysis text
ROOT_CAUSE = """Most likely cause: Connection pool saturation under peak load.
Evidence:
- 2340 affected users in ap-south-1
- payment-gateway DB connection pool exhausted
- critical severity incident"""

# REMEDIATION - mocked five-step remediation text
REMEDIATION = """1. [5 min] Scale connection pool limits.
2. [10 min] Drain unhealthy gateway pods.
3. [15 min] Fail over to read replica for auth checks.
4. [20 min] Validate pool metrics on dashboards.
5. [30 min] Post incident review with SRE."""

# INCIDENT - sample CRITICAL payment-gateway incident payload
INCIDENT = {
    "incident_id": "INC-001",
    "severity": "critical",
    "service": "payment-gateway",
    "error": "DB connection pool exhausted",
    "affected_users": 2340,
    "region": "ap-south-1",
}


# test_escalation_graph_produces_pagerduty_alert - test sub-graph outputs hypothesis, steps, alert
def test_escalation_graph_produces_pagerduty_alert(test_settings) -> None:
    client = MagicMock()
    client.chat.completions.create.side_effect = [
        _response(ROOT_CAUSE),
        _response(REMEDIATION),
    ]
    service = LLMService(settings=test_settings, client=client)
    result = build_escalation_graph(service).invoke(initial_escalation_state(INCIDENT, 0))

    assert "Most likely cause:" in result["root_cause"]
    assert "1." in result["remediation"]
    assert "🚨 PAGERDUTY ALERT" in result["pagerduty_alert"]
    assert "INC-001" in result["pagerduty_alert"]
    assert "Assigned to: Alice Chen" in result["pagerduty_alert"]
    assert "runbooks.internal/payment-gateway/p0" in result["pagerduty_alert"]


# _response - build a mocked chat completion response
def _response(content: str) -> MagicMock:
    return MagicMock(
        choices=[MagicMock(message=MagicMock(content=content))]
    )
