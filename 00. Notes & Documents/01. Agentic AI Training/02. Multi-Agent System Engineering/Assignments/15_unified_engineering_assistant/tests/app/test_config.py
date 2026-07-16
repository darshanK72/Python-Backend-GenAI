"""Tests for configuration."""

from app.config import (
    DEMO_QUERIES,
    ENV_FILE,
    HELP_TEXT,
    MCP_SERVER_URL,
    PROJECT_ROOT,
    THREAD_ID,
    Settings,
    get_settings,
    load_env_file,
)


# test_project_root_points_at_assignment_folder - test that PROJECT_ROOT points at the assignment folder
def test_project_root_points_at_assignment_folder() -> None:
    assert PROJECT_ROOT.name == "15_unified_engineering_assistant"
    assert (PROJECT_ROOT / "engineering_assistant.py").is_file()
    assert (PROJECT_ROOT / "mcp_server.py").is_file()


# test_env_file_lives_in_project_root - test that ENV_FILE points at the assignment .env file
def test_env_file_lives_in_project_root() -> None:
    assert ENV_FILE == PROJECT_ROOT / ".env"
    assert (PROJECT_ROOT / ".env.example").is_file()


# test_demo_queries_and_thread_match_assignment_spec - test demo session constants
def test_demo_queries_and_thread_match_assignment_spec() -> None:
    assert THREAD_ID == "capstone-session-01"
    assert MCP_SERVER_URL == "http://127.0.0.1:8000/mcp"
    assert len(DEMO_QUERIES) == 4
    assert "microservices" in DEMO_QUERIES[0].lower()
    assert "blocked" in DEMO_QUERIES[1].lower()
    assert "so far" in DEMO_QUERIES[2].lower()
    assert "devops" in DEMO_QUERIES[3].lower()


# test_help_text_documents_cli_and_mcp - test HELP_TEXT documents setup and CLI
def test_help_text_documents_cli_and_mcp() -> None:
    assert "mcp_server.py" in HELP_TEXT
    assert "engineering_assistant.py" in HELP_TEXT
    assert "demo" in HELP_TEXT
    assert "rebuild_index.py" in HELP_TEXT


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
    assert settings.mcp_server_url == MCP_SERVER_URL


# test_get_settings_is_cached - test that get_settings returns the same cached instance
def test_get_settings_is_cached() -> None:
    get_settings.cache_clear()
    first = get_settings()
    second = get_settings()
    assert first is second
