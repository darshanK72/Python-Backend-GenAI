"""Console output for A2A writer traces."""

from __future__ import annotations


# print_topic - print the research topic header
def print_topic(topic: str) -> None:
    """Print the research topic header."""
    print(f"\n{'=' * 60}")
    print("  Cross-Agent Research (A2A)")
    print(f"{'=' * 60}")
    print(f"\nTopic: {topic}\n")


# print_discovery - print AgentCard discovery details
def print_discovery(card: dict) -> None:
    """Print AgentCard discovery details."""
    skills = ", ".join(skill["name"] for skill in card.get("skills", []))
    print(
        f"Agent discovered: {card['name']} v{card['version']} — Skills: {skills}\n"
    )


# print_delegation - print A2A task completion summary
def print_delegation(task_id: str, char_count: int) -> None:
    """Print A2A task completion summary."""
    print(f"A2A task {task_id} completed. Research received ({char_count} characters).\n")


# print_article - print the generated engineering brief
def print_article(article: str) -> None:
    """Print the generated engineering brief."""
    print(f"Article:\n{article}\n")
