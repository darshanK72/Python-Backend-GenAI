"""Build and compile the supervisor LangGraph."""

from __future__ import annotations

from langgraph.graph import END, START, StateGraph

from app.graph.nodes import (
    make_capacity_checker_node,
    make_risk_assessor_node,
    make_sprint_builder_node,
    make_supervisor_node,
)
from app.graph.state import SprintState
from app.services.llm_service import LLMService
from app.services.mcp_client import MCPClientWrapper


# route_after_supervisor - route to a worker or END when FINISH is selected
def route_after_supervisor(state: SprintState) -> str:
    """Route to a worker, or END when the supervisor selects FINISH."""
    if state["route"] == "FINISH" or state["finished"]:
        return "end"
    return state["route"]


# route_after_worker - return to supervisor for the next request or END when done
def route_after_worker(state: SprintState) -> str:
    """Return to the supervisor for the next request."""
    if state["finished"] or state["request_index"] >= len(state["requests"]):
        return "end"
    return "supervisor"


# build_graph - compile the supervisor StateGraph with three worker nodes
def build_graph(
    service: LLMService | None = None,
    mcp_client: MCPClientWrapper | None = None,
):
    """Compile the supervisor StateGraph with three worker nodes."""
    llm = service or LLMService()
    mcp = mcp_client or MCPClientWrapper()

    builder = StateGraph(SprintState)
    builder.add_node("supervisor", make_supervisor_node(llm))
    builder.add_node("sprint_builder", make_sprint_builder_node(llm, mcp))
    builder.add_node("capacity_checker", make_capacity_checker_node(mcp))
    builder.add_node("risk_assessor", make_risk_assessor_node(llm, mcp))

    builder.add_edge(START, "supervisor")
    builder.add_conditional_edges(
        "supervisor",
        route_after_supervisor,
        {
            "sprint_builder": "sprint_builder",
            "capacity_checker": "capacity_checker",
            "risk_assessor": "risk_assessor",
            "end": END,
        },
    )
    for worker in ("sprint_builder", "capacity_checker", "risk_assessor"):
        builder.add_conditional_edges(
            worker,
            route_after_worker,
            {
                "supervisor": "supervisor",
                "end": END,
            },
        )

    return builder.compile()
