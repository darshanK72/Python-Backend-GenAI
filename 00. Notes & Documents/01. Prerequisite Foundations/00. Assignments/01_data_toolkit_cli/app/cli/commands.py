"""CLI command handlers."""

from __future__ import annotations

from app.services.analytics import assignee_load, count_by_status, filter_by_tag, total_points


def cmd_summary(tasks: list[dict]) -> None:
    """Print status counts and overall point totals."""
    counts = count_by_status(tasks)
    print("Task summary")
    print("-" * 32)
    for status, count in counts.items():
        print(f"  {status:12} {count:3}")
    print("-" * 32)
    print(f"  {'total points':12} {total_points(tasks):3}")
    open_points = (
        total_points(tasks, status="todo")
        + total_points(tasks, status="in_progress")
        + total_points(tasks, status="blocked")
    )
    print(f"  {'open points':12} {open_points:3}")


def cmd_points(tasks: list[dict], status: str | None) -> None:
    """Print summed story points."""
    if status is None:
        print(f"Total story points: {total_points(tasks)}")
        return
    print(f"Story points ({status}): {total_points(tasks, status=status)}")


def cmd_load(tasks: list[dict], assignee: str | None) -> None:
    """Print open story points per assignee."""
    loads = assignee_load(tasks)
    if assignee is None:
        print("Open story points by assignee")
        print("-" * 32)
        for name, points in loads.items():
            print(f"  {name:12} {points:3}")
        return

    points = loads.get(assignee, 0)
    print(f"Open story points for {assignee}: {points}")


def cmd_tag(tasks: list[dict], tag: str) -> None:
    """Print tasks that match the given tag."""
    matches = filter_by_tag(tasks, tag)
    if not matches:
        print(f"No tasks found for tag '{tag}'.")
        return

    print(f"Tasks tagged '{tag}' ({len(matches)})")
    print("-" * 48)
    for task in matches:
        print(f"  #{task['id']:2} [{task['status']}] {task['title']} ({task['assignee']})")
