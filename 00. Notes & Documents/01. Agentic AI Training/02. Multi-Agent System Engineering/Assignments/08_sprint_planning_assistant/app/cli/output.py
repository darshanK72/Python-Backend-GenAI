"""Console output for supervisor routing."""

from __future__ import annotations

from typing import Any

# _RULE - horizontal rule used between requests in a session
_RULE = "─" * 60


# print_session_start - print the sprint planning session header
def print_session_start() -> None:
    """Print the sprint planning session header."""
    print(f"\n{'=' * 60}")
    print("  Sprint planning session")
    print(f"{'=' * 60}\n")


# print_request - print the current user request
def print_request(request: str, *, index: int | None = None) -> None:
    """Print the current user request."""
    if index is not None and index > 0:
        print(_RULE)
    if index is not None:
        print(f"\nRequest {index + 1}: {request}")
    else:
        print(f"\nRequest: {request}")


# print_supervisor_route - print the supervisor routing decision
def print_supervisor_route(route: str) -> None:
    """Print the supervisor routing decision."""
    print(f"[supervisor] route -> {route}")


# print_finish - print when the supervisor ends the session
def print_finish() -> None:
    """Print when the supervisor ends the session."""
    print("\n[supervisor] route -> FINISH")
    print("Session complete.\n")


# print_mcp_call - print an indented MCP tool call and result
def print_mcp_call(name: str, arguments: dict[str, Any], result: str) -> None:
    """Print an indented MCP tool call and result."""
    args_text = ", ".join(f"{key}={value!r}" for key, value in arguments.items())
    print(f"  MCP: {name}({args_text})")
    for line in result.splitlines():
        print(f"       {line}")


# print_sprint_builder_header - print the sprint builder section header
def print_sprint_builder_header(feature: str) -> None:
    """Print the sprint builder section header."""
    print("\n[sprint_builder]")
    print(f"  Feature: {feature}\n")


# print_sprint_builder_tasks - print the numbered task list
def print_sprint_builder_tasks(tasks: list[dict[str, Any]]) -> None:
    """Print the numbered task list."""
    print(f"  Tasks created ({len(tasks)}):")
    for index, task in enumerate(tasks, start=1):
        print(
            f"    {index}. {task['title']} — "
            f"{task['story_points']} SP ({task['assignee']})"
        )
    print()


# print_sprint_builder_result - print a formatted sprint builder summary
def print_sprint_builder_result(feature: str, tasks: list[dict[str, Any]]) -> None:
    """Print a formatted sprint builder summary."""
    print_sprint_builder_header(feature)
    print_sprint_builder_tasks(tasks)


# print_capacity_result - print capacity status and recommendation
def print_capacity_result(
    capacity: str,
    recommendation: str,
    *,
    include_header: bool = True,
) -> None:
    """Print capacity status and recommendation."""
    if include_header:
        print("\n[capacity_checker]")
    print(f"  Capacity: {capacity.rstrip('.')}")
    print(f"  Recommendation: {recommendation}")
    print()


# print_risk_header - print the risk assessor section header
def print_risk_header() -> None:
    """Print the risk assessor section header."""
    print("\n[risk_assessor]")
    print("  Risks identified:")


# print_risk_result - print formatted risk assessor output
def print_risk_result(result: str, *, include_header: bool = True) -> None:
    """Print formatted risk assessor output."""
    if include_header:
        print_risk_header()
    else:
        print("  Risks identified:")
    for line in result.splitlines():
        cleaned = line.strip()
        if not cleaned:
            continue
        if cleaned[0].isdigit() and "." in cleaned[:4]:
            print(f"    {cleaned}")
        else:
            print(f"    - {cleaned}")
    print()


# print_worker_result - print a generic worker result block
def print_worker_result(worker: str, result: str) -> None:
    """Print a generic worker result block."""
    print(f"\n[{worker}]")
    for line in result.splitlines():
        print(f"  {line}")
    print()
