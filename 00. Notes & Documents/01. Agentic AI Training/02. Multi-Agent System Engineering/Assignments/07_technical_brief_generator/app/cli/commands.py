"""CLI command handlers."""

from __future__ import annotations

import sys

from app.cli.output import print_topic
from app.graph.builder import build_graph
from app.graph.state import BriefState, initial_state
from app.services.llm_service import LLMService

# DEMO_TOPICS - evaluator sample topics for the demo command
DEMO_TOPICS = [
    "Event-driven architecture",
    "GraphQL vs REST APIs",
]


# run_brief - execute the brief generator LangGraph for a single topic
def run_brief(topic: str, *, service: LLMService | None = None) -> BriefState:
    """Run the technical brief pipeline and return the final graph state."""
    llm = service or LLMService()
    graph = build_graph(llm)
    print_topic(topic)
    return graph.invoke(initial_state(topic))


# cmd_topic - generate a brief for one topic and return an exit code
def cmd_topic(topic: str, *, service: LLMService | None = None) -> int:
    """Generate a brief for one topic and return an exit code."""
    try:
        run_brief(topic, service=service)
    except RuntimeError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1
    return 0


# cmd_demo - run all evaluator sample topics and return an exit code
def cmd_demo(*, service: LLMService | None = None) -> int:
    """Run all demo topics and return an exit code."""
    for index, topic in enumerate(DEMO_TOPICS, start=1):
        print(f"=== Demo topic {index}/{len(DEMO_TOPICS)} ===")
        try:
            run_brief(topic, service=service)
        except RuntimeError as exc:
            print(f"Error: {exc}", file=sys.stderr)
            return 1
    return 0
