"""Tests for configuration."""

from app.config import (
    DEMO_TOPICS,
    ENV_FILE,
    HELP_TEXT,
    PROJECT_ROOT,
    RESEARCH_AGENT_PORT,
    RESEARCH_AGENT_URL,
    Settings,
    WRITER_AGENT_PORT,
    get_settings,
    load_env_file,
)


# test_project_root_points_at_assignment_folder - test that PROJECT_ROOT points at the assignment folder
def test_project_root_points_at_assignment_folder() -> None:
    assert PROJECT_ROOT.name == "14_cross_agent_research_a2a"
    assert (PROJECT_ROOT / "research_agent.py").is_file()
    assert (PROJECT_ROOT / "writer_agent.py").is_file()


# test_env_file_lives_in_project_root - test that ENV_FILE points at the assignment .env file
def test_env_file_lives_in_project_root() -> None:
    assert ENV_FILE == PROJECT_ROOT / ".env"
    assert (PROJECT_ROOT / ".env.example").is_file()


# test_ports_and_demo_topics_match_assignment_spec - test ports and demo topics
def test_ports_and_demo_topics_match_assignment_spec() -> None:
    assert RESEARCH_AGENT_PORT == 8001
    assert WRITER_AGENT_PORT == 8002
    assert RESEARCH_AGENT_URL == "http://localhost:8001"
    assert DEMO_TOPICS == [
        "Event-driven architecture",
        "Observability in microservices",
    ]


# test_help_text_documents_cli_and_services - test HELP_TEXT documents both services
def test_help_text_documents_cli_and_services() -> None:
    assert "research_agent" in HELP_TEXT
    assert "writer_agent.py" in HELP_TEXT
    assert "demo" in HELP_TEXT
    assert "8001" in HELP_TEXT


# test_load_env_file_loads_project_dotenv - test that load_env_file reads from the assignment .env file
def test_load_env_file_loads_project_dotenv(tmp_path, monkeypatch) -> None:
    monkeypatch.setattr("app.config.ENV_FILE", tmp_path / ".env")
    (tmp_path / ".env").write_text("OPENAI_API_KEY=from-project-env\n", encoding="utf-8")
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)

    load_env_file()
    settings = Settings()

    assert settings.openai_api_key == "from-project-env"
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)


# test_settings_defaults - test that Settings provides expected default values
def test_settings_defaults() -> None:
    settings = Settings.model_construct()
    assert settings.openai_model == "gpt-4o-mini"
    assert settings.research_agent_url == RESEARCH_AGENT_URL


# test_get_settings_is_cached - test that get_settings returns the same cached instance
def test_get_settings_is_cached() -> None:
    get_settings.cache_clear()
    first = get_settings()
    second = get_settings()
    assert first is second
