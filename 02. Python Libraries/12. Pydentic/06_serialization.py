# 06 — Serialization and parsing (dict, JSON)
# Run: python 06_serialization.py

import json

from pydantic import BaseModel, Field


class Event(BaseModel):
    id: int
    name: str
    attendees: list[str] = Field(default_factory=list)


event = Event(id=1, name="Python Meetup", attendees=["Ada", "Grace"])

# --- 1. model_dump() — Python dict ---
data = event.model_dump()
print("dict:", data)

# --- 2. model_dump_json() — JSON string ---
json_str = event.model_dump_json(indent=2)
print("json:\n", json_str)

# --- 3. Parse dict / JSON back into a model ---
restored = Event.model_validate(json.loads(json_str))
print("restored name:", restored.name)

# --- 4. Exclude / include fields ---
public = event.model_dump(exclude={"id"})
print("public view:", public)

# --- 5. mode="json" converts types JSON cannot represent natively ---
from datetime import datetime


class LogEntry(BaseModel):
    message: str
    created_at: datetime


entry = LogEntry(message="server started", created_at=datetime(2026, 7, 3, 10, 30))
print("json mode:", entry.model_dump(mode="json"))
