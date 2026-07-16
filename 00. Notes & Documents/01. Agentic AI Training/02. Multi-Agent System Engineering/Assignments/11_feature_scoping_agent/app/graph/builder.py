"""Build and compile the feature scoping LangGraph."""

from __future__ import annotations

from langgraph.graph import END, START, StateGraph

from app.graph.nodes import make_executor_node, make_planner_node, make_reviewer_node
from app.graph.state import ScopeState
from app.services.llm_service import LLMService


# route_after_executor - continue the loop or move to reviewer when the plan is done
def route_after_executor(state: ScopeState) -> str:
    """Route back to executor while steps remain, otherwise to reviewer."""
    if state["current_step_idx"] < len(state["plan"]):
        return "executor"
    return "reviewer"


# build_graph - compile the planner → executor loop → reviewer StateGraph
def build_graph(service: LLMService | None = None):
    """Compile the plan-and-execute StateGraph."""
    llm = service or LLMService()
    builder = StateGraph(ScopeState)
    builder.add_node("planner", make_planner_node(llm))
    builder.add_node("executor", make_executor_node(llm))
    builder.add_node("reviewer", make_reviewer_node(llm))

    builder.add_edge(START, "planner")
    builder.add_edge("planner", "executor")
    builder.add_conditional_edges(
        "executor",
        route_after_executor,
        {
            "executor": "executor",
            "reviewer": "reviewer",
        },
    )
    builder.add_edge("reviewer", END)
    return builder.compile()
