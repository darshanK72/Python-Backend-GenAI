"""Create AutoGen agents for the delivery team."""

from __future__ import annotations

from autogen_agentchat.agents import AssistantAgent
from autogen_ext.models.openai import OpenAIChatCompletionClient

from app.schemas.agent_prompts import (
    AGENT_DESCRIPTIONS,
    AGENT_MESSAGES,
    DOCUMENTATION_WRITER_MESSAGE,
    ROLE_AGENT_NAMES,
)


# create_model_client - build an OpenAI chat completion client for AutoGen agents
def create_model_client(api_key: str, model: str) -> OpenAIChatCompletionClient:
    """Build an OpenAI chat completion client for AutoGen agents."""
    return OpenAIChatCompletionClient(model=model, api_key=api_key)


# create_role_agents - create the five group-chat role agents
def create_role_agents(model_client: OpenAIChatCompletionClient) -> list[AssistantAgent]:
    """Create the five group-chat role agents."""
    agents: list[AssistantAgent] = []
    for name in ROLE_AGENT_NAMES:
        agents.append(
            AssistantAgent(
                name=name,
                model_client=model_client,
                system_message=AGENT_MESSAGES[name],
                description=AGENT_DESCRIPTIONS[name],
            )
        )
    return agents


# create_documentation_writer - create the post-chat DocumentationWriter agent
def create_documentation_writer(
    model_client: OpenAIChatCompletionClient,
) -> AssistantAgent:
    """Create the post-chat DocumentationWriter agent."""
    return AssistantAgent(
        name="DocumentationWriter",
        model_client=model_client,
        system_message=DOCUMENTATION_WRITER_MESSAGE,
        description="Writes the post-chat delivery report from the transcript.",
    )
