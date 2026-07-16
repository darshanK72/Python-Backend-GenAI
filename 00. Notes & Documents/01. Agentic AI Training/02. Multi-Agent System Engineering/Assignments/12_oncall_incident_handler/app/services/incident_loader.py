"""Load incident JSON files."""

from __future__ import annotations

import json
from pathlib import Path

# REQUIRED_INCIDENT_FIELDS - fields every sample incident JSON must include
REQUIRED_INCIDENT_FIELDS = (
    "incident_id",
    "severity",
    "service",
    "error",
    "affected_users",
    "region",
)


# load_incident - load and validate one incident JSON file
def load_incident(path: Path) -> dict:
    """Load and validate one incident JSON file."""
    payload = json.loads(path.read_text(encoding="utf-8"))
    missing = [field for field in REQUIRED_INCIDENT_FIELDS if field not in payload]
    if missing:
        raise ValueError(f"Incident file missing fields: {', '.join(missing)}")
    return payload
