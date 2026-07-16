"""Build the escalation sub-graph as a separate StateGraph."""

from __future__ import annotations

from langgraph.graph import END, START, StateGraph

from app.graph.escalation_graph.escalation_nodes import (
    make_pagerduty_node,
    make_remediation_node,
    make_root_cause_node,
)
from app.graph.escalation_graph.escalation_state import EscalationState
from app.services.llm_service import LLMService


# build_escalation_graph - compile the CRITICAL escalation sub-graph separately
def build_escalation_graph(service: LLMService | None = None):
    """Compile the CRITICAL escalation sub-graph separately."""
    llm = service or LLMService()
    builder = StateGraph(EscalationState)
    builder.add_node("root_cause", make_root_cause_node(llm))
    builder.add_node("remediation", make_remediation_node(llm))
    builder.add_node("pagerduty", make_pagerduty_node())

    builder.add_edge(START, "root_cause")
    builder.add_edge("root_cause", "remediation")
    builder.add_edge("remediation", "pagerduty")
    builder.add_edge("pagerduty", END)
    return builder.compile()
