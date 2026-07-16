"""Console output for incident handling traces."""

from __future__ import annotations


# print_incident_header - print the incident and thread banner
def print_incident_header(incident_id: str, thread_id: str) -> None:
    """Print the incident and thread banner."""
    print(f"\n{'=' * 60}")
    print("  On-Call Incident Handler")
    print(f"{'=' * 60}")
    print(f"\n=== Handling {incident_id} (thread: {thread_id}) ===\n")


# print_classifier - print severity classification and route
def print_classifier(incident: dict, route: str) -> None:
    """Print severity classification and route."""
    print(
        f"[classifier] {incident['incident_id']} | {incident['severity']} | "
        f"{incident['service']} -> route: {route}"
    )


# print_cross_reference - print a same-service memory cross-reference note
def print_cross_reference(note: str) -> None:
    """Print a same-service memory cross-reference note."""
    print(f"[memory] {note}")


# print_history - print accumulated incident_history for the shift thread
def print_history(history: list[str]) -> None:
    """Print accumulated incident_history for the shift thread."""
    print("[memory] incident_history:")
    for line in history:
        print(f"  - {line}")
    print()


# print_route_output - print main-graph route content (response / log / escalation)
def print_route_output(route: str, content: str) -> None:
    """Print main-graph route content (response / log / escalation)."""
    print(f"[{route}] {content}\n")


# print_escalation_section - print an escalation sub-graph section
def print_escalation_section(section: str, content: str) -> None:
    """Print an escalation sub-graph section."""
    print(f"[escalation:{section}] {content}\n")


# print_notification - print the final two-sentence notification summary
def print_notification(content: str) -> None:
    """Print the final two-sentence notification summary."""
    print(f"[notification] {content}\n")
