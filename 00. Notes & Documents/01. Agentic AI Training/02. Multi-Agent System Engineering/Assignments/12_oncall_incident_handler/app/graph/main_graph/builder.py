"""Build and compile the main incident handler graph with MemorySaver."""

from __future__ import annotations

from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import END, START, StateGraph

from app.graph.escalation_graph.escalation_builder import build_escalation_graph
from app.graph.main_graph.nodes import (
    make_classifier_node,
    make_escalation_invoke_node,
    make_log_node,
    make_notification_node,
    make_response_node,
)
from app.graph.main_graph.state import IncidentState
from app.services.llm_service import LLMService


# route_after_classifier - route CRITICAL / HIGH / MEDIUM-LOW after classification
def route_after_classifier(state: IncidentState) -> str:
    """Route CRITICAL / HIGH / MEDIUM-LOW after classification."""
    if state["route"] == "critical":
        return "escalation"
    if state["route"] == "high":
        return "response"
    return "log"


# build_graph - compile the main graph with MemorySaver checkpointer
def build_graph(
    service: LLMService | None = None,
    *,
    checkpointer: MemorySaver | None = None,
):
    """Compile the main graph with MemorySaver checkpointer."""
    llm = service or LLMService()
    escalation_graph = build_escalation_graph(llm)

    builder = StateGraph(IncidentState)
    builder.add_node("classifier", make_classifier_node())
    builder.add_node("escalation", make_escalation_invoke_node(escalation_graph))
    builder.add_node("response", make_response_node(llm))
    builder.add_node("log", make_log_node())
    builder.add_node("notification", make_notification_node(llm))

    builder.add_edge(START, "classifier")
    builder.add_conditional_edges(
        "classifier",
        route_after_classifier,
        {
            "escalation": "escalation",
            "response": "response",
            "log": "log",
        },
    )
    builder.add_edge("escalation", "notification")
    builder.add_edge("response", "notification")
    builder.add_edge("log", "notification")
    builder.add_edge("notification", END)

    memory = checkpointer or MemorySaver()
    return builder.compile(checkpointer=memory)
