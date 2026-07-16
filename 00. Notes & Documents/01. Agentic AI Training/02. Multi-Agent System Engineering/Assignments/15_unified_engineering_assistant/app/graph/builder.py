"""Build and compile the unified assistant supervisor graph."""

from __future__ import annotations

from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import END, START, StateGraph

from app.graph.nodes import (
    make_db_worker_node,
    make_finish_node,
    make_memory_worker_node,
    make_rag_worker_node,
    make_supervisor_node,
)
from app.graph.state import AssistantState
from app.services.llm_service import LLMService
from app.services.mcp_client import MCPClientWrapper


# route_after_supervisor - map supervisor route tokens to graph node names
def route_after_supervisor(state: AssistantState) -> str:
    if state["route"] == "FINISH":
        return "finish"
    return state["route"]


# build_graph - compile the supervisor graph with MemorySaver checkpointer
def build_graph(
    service: LLMService | None = None,
    mcp_client: MCPClientWrapper | None = None,
    *,
    checkpointer: MemorySaver | None = None,
):
    llm = service or LLMService()
    mcp = mcp_client or MCPClientWrapper()

    builder = StateGraph(AssistantState)
    builder.add_node("supervisor", make_supervisor_node(llm))
    builder.add_node("rag", make_rag_worker_node(llm, mcp))
    builder.add_node("db", make_db_worker_node(mcp))
    builder.add_node("memory", make_memory_worker_node(mcp))
    builder.add_node("finish", make_finish_node())

    builder.add_edge(START, "supervisor")
    builder.add_conditional_edges(
        "supervisor",
        route_after_supervisor,
        {
            "rag": "rag",
            "db": "db",
            "memory": "memory",
            "finish": "finish",
        },
    )
    for worker in ("rag", "db", "memory", "finish"):
        builder.add_edge(worker, END)

    memory = checkpointer or MemorySaver()
    return builder.compile(checkpointer=memory)
