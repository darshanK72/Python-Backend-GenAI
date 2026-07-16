"""Escalation sub-graph nodes for CRITICAL incidents."""

from __future__ import annotations

from app.cli.output import print_escalation_section
from app.config import ONCALL_ROSTER
from app.graph.escalation_graph.escalation_state import EscalationState
from app.schemas.prompts import REMEDIATION_SYSTEM, REMEDIATION_USER, ROOT_CAUSE_SYSTEM, ROOT_CAUSE_USER
from app.services.llm_service import LLMService


# make_root_cause_node - create the root-cause hypothesis node
def make_root_cause_node(service: LLMService):
    """Create the root-cause hypothesis node."""

    def root_cause_node(state: EscalationState) -> EscalationState:
        root_cause = service.chat(
            [
                {"role": "system", "content": ROOT_CAUSE_SYSTEM},
                {
                    "role": "user",
                    "content": ROOT_CAUSE_USER.format(
                        incident_id=state["incident_id"],
                        service=state["service"],
                        error=state["error"],
                        affected_users=state["affected_users"],
                        region=state["region"],
                    ),
                },
            ],
            temperature=0.2,
        ).strip()
        print_escalation_section("root_cause", root_cause)
        return EscalationState(
            incident=state["incident"],
            incident_id=state["incident_id"],
            severity=state["severity"],
            service=state["service"],
            error=state["error"],
            affected_users=state["affected_users"],
            region=state["region"],
            roster_index=state["roster_index"],
            root_cause=root_cause,
            remediation=state["remediation"],
            pagerduty_alert=state["pagerduty_alert"],
        )

    return root_cause_node


# make_remediation_node - create the five-step remediation node
def make_remediation_node(service: LLMService):
    """Create the five-step remediation node."""

    def remediation_node(state: EscalationState) -> EscalationState:
        remediation = service.chat(
            [
                {"role": "system", "content": REMEDIATION_SYSTEM},
                {
                    "role": "user",
                    "content": REMEDIATION_USER.format(
                        incident_id=state["incident_id"],
                        service=state["service"],
                        error=state["error"],
                        root_cause=state["root_cause"],
                    ),
                },
            ],
            temperature=0.2,
        ).strip()
        print_escalation_section("remediation", remediation)
        return EscalationState(
            incident=state["incident"],
            incident_id=state["incident_id"],
            severity=state["severity"],
            service=state["service"],
            error=state["error"],
            affected_users=state["affected_users"],
            region=state["region"],
            roster_index=state["roster_index"],
            root_cause=state["root_cause"],
            remediation=remediation,
            pagerduty_alert=state["pagerduty_alert"],
        )

    return remediation_node


# make_pagerduty_node - create the simulated PagerDuty alert node
def make_pagerduty_node():
    """Create the simulated PagerDuty alert node."""

    def pagerduty_node(state: EscalationState) -> EscalationState:
        assignee = ONCALL_ROSTER[state["roster_index"] % len(ONCALL_ROSTER)]
        alert = (
            f"🚨 PAGERDUTY ALERT | Incident: {state['incident_id']} | "
            f"Severity: CRITICAL | Service: {state['service']} | "
            f"Assigned to: {assignee} | "
            f"Runbook: https://runbooks.internal/{state['service']}/p0"
        )
        print_escalation_section("pagerduty", alert)
        return EscalationState(
            incident=state["incident"],
            incident_id=state["incident_id"],
            severity=state["severity"],
            service=state["service"],
            error=state["error"],
            affected_users=state["affected_users"],
            region=state["region"],
            roster_index=state["roster_index"],
            root_cause=state["root_cause"],
            remediation=state["remediation"],
            pagerduty_alert=alert,
        )

    return pagerduty_node
