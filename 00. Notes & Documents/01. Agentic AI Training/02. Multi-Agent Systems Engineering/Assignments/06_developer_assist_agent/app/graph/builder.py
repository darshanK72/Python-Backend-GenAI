"""Build and compile the developer assist LangGraph."""

from __future__ import annotations

from langgraph.graph import END, START, StateGraph

from app.graph.nodes import make_act_node, make_finalize_node, make_reason_node
from app.graph.state import AgentState
from app.services.llm_service import LLMService


def route_after_reason(state: AgentState) -> str:
    """Route to END when the agent produced a Final Answer."""
    if state["final_answer"]:
        return "end"
    if state["pending_action"]:
        return "act"
    return "finalize"


def route_after_act(state: AgentState) -> str:
    """Always return to the reason node for the next Thought cycle."""
    return "reason"


def build_graph(service: LLMService | None = None):
    """Compile the ReAct StateGraph."""
    llm = service or LLMService()
    builder = StateGraph(AgentState)
    builder.add_node("reason", make_reason_node(llm))
    builder.add_node("act", make_act_node(llm))
    builder.add_node("finalize", make_finalize_node(llm))

    builder.add_edge(START, "reason")
    # Route to act when the reason node selected a tool, END when it produced a Final Answer,
    # or finalize when parsing failed without a usable action.
    builder.add_conditional_edges(
        "reason",
        route_after_reason,
        {
            "act": "act",
            "end": END,
            "finalize": "finalize",
        },
    )
    # After each tool observation, return to reason for the next Thought cycle.
    builder.add_conditional_edges(
        "act",
        route_after_act,
        {
            "reason": "reason",
        },
    )
    builder.add_edge("finalize", END)
    return builder.compile()
