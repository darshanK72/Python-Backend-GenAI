"""Escalation sub-graph state."""

from __future__ import annotations

from typing import TypedDict


class EscalationState(TypedDict):
    """State for the CRITICAL escalation StateGraph."""

    incident: dict
    incident_id: str
    severity: str
    service: str
    error: str
    affected_users: int
    region: str
    roster_index: int
    root_cause: str
    remediation: str
    pagerduty_alert: str


# initial_escalation_state - build starting EscalationState for a CRITICAL incident
def initial_escalation_state(incident: dict, roster_index: int) -> EscalationState:
    """Build starting EscalationState for a CRITICAL incident."""
    return EscalationState(
        incident=incident,
        incident_id=incident["incident_id"],
        severity=incident["severity"],
        service=incident["service"],
        error=incident["error"],
        affected_users=int(incident["affected_users"]),
        region=incident["region"],
        roster_index=roster_index,
        root_cause="",
        remediation="",
        pagerduty_alert="",
    )
