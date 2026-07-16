"""FastMCP server for sprint backlog tools."""

from __future__ import annotations

from fastmcp import FastMCP

mcp = FastMCP("sprint-backlog")

# BACKLOG - in-memory sprint task store shared by all MCP tools
BACKLOG: list[dict] = [
    {
        "title": "DB migration",
        "assignee": "",
        "story_points": 8,
        "status": "todo",
        "risk_level": "high",
    },
    {
        "title": "Auth token refresh",
        "assignee": "Sam",
        "story_points": 5,
        "status": "in_progress",
        "risk_level": "medium",
    },
    {
        "title": "Dashboard filters",
        "assignee": "Alex",
        "story_points": 3,
        "status": "todo",
        "risk_level": "low",
    },
]


# _open_points - sum story points for all non-done tasks
def _open_points() -> int:
    return sum(task["story_points"] for task in BACKLOG if task["status"] != "done")


# get_backlog - return all sprint tasks with story points and status
@mcp.tool
def get_backlog() -> str:
    """Return all sprint tasks with story points and status."""
    if not BACKLOG:
        return "Backlog is empty."
    lines = []
    for index, task in enumerate(BACKLOG, start=1):
        lines.append(
            f"{index}. {task['title']} — {task['story_points']} SP, "
            f"status={task['status']}, assignee={task['assignee'] or 'unassigned'}, "
            f"risk={task['risk_level']}"
        )
    return "\n".join(lines)


# add_task - add a new todo task to the backlog
@mcp.tool
def add_task(title: str, assignee: str, story_points: int) -> str:
    """Add a new todo task to the backlog."""
    BACKLOG.append(
        {
            "title": title,
            "assignee": assignee,
            "story_points": story_points,
            "status": "todo",
            "risk_level": "low",
        }
    )
    return f"Task added: {title} ({story_points} SP, assigned to {assignee})"


# check_capacity - compare open story points against sprint velocity
@mcp.tool
def check_capacity(velocity: int = 40) -> str:
    """Sum open story points against sprint velocity."""
    total = _open_points()
    if total > velocity:
        delta = total - velocity
        return f"Sprint is at {total}/{velocity} SP. Over capacity by {delta} SP."
    if total < velocity:
        delta = velocity - total
        return f"Sprint is at {total}/{velocity} SP. Under capacity by {delta} SP."
    return f"Sprint is at {total}/{velocity} SP. Under capacity by 0 SP."


# get_risk_summary - return medium and high risk tasks
@mcp.tool
def get_risk_summary() -> str:
    """Return medium and high risk tasks."""
    risky = [task for task in BACKLOG if task["risk_level"] in {"high", "medium"}]
    if not risky:
        return "No medium or high risk tasks in the backlog."
    lines = []
    for index, task in enumerate(risky, start=1):
        lines.append(
            f"{index}. {task['title']} — {task['story_points']} SP, "
            f"status={task['status']}, risk={task['risk_level']}"
        )
    return "\n".join(lines)


# main - run the MCP server over HTTP for the sprint planner client
if __name__ == "__main__":
    mcp.run(transport="streamable-http", host="127.0.0.1", port=8000)
