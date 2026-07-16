"""Console output for plan-and-execute traces."""

from __future__ import annotations

import json

from app.graph.state import PlanStep, ReviewResult


# print_request - print the feature request header
def print_request(request: str) -> None:
    """Print the feature request header."""
    print(f"\n{'=' * 60}")
    print("  Feature Scoping Agent")
    print(f"{'=' * 60}")
    print(f"\nFeature request: {request}\n")


# print_plan - print the planner JSON delivery plan
def print_plan(plan: list[PlanStep]) -> None:
    """Print the planner JSON delivery plan."""
    print("[planner] delivery plan:")
    print(json.dumps(plan, indent=2))
    print()


# print_execution_step - print one executor log entry
def print_execution_step(entry: str) -> None:
    """Print one executor log entry."""
    print(f"[executor] {entry}\n")


# print_review - print the reviewer assessment fields
def print_review(review: ReviewResult) -> None:
    """Print the reviewer assessment fields."""
    print("[reviewer] assessment:")
    print(f"  coverage_score: {review['coverage_score']}")
    print("  gaps:")
    if review["gaps"]:
        for gap in review["gaps"]:
            print(f"    - {gap}")
    else:
        print("    - (none)")
    print(f"  recommendation: {review['recommendation']}\n")
