"""Tests for configuration."""

from app.cli.commands import DEMO_REQUESTS
from app.config import (
    DEFAULT_VELOCITY,
    ENV_FILE,
    HELP_TEXT,
    MCP_SERVER_PORT,
    MCP_SERVER_SCRIPT,
    MCP_SERVER_URL,
    PROJECT_ROOT,
    Settings,
    get_settings,
    load_env_file,
)


# test_project_root_points_at_assignment_folder - test that PROJECT_ROOT points at the assignment folder
def test_project_root_points_at_assignment_folder() -> None:
    assert PROJECT_ROOT.name == "08_sprint_planning_assistant"
    assert (PROJECT_ROOT / "sprint_planner.py").is_file()


# test_env_file_lives_in_project_root - test that ENV_FILE points at the assignment .env file
def test_env_file_lives_in_project_root() -> None:
    assert ENV_FILE == PROJECT_ROOT / ".env"
    assert (PROJECT_ROOT / ".env.example").is_file()


# test_mcp_server_script_points_at_project_file - test that MCP_SERVER_SCRIPT points at mcp_server.py
def test_mcp_server_script_points_at_project_file() -> None:
    assert MCP_SERVER_SCRIPT == PROJECT_ROOT / "mcp_server.py"
    assert MCP_SERVER_SCRIPT.is_file()


# test_mcp_server_url_points_at_local_http_endpoint - test default MCP HTTP URL
def test_mcp_server_url_points_at_local_http_endpoint() -> None:
    assert MCP_SERVER_URL == f"http://127.0.0.1:{MCP_SERVER_PORT}/mcp"


# test_default_velocity_matches_assignment_spec - test that DEFAULT_VELOCITY is forty
def test_default_velocity_matches_assignment_spec() -> None:
    assert DEFAULT_VELOCITY == 40


# test_demo_requests_match_assignment_spec - test that demo requests match the evaluator list
def test_demo_requests_match_assignment_spec() -> None:
    assert len(DEMO_REQUESTS) == 5
    assert DEMO_REQUESTS[0] == "Plan OAuth login for the admin dashboard"
    assert DEMO_REQUESTS[-1] == "Done"


# test_help_text_documents_cli_usage - test that HELP_TEXT documents request and demo commands
def test_help_text_documents_cli_usage() -> None:
    assert "sprint_planner.py" in HELP_TEXT
    assert "demo" in HELP_TEXT
    assert "mcp_server.py" in HELP_TEXT


# test_load_env_file_loads_project_dotenv - test that load_env_file reads from the assignment .env file
def test_load_env_file_loads_project_dotenv(tmp_path, monkeypatch) -> None:
    monkeypatch.setattr("app.config.ENV_FILE", tmp_path / ".env")
    (tmp_path / ".env").write_text("OPENAI_API_KEY=from-project-env\n", encoding="utf-8")
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)

    load_env_file()
    settings = Settings()

    assert settings.openai_api_key == "from-project-env"


# test_settings_defaults - test that Settings provides expected default values
def test_settings_defaults() -> None:
    settings = Settings.model_construct()
    assert settings.openai_model == "gpt-4o-mini"
    assert settings.llm_temperature == 0.0
    assert settings.mcp_server_url == MCP_SERVER_URL


# test_get_settings_is_cached - test that get_settings returns the same cached instance
def test_get_settings_is_cached() -> None:
    get_settings.cache_clear()
    first = get_settings()
    second = get_settings()
    assert first is second
