"""CLI command handlers."""

from __future__ import annotations

import sys

from app.cli.output import print_request
from app.graph.builder import build_graph
from app.graph.state import ScopeState, initial_state
from app.services.llm_service import LLMService

# FEATURE_A - evaluator sample feature for email notifications on blocked status
FEATURE_A = "Add email notifications when a task's status changes to blocked"

# FEATURE_B - evaluator sample feature for backlog CSV export with filters
FEATURE_B = "Build a CSV export for the project backlog with filters by status and assignee"

# DEMO_FEATURES - both evaluator sample features for the demo command
DEMO_FEATURES = [FEATURE_A, FEATURE_B]


# run_scope - execute the plan-and-execute graph for a single feature request
def run_scope(
    request: str,
    *,
    service: LLMService | None = None,
) -> ScopeState:
    """Run the feature scoping pipeline and return the final graph state."""
    llm = service or LLMService()
    graph = build_graph(llm)
    print_request(request)
    return graph.invoke(initial_state(request))


# cmd_scope - scope one feature request and return an exit code
def cmd_scope(
    request: str,
    *,
    service: LLMService | None = None,
) -> int:
    """Scope one feature request and return an exit code."""
    try:
        run_scope(request, service=service)
    except RuntimeError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1
    return 0


# cmd_demo - run both evaluator sample features and return an exit code
def cmd_demo(*, service: LLMService | None = None) -> int:
    """Run both demo features and return an exit code."""
    for index, request in enumerate(DEMO_FEATURES, start=1):
        print(f"=== Demo feature {index}/{len(DEMO_FEATURES)} ===")
        try:
            run_scope(request, service=service)
        except RuntimeError as exc:
            print(f"Error: {exc}", file=sys.stderr)
            return 1
    return 0
