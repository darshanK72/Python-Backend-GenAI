"""Tests for configuration."""

from app.config import (
    DEFAULT_SAMPLE_DOC,
    ENV_FILE,
    HELP_TEXT,
    MAX_TOOL_CALLS,
    PROJECT_ROOT,
    Settings,
    get_settings,
    load_env_file,
)


# test_project_root_points_at_assignment_folder - test that PROJECT_ROOT points at the assignment folder
def test_project_root_points_at_assignment_folder() -> None:
    assert PROJECT_ROOT.name == "06_developer_assist_agent"
    assert (PROJECT_ROOT / "developer_assist.py").is_file()


# test_env_file_lives_in_project_root - test that ENV_FILE points at the assignment .env file
def test_env_file_lives_in_project_root() -> None:
    assert ENV_FILE == PROJECT_ROOT / ".env"
    assert (PROJECT_ROOT / ".env.example").is_file()


# test_default_sample_doc_points_at_data_fixture - test that DEFAULT_SAMPLE_DOC points at the sample doc
def test_default_sample_doc_points_at_data_fixture() -> None:
    assert DEFAULT_SAMPLE_DOC == PROJECT_ROOT / "data" / "sample_langgraph_readme.txt"
    assert DEFAULT_SAMPLE_DOC.is_file()


# test_max_tool_calls_matches_assignment_spec - test that MAX_TOOL_CALLS is six
def test_max_tool_calls_matches_assignment_spec() -> None:
    assert MAX_TOOL_CALLS == 6


# test_help_text_documents_cli_usage - test that HELP_TEXT documents ask and demo commands
def test_help_text_documents_cli_usage() -> None:
    assert "developer_assist.py" in HELP_TEXT
    assert "demo" in HELP_TEXT


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


# test_get_settings_is_cached - test that get_settings returns the same cached instance
def test_get_settings_is_cached() -> None:
    get_settings.cache_clear()
    first = get_settings()
    second = get_settings()
    assert first is second
