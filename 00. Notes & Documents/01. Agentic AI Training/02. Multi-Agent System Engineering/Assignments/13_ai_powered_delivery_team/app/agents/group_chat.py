"""AutoGen group chat runner using SelectorGroupChat (auto speaker selection)."""

from __future__ import annotations

from autogen_agentchat.base import TaskResult
from autogen_agentchat.conditions import TextMentionTermination
from autogen_agentchat.teams import SelectorGroupChat
from autogen_ext.models.openai import OpenAIChatCompletionClient

from app.agents.definitions import create_role_agents
from app.config import MAX_ROUNDS, TERMINATION_TOKEN


# run_group_chat - run the five role agents until DEPLOYMENT_COMPLETE or max turns
async def run_group_chat(
    feature_request: str,
    model_client: OpenAIChatCompletionClient,
) -> TaskResult:
    """Run the five role agents in a SelectorGroupChat team.

    SelectorGroupChat uses a GroupChatManager-style selector model to pick the
    next speaker automatically (equivalent to speaker_selection_method='auto').
    """
    agents = create_role_agents(model_client)
    termination = TextMentionTermination(TERMINATION_TOKEN)
    team = SelectorGroupChat(
        agents,
        model_client=model_client,
        termination_condition=termination,
        max_turns=MAX_ROUNDS,
    )
    return await team.run(task=feature_request)
