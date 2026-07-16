"""CLI command handlers."""

from __future__ import annotations

import sys

from app.cli.output import print_query, print_session_history
from app.config import DEMO_QUERIES, THREAD_ID
from app.graph.builder import build_graph
from app.graph.state import query_input
from app.services.llm_service import LLMService
from app.services.mcp_client import MCPClientWrapper
from app.services.session_store import clear_store


# thread_config - build LangGraph config with the capstone MemorySaver thread id
def thread_config(thread_id: str = THREAD_ID) -> dict:
    """Build LangGraph config with the capstone MemorySaver thread id."""
    return {"configurable": {"thread_id": thread_id}}


# run_query - execute supervisor routing for one question on a shared thread
def run_query(
    question: str,
    *,
    service: LLMService | None = None,
    mcp_client: MCPClientWrapper | None = None,
    graph=None,
    thread_id: str = THREAD_ID,
    turn: int | None = None,
    config: dict | None = None,
):
    """Run one query through the supervisor graph and return final state."""
    llm = service or LLMService()
    mcp = mcp_client or MCPClientWrapper()
    app = graph or build_graph(llm, mcp)
    cfg = config or thread_config(thread_id)
    if turn is None:
        snapshot = app.get_state(cfg)
        turn = len(snapshot.values.get("session_history", [])) + 1
    print_query(question, thread_id)
    result = app.invoke(query_input(question, thread_id, turn), config=cfg)
    snapshot = app.get_state(cfg)
    history = snapshot.values.get("session_history", result.get("session_history", []))
    print_session_history(history)
    return result


# cmd_ask - ask one question and return an exit code
def cmd_ask(
    question: str,
    *,
    service: LLMService | None = None,
    mcp_client: MCPClientWrapper | None = None,
) -> int:
    """Ask one question and return an exit code."""
    try:
        run_query(question, service=service, mcp_client=mcp_client)
    except (RuntimeError, FileNotFoundError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1
    return 0


# cmd_demo - run the four evaluator queries on one thread and return an exit code
def cmd_demo(
    *,
    service: LLMService | None = None,
    mcp_client: MCPClientWrapper | None = None,
) -> int:
    """Run the four evaluator queries on one thread and return an exit code."""
    clear_store()
    llm = service or LLMService()
    mcp = mcp_client or MCPClientWrapper()
    try:
        graph = build_graph(llm, mcp)
        config = thread_config(THREAD_ID)
        for question in DEMO_QUERIES:
            run_query(
                question,
                service=llm,
                mcp_client=mcp,
                graph=graph,
                thread_id=THREAD_ID,
                config=config,
            )
    except (RuntimeError, FileNotFoundError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1
    return 0
