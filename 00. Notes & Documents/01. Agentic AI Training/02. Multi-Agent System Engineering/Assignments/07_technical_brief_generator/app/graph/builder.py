"""Build and compile the technical brief LangGraph."""

from __future__ import annotations

from langgraph.graph import END, START, StateGraph

from app.cli.output import print_gate_decision
from app.config import MAX_RETRIES, MIN_CLAIMS
from app.graph.nodes import make_analyst_node, make_researcher_node, make_writer_node
from app.graph.state import BriefState
from app.services.llm_service import LLMService


# route_after_analyst - quality gate: route to writer or back to researcher
def route_after_analyst(state: BriefState) -> str:
    """Route to writer when enough claims exist, else retry research up to the limit."""
    if state["claim_count"] >= MIN_CLAIMS:
        destination = "writer"
    elif state["retry_count"] < MAX_RETRIES:
        destination = "researcher"
    else:
        destination = "writer"
    print_gate_decision(destination, state)
    return destination


# build_graph - compile the sequential brief StateGraph with quality gate
def build_graph(service: LLMService | None = None):
    """Compile the sequential brief StateGraph with quality gate."""
    llm = service or LLMService()
    builder = StateGraph(BriefState)
    builder.add_node("researcher", make_researcher_node(llm))
    builder.add_node("analyst", make_analyst_node(llm))
    builder.add_node("writer", make_writer_node(llm))

    builder.add_edge(START, "researcher")
    builder.add_edge("researcher", "analyst")
    builder.add_conditional_edges(
        "analyst",
        route_after_analyst,
        {
            "researcher": "researcher",
            "writer": "writer",
        },
    )
    builder.add_edge("writer", END)
    return builder.compile()
