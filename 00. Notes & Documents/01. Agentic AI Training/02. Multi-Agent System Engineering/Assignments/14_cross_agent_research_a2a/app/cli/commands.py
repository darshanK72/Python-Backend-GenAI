"""CLI command handlers for the WriterAgent."""

from __future__ import annotations

import sys

import httpx

from app.cli.output import print_article, print_topic
from app.config import DEMO_TOPICS
from app.graph.builder import build_graph
from app.graph.state import initial_state


# run_brief - invoke discovery → delegation → writer for one topic
def run_brief(topic: str, *, graph=None) -> dict:
    """Run the writer LangGraph for one topic and return final state."""
    print_topic(topic)
    app = graph or build_graph()
    return app.invoke(initial_state(topic))


# cmd_topic - write a brief for one topic and return an exit code
def cmd_topic(topic: str, *, graph=None) -> int:
    """Write a brief for one topic and return an exit code."""
    try:
        result = run_brief(topic, graph=graph)
        print_article(result["article"])
    except (RuntimeError, httpx.HTTPError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1
    return 0


# cmd_demo - run both evaluator sample topics and return an exit code
def cmd_demo(*, graph=None) -> int:
    """Run both demo topics and return an exit code."""
    compiled = graph or build_graph()
    for topic in DEMO_TOPICS:
        print(f"=== Demo topic: {topic} ===")
        try:
            result = run_brief(topic, graph=compiled)
            print_article(result["article"])
        except (RuntimeError, httpx.HTTPError) as exc:
            print(f"Error: {exc}", file=sys.stderr)
            return 1
    return 0
