"""Build and compile the developer assist LangGraph."""

from __future__ import annotations

from langgraph.graph import END, START, StateGraph

from app.graph.nodes import make_act_node, make_finalize_node, make_reason_node
from app.graph.state import AgentState
from app.services.llm_service import LLMService


# route_after_reason - route to END, act, or finalize after the reason node
def route_after_reason(state: AgentState) -> str:
    """Route to END when the agent produced a Final Answer."""
    if state["final_answer"]:
        return "end"
    if state["pending_action"]:
        return "act"
    return "finalize"


# route_after_act - always return to the reason node for the next Thought cycle
def route_after_act(state: AgentState) -> str:
    """Always return to the reason node for the next Thought cycle."""
    return "reason"


# build_graph - compile the ReAct StateGraph
def build_graph(service: LLMService | None = None):
    """Compile the ReAct StateGraph."""
    llm = service or LLMService()
    builder = StateGraph(AgentState)
    builder.add_node("reason", make_reason_node(llm))
    builder.add_node("act", make_act_node(llm))
    builder.add_node("finalize", make_finalize_node(llm))

    builder.add_edge(START, "reason")
    builder.add_conditional_edges(
        "reason",
        route_after_reason,
        {
            "act": "act",
            "end": END,
            "finalize": "finalize",
        },
    )
    builder.add_conditional_edges(
        "act",
        route_after_act,
        {
            "reason": "reason",
        },
    )
    builder.add_edge("finalize", END)
    return builder.compile()
