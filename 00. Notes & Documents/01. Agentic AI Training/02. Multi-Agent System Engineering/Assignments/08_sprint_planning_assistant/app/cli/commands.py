"""CLI command handlers."""

from __future__ import annotations

import sys

from app.cli.output import print_session_start
from app.graph.builder import build_graph
from app.graph.state import SprintState, initial_state
from app.services.llm_service import LLMService
from app.services.mcp_client import MCPClientWrapper

# DEMO_REQUESTS - evaluator sample requests for the demo command
DEMO_REQUESTS = [
    "Plan OAuth login for the admin dashboard",
    "Check capacity",
    "Any risks in the current sprint?",
    "Add tasks for CSV export on the backlog page",
    "Done",
]


# run_session - execute the supervisor LangGraph for a list of requests
def run_session(
    requests: list[str],
    *,
    service: LLMService | None = None,
    mcp_client: MCPClientWrapper | None = None,
) -> SprintState:
    """Run the sprint planning session and return the final graph state."""
    llm = service or LLMService()
    mcp = mcp_client or MCPClientWrapper()
    graph = build_graph(llm, mcp)
    print_session_start()
    return graph.invoke(initial_state(requests))


# cmd_request - route a single request and return an exit code
def cmd_request(
    request: str,
    *,
    service: LLMService | None = None,
    mcp_client: MCPClientWrapper | None = None,
) -> int:
    """Route one sprint planning request and return an exit code."""
    try:
        run_session([request], service=service, mcp_client=mcp_client)
    except RuntimeError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1
    return 0


# cmd_demo - run all evaluator sample requests and return an exit code
def cmd_demo(
    *,
    service: LLMService | None = None,
    mcp_client: MCPClientWrapper | None = None,
) -> int:
    """Run all demo requests and return an exit code."""
    try:
        run_session(DEMO_REQUESTS, service=service, mcp_client=mcp_client)
    except RuntimeError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1
    return 0
