"""Console output for pipeline transitions."""

from __future__ import annotations

from app.graph.state import BriefState


# print_topic - print the topic header
def print_topic(topic: str) -> None:
    """Print the topic header."""
    print(f"\nTopic: {topic}\n")


# print_transition - print claim_count and retry_count when a node runs
def print_transition(node: str, state: BriefState) -> None:
    """Print claim_count and retry_count when a node runs."""
    print(
        f"[{node}] claim_count={state['claim_count']}, "
        f"retry_count={state['retry_count']}"
    )


# print_facts - print the numbered fact list from the researcher
def print_facts(facts: list[str]) -> None:
    """Print the numbered fact list from the researcher."""
    print("Facts:")
    for index, fact in enumerate(facts, start=1):
        print(f"  {index}. {fact}")
    print()


# print_gate_decision - print the quality gate routing decision
def print_gate_decision(destination: str, state: BriefState) -> None:
    """Print the quality gate routing decision."""
    print(
        f"[gate] claim_count={state['claim_count']}, "
        f"retry_count={state['retry_count']} -> {destination}\n"
    )


# print_article - print the final brief article
def print_article(article: str) -> None:
    """Print the final brief article."""
    print(article)
    print()
