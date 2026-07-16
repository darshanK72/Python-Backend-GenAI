"""AgentCard builder for the ResearchAgent."""

from __future__ import annotations

from app.config import RESEARCH_AGENT_URL


# build_agent_card - return the A2A AgentCard JSON for ResearchAgent
def build_agent_card() -> dict:
    """Return the A2A AgentCard JSON for ResearchAgent."""
    return {
        "name": "ResearchAgent",
        "version": "1.0",
        "description": "Researches engineering topics and returns structured facts and trends.",
        "url": RESEARCH_AGENT_URL,
        "skills": [
            {
                "name": "research",
                "description": "Research a technical topic and return structured findings.",
                "inputSchema": {
                    "type": "object",
                    "properties": {"topic": {"type": "string"}},
                },
                "outputSchema": {
                    "type": "object",
                    "properties": {"output": {"type": "string"}},
                },
            }
        ],
    }
