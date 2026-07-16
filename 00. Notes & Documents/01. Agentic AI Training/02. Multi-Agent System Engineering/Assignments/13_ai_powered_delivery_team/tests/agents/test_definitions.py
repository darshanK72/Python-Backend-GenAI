"""Tests for agent prompt definitions."""

from app.schemas.agent_prompts import AGENT_MESSAGES, ROLE_AGENT_NAMES, SCOPE_RULE


# test_all_role_agents_have_distinct_system_messages - test five role messages are unique
def test_all_role_agents_have_distinct_system_messages() -> None:
    messages = [AGENT_MESSAGES[name] for name in ROLE_AGENT_NAMES]
    assert len(messages) == len(set(messages))


# test_each_system_message_requires_name_references - test collaboration rule is present
def test_each_system_message_requires_name_references() -> None:
    for name in ROLE_AGENT_NAMES:
        assert "reference their name explicitly" in AGENT_MESSAGES[name]


# test_each_role_message_requires_kickoff_feature_scope - test agents must not swap features
def test_each_role_message_requires_kickoff_feature_scope() -> None:
    for name in ROLE_AGENT_NAMES:
        assert SCOPE_RULE in AGENT_MESSAGES[name]
        assert "Design ONLY the feature described in the kickoff" in AGENT_MESSAGES[name]


# test_devops_message_requires_deployment_complete_token - test DevOps termination token
def test_devops_message_requires_deployment_complete_token() -> None:
    devops = AGENT_MESSAGES["DevOps"]
    assert "DEPLOYMENT_COMPLETE" in devops
    assert "Task Notifications v1.0 deployed to staging" in devops
