"""Build one-line incident summaries and cross-reference notes."""

from __future__ import annotations


# build_history_line - format one incident as a MemorySaver history line
def build_history_line(incident: dict) -> str:
    """Format one incident as a MemorySaver history line."""
    return (
        f"{incident['incident_id']} | {incident['severity']} | "
        f"{incident['service']} | {incident['error']}"
    )


# parse_history_line - parse a history line back into named fields
def parse_history_line(line: str) -> dict[str, str]:
    """Parse a history line back into named fields."""
    parts = [part.strip() for part in line.split("|")]
    if len(parts) != 4:
        return {}
    return {
        "incident_id": parts[0],
        "severity": parts[1],
        "service": parts[2],
        "error": parts[3],
    }


# build_cross_reference - note prior same-service incidents from shift history
def build_cross_reference(
    service: str,
    incident_id: str,
    history: list[str],
) -> str:
    """Note prior same-service incidents from shift history."""
    prior_same_service = []
    for line in history:
        parsed = parse_history_line(line)
        if parsed.get("service") == service and parsed.get("incident_id") != incident_id:
            prior_same_service.append(parsed)

    if not prior_same_service:
        return ""

    first = prior_same_service[0]
    ordinal = "second" if len(prior_same_service) == 1 else f"{len(prior_same_service) + 1}th"
    return (
        f"Note: This is the {ordinal} {service} incident this shift. "
        f"{first['incident_id']} involved {first['error']} ? check if root cause is related."
    )


# format_log_message - build the MEDIUM/LOW watch-list acknowledgement string
def format_log_message(incident: dict) -> str:
    """Build the MEDIUM/LOW watch-list acknowledgement string."""
    return (
        f"{incident['incident_id']} logged for monitoring. No immediate action required. "
        f"Added to watch list: {incident['service']} {incident['error'].lower()}."
    )
