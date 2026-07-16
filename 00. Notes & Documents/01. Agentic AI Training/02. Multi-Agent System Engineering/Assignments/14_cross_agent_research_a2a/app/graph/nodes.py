"""Writer agent LangGraph nodes."""

from __future__ import annotations

from typing import Any

from app.cli.output import print_delegation, print_discovery
from app.graph.state import WriterState
from app.schemas.prompts import WRITER_SYSTEM, WRITER_USER
from app.services.a2a_client import delegate_task, discover_agent
from app.services.llm_service import LLMService


# make_discovery_node - create the AgentCard discovery node
def make_discovery_node(
    base_url: str,
    client: Any | None = None,
):
    """Create the AgentCard discovery node."""

    def discovery_node(state: WriterState) -> WriterState:
        card = discover_agent(base_url, client=client)
        print_discovery(card)
        return WriterState(
            topic=state["topic"],
            agent_card=card,
            task_id=state["task_id"],
            research_result=state["research_result"],
            article=state["article"],
        )

    return discovery_node


# make_delegation_node - create the A2A /tasks/send delegation node
def make_delegation_node(
    base_url: str,
    client: Any | None = None,
):
    """Create the A2A /tasks/send delegation node."""

    def delegation_node(state: WriterState) -> WriterState:
        task_id, output = delegate_task(
            state["topic"],
            base_url=base_url,
            client=client,
        )
        print_delegation(task_id, len(output))
        return WriterState(
            topic=state["topic"],
            agent_card=state["agent_card"],
            task_id=task_id,
            research_result=output,
            article=state["article"],
        )

    return delegation_node


# make_writer_node - create the OpenAI brief-writing node
def make_writer_node(service: LLMService):
    """Create the OpenAI brief-writing node."""

    def writer_node(state: WriterState) -> WriterState:
        article = service.chat(
            [
                {"role": "system", "content": WRITER_SYSTEM},
                {
                    "role": "user",
                    "content": WRITER_USER.format(
                        topic=state["topic"],
                        research=state["research_result"],
                    ),
                },
            ],
            temperature=0.3,
        ).strip()
        return WriterState(
            topic=state["topic"],
            agent_card=state["agent_card"],
            task_id=state["task_id"],
            research_result=state["research_result"],
            article=article,
        )

    return writer_node
