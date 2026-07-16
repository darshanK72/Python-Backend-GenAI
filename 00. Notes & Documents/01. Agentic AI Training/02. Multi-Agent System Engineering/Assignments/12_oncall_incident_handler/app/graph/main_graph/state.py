"""Main incident handler graph state."""

from __future__ import annotations

import operator
from typing import Annotated, TypedDict


class IncidentState(TypedDict):
    """LangGraph state for the main on-call routing graph."""

    incident: dict
    incident_id: str
    severity: str
    service: str
    error: str
    affected_users: int
    region: str
    route: str
    incident_history: Annotated[list[str], operator.add]
    cross_reference: str
    response_plan: str
    log_message: str
    escalation_output: str
    notification: str
    roster_index: int


# incident_input - build invoke payload for a new incident (history from MemorySaver)
def incident_input(incident: dict) -> dict:
    """Pass only the new incident; MemorySaver keeps incident_history across calls."""
    return {
        "incident": incident,
        "route": "",
        "cross_reference": "",
        "response_plan": "",
        "log_message": "",
        "escalation_output": "",
        "notification": "",
    }
