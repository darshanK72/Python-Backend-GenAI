"""CLI command handlers."""

from __future__ import annotations

import sys
from pathlib import Path

from app.cli.output import print_history, print_incident_header
from app.config import DATA_DIR, INCIDENT_FILES, THREAD_ID
from app.graph.main_graph.builder import build_graph
from app.graph.main_graph.state import incident_input
from app.services.incident_loader import load_incident
from app.services.llm_service import LLMService


# thread_config - build LangGraph config with the shift MemorySaver thread id
def thread_config(thread_id: str = THREAD_ID) -> dict:
    """Build LangGraph config with the shift MemorySaver thread id."""
    return {"configurable": {"thread_id": thread_id}}


# resolve_incident_path - resolve a CLI path, falling back to data/
def resolve_incident_path(raw: str) -> Path:
    """Resolve an incident path; try data/<name> when the given path is missing."""
    path = Path(raw)
    if path.is_file():
        return path
    candidate = DATA_DIR / path.name
    if candidate.is_file():
        return candidate
    return path


# run_incident - execute the nested graph for one incident JSON file
def run_incident(
    incident_path: Path,
    *,
    service: LLMService | None = None,
    graph=None,
    thread_id: str = THREAD_ID,
) -> dict:
    """Run the incident handler pipeline and return the final graph state."""
    llm = service or LLMService()
    app = graph or build_graph(llm)
    incident = load_incident(incident_path)
    config = thread_config(thread_id)
    print_incident_header(incident["incident_id"], thread_id)
    result = app.invoke(incident_input(incident), config=config)
    snapshot = app.get_state(config)
    history = snapshot.values.get("incident_history", result.get("incident_history", []))
    print_history(history)
    return result


# cmd_incident - handle one incident file and return an exit code
def cmd_incident(
    incident_path: Path,
    *,
    service: LLMService | None = None,
    graph=None,
    thread_id: str = THREAD_ID,
) -> int:
    """Handle one incident file and return an exit code."""
    if not incident_path.is_file():
        print(f"Error: incident file not found: {incident_path}", file=sys.stderr)
        return 1
    try:
        run_incident(incident_path, service=service, graph=graph, thread_id=thread_id)
    except (RuntimeError, ValueError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1
    return 0


# cmd_demo - run all three sample incidents on one shift thread
def cmd_demo(*, service: LLMService | None = None) -> int:
    """Run all three sample incidents on one shift thread."""
    try:
        graph = build_graph(service) if service is not None else build_graph()
        for path in INCIDENT_FILES:
            code = cmd_incident(path, service=service, graph=graph)
            if code != 0:
                return code
    except (RuntimeError, ValueError, FileNotFoundError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1
    return 0
