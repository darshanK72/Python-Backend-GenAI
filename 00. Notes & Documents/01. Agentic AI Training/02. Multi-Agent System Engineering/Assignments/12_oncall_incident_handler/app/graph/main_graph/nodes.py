"""Main incident handler graph nodes."""

from __future__ import annotations

from app.cli.output import (
    print_classifier,
    print_cross_reference,
    print_notification,
    print_route_output,
)
from app.graph.escalation_graph.escalation_state import initial_escalation_state
from app.graph.main_graph.state import IncidentState
from app.schemas.prompts import NOTIFICATION_SYSTEM, NOTIFICATION_USER, RESPONSE_SYSTEM, RESPONSE_USER
from app.services.incident_memory import (
    build_cross_reference,
    build_history_line,
    format_log_message,
)
from app.services.llm_service import LLMService


# _severity_route - map incident severity to main-graph route name
def _severity_route(severity: str) -> str:
    """Map incident severity to main-graph route name."""
    normalized = severity.strip().lower()
    if normalized == "critical":
        return "critical"
    if normalized == "high":
        return "high"
    return "medium_low"


# make_classifier_node - create the severity classifier and history/cross-ref node
def make_classifier_node():
    """Create the severity classifier and history/cross-ref node."""

    def classifier_node(state: IncidentState) -> IncidentState:
        incident = state["incident"]
        history = list(state.get("incident_history", []))
        cross_reference = build_cross_reference(
            incident["service"],
            incident["incident_id"],
            history,
        )
        summary = build_history_line(incident)
        route = _severity_route(incident["severity"])
        print_classifier(incident, route)
        if cross_reference:
            print_cross_reference(cross_reference)

        return IncidentState(
            incident=incident,
            incident_id=incident["incident_id"],
            severity=incident["severity"],
            service=incident["service"],
            error=incident["error"],
            affected_users=int(incident["affected_users"]),
            region=incident["region"],
            route=route,
            incident_history=[summary],
            cross_reference=cross_reference,
            response_plan=state.get("response_plan", ""),
            log_message=state.get("log_message", ""),
            escalation_output=state.get("escalation_output", ""),
            notification=state.get("notification", ""),
            roster_index=len(history),
        )

    return classifier_node


# make_escalation_invoke_node - create the node that invokes the escalation sub-graph
def make_escalation_invoke_node(escalation_graph):
    """Create the node that invokes the escalation sub-graph."""

    def escalation_invoke_node(state: IncidentState) -> IncidentState:
        result = escalation_graph.invoke(
            initial_escalation_state(state["incident"], state["roster_index"])
        )
        output = (
            f"{result['root_cause']}\n\n"
            f"{result['remediation']}\n\n"
            f"{result['pagerduty_alert']}"
        )
        if state["cross_reference"]:
            output = f"{state['cross_reference']}\n\n{output}"
        print_route_output("escalation", output)
        return IncidentState(
            incident=state["incident"],
            incident_id=state["incident_id"],
            severity=state["severity"],
            service=state["service"],
            error=state["error"],
            affected_users=state["affected_users"],
            region=state["region"],
            route=state["route"],
            incident_history=[],
            cross_reference=state["cross_reference"],
            response_plan=state["response_plan"],
            log_message=state["log_message"],
            escalation_output=output,
            notification=state["notification"],
            roster_index=state["roster_index"],
        )

    return escalation_invoke_node


# make_response_node - create the HIGH-severity response plan node
def make_response_node(service: LLMService):
    """Create the HIGH-severity response plan node."""

    def response_node(state: IncidentState) -> IncidentState:
        cross_ref = state["cross_reference"]
        extra = f"\n{cross_ref}" if cross_ref else ""
        response_plan = service.chat(
            [
                {"role": "system", "content": RESPONSE_SYSTEM},
                {
                    "role": "user",
                    "content": RESPONSE_USER.format(
                        incident_id=state["incident_id"],
                        service=state["service"],
                        error=state["error"],
                        affected_users=state["affected_users"],
                        cross_reference=extra,
                    ),
                },
            ],
            temperature=0.2,
        ).strip()
        if cross_ref:
            response_plan = f"{cross_ref}\n\n{response_plan}"
        print_route_output("response", response_plan)
        return IncidentState(
            incident=state["incident"],
            incident_id=state["incident_id"],
            severity=state["severity"],
            service=state["service"],
            error=state["error"],
            affected_users=state["affected_users"],
            region=state["region"],
            route=state["route"],
            incident_history=[],
            cross_reference=state["cross_reference"],
            response_plan=response_plan,
            log_message=state["log_message"],
            escalation_output=state["escalation_output"],
            notification=state["notification"],
            roster_index=state["roster_index"],
        )

    return response_node


# make_log_node - create the MEDIUM/LOW watch-list log node
def make_log_node():
    """Create the MEDIUM/LOW watch-list log node."""

    def log_node(state: IncidentState) -> IncidentState:
        message = format_log_message(state["incident"])
        if state["cross_reference"]:
            message = f"{state['cross_reference']}\n{message}"
        print_route_output("log", message)
        return IncidentState(
            incident=state["incident"],
            incident_id=state["incident_id"],
            severity=state["severity"],
            service=state["service"],
            error=state["error"],
            affected_users=state["affected_users"],
            region=state["region"],
            route=state["route"],
            incident_history=[],
            cross_reference=state["cross_reference"],
            response_plan=state["response_plan"],
            log_message=message,
            escalation_output=state["escalation_output"],
            notification=state["notification"],
            roster_index=state["roster_index"],
        )

    return log_node


# make_notification_node - create the final two-sentence notification node
def make_notification_node(service: LLMService):
    """Create the final two-sentence notification node."""

    def notification_node(state: IncidentState) -> IncidentState:
        if state["route"] == "critical":
            action_details = state["escalation_output"]
        elif state["route"] == "high":
            action_details = state["response_plan"]
        else:
            action_details = state["log_message"]

        cross_ref = state["cross_reference"]
        extra = f"\n{cross_ref}" if cross_ref else ""
        notification = service.chat(
            [
                {"role": "system", "content": NOTIFICATION_SYSTEM},
                {
                    "role": "user",
                    "content": NOTIFICATION_USER.format(
                        incident_id=state["incident_id"],
                        severity=state["severity"],
                        route=state["route"],
                        action_details=action_details,
                        cross_reference=extra,
                    ),
                },
            ],
            temperature=0.2,
        ).strip()
        print_notification(notification)
        return IncidentState(
            incident=state["incident"],
            incident_id=state["incident_id"],
            severity=state["severity"],
            service=state["service"],
            error=state["error"],
            affected_users=state["affected_users"],
            region=state["region"],
            route=state["route"],
            incident_history=[],
            cross_reference=state["cross_reference"],
            response_plan=state["response_plan"],
            log_message=state["log_message"],
            escalation_output=state["escalation_output"],
            notification=notification,
            roster_index=state["roster_index"],
        )

    return notification_node
