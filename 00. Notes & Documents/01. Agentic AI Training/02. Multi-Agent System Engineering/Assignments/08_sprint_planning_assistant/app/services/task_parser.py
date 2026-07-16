"""Parse sprint builder JSON."""

from __future__ import annotations

import json


# parse_task_plan - parse sprint builder JSON with 3-5 tasks
def parse_task_plan(text: str) -> dict:
    """Parse sprint builder JSON with 3-5 tasks."""
    stripped = text.strip()
    if stripped.startswith("```"):
        stripped = stripped.strip("`")
        if stripped.startswith("json"):
            stripped = stripped[4:].strip()
    payload = json.loads(stripped)
    tasks = payload.get("tasks", [])
    if not 3 <= len(tasks) <= 5:
        raise ValueError("Sprint builder must return 3-5 tasks.")
    return payload
