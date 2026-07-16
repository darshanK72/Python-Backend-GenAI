"""Console output for routing traces."""

from __future__ import annotations

from typing import Any

from app.graph.state import SessionEntry


# print_query - print the question and thread banner
def print_query(query: str, thread_id: str) -> None:
    """Print the question and thread banner."""
    print(f"\n{'=' * 60}")
    print("  Unified Engineering Assistant")
    print(f"{'=' * 60}")
    print(f"\nQuery ({thread_id}): {query}\n")


# print_route - print the supervisor route decision
def print_route(route: str, query: str) -> None:
    """Print the supervisor route decision."""
    print(f"[supervisor] route={route} for: {query}\n")


# print_mcp_call - print an indented MCP tool call summary
def print_mcp_call(name: str, arguments: dict[str, Any], result: str) -> None:
    """Print an indented MCP tool call summary."""
    preview = result.replace("\n", " ")[:120]
    print(f"  MCP call: {name}({arguments})")
    print(f"    -> {preview}...\n")


# print_answer - print the worker answer
def print_answer(answer: str) -> None:
    """Print the worker answer."""
    print(f"Answer: {answer}\n")


# print_session_history - print accumulated session history for the thread
def print_session_history(history: list[SessionEntry]) -> None:
    """Print accumulated session history for the thread."""
    print("[session] history:")
    if not history:
        print("  (empty)")
    else:
        for entry in history:
            print(
                f"  Turn {entry['turn']}: [{entry['worker']}] "
                f"{entry['query']} -> {entry['summary'][:80]}"
            )
    print()
