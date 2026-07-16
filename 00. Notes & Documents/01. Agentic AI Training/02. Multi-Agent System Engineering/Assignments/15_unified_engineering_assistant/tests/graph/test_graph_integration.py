"""Integration tests for supervisor routing and memory."""

from __future__ import annotations

from unittest.mock import MagicMock

from app.cli.commands import thread_config
from app.config import DEMO_QUERIES, THREAD_ID
from app.graph.builder import build_graph
from app.graph.state import query_input
from app.services.llm_service import LLMService
from app.services.mcp_client import MCPClientWrapper
from app.services.session_store import clear_store, format_history


# test_four_query_session_routes_and_recalls_history - test the evaluator 4-query session
def test_four_query_session_routes_and_recalls_history(
    test_settings,
    session_store_file,
) -> None:
    clear_store(session_store_file)

    # tool_handler - in-memory MCP double for the three capstone tools
    def tool_handler(name: str, arguments: dict) -> str:
        if name == "rag_search":
            return "Result 1 (Source: Microservices): Independent deployable services."
        if name == "db_query":
            return "Fix session timeout and Add retry policy are blocked."
        if name == "get_session_history":
            return format_history(arguments["thread_id"])
        raise ValueError(name)

    client = MagicMock()
    client.chat.completions.create.side_effect = [
        _response("Microservices deploy independently while monoliths ship as one unit."),
        _response("Apply CI/CD automation and monitoring for blocked task recovery."),
    ]
    llm = LLMService(settings=test_settings, client=client)
    mcp = MCPClientWrapper(tool_handler=tool_handler)
    graph = build_graph(llm, mcp)
    config = thread_config(THREAD_ID)

    routes = []
    for question in DEMO_QUERIES:
        result = graph.invoke(query_input(question, THREAD_ID, 0), config=config)
        routes.append(result["route"])

    snapshot = graph.get_state(config)
    history = snapshot.values["session_history"]
    memory_result = graph.invoke(
        query_input(DEMO_QUERIES[2], THREAD_ID, 0),
        config=config,
    )

    assert routes[0] == "rag"
    assert routes[1] == "db"
    assert routes[2] == "memory"
    assert routes[3] == "rag"
    assert len(history) >= 3
    assert (
        "microservices" in memory_result["worker_result"].lower()
        or "Turn 1" in memory_result["worker_result"]
    )


# _response - build a minimal OpenAI-like chat completion mock
def _response(content: str) -> MagicMock:
    return MagicMock(choices=[MagicMock(message=MagicMock(content=content))])
