"""Build and compile the writer LangGraph."""

from __future__ import annotations

from typing import Any

from langgraph.graph import END, START, StateGraph

from app.config import get_settings
from app.graph.nodes import make_delegation_node, make_discovery_node, make_writer_node
from app.graph.state import WriterState
from app.services.llm_service import LLMService


# build_graph - compile discovery → delegation → writer StateGraph
def build_graph(
    service: LLMService | None = None,
    *,
    base_url: str | None = None,
    http_client: Any | None = None,
):
    """Compile discovery → delegation → writer StateGraph."""
    settings = get_settings()
    llm = service or LLMService(settings)
    research_url = base_url or settings.research_agent_url

    builder = StateGraph(WriterState)
    builder.add_node("discovery", make_discovery_node(research_url, http_client))
    builder.add_node("delegation", make_delegation_node(research_url, http_client))
    builder.add_node("writer", make_writer_node(llm))

    builder.add_edge(START, "discovery")
    builder.add_edge("discovery", "delegation")
    builder.add_edge("delegation", "writer")
    builder.add_edge("writer", END)
    return builder.compile()
