"""Tests for configuration."""

from app.config import (
    ENV_FILE,
    FEATURE_REQUEST,
    HELP_TEXT,
    MAX_ROUNDS,
    PROJECT_ROOT,
    REPORT_PATH,
    REPORT_SECTIONS,
    Settings,
    TERMINATION_TOKEN,
    TRANSCRIPT_PATH,
    get_settings,
    load_env_file,
)


# test_project_root_points_at_assignment_folder - test that PROJECT_ROOT points at the assignment folder
def test_project_root_points_at_assignment_folder() -> None:
    assert PROJECT_ROOT.name == "13_ai_powered_delivery_team"
    assert (PROJECT_ROOT / "delivery_team.py").is_file()


# test_env_file_lives_in_project_root - test that ENV_FILE points at the assignment .env file
def test_env_file_lives_in_project_root() -> None:
    assert ENV_FILE == PROJECT_ROOT / ".env"
    assert (PROJECT_ROOT / ".env.example").is_file()


# test_artifact_paths_live_in_project_root - test transcript and report paths
def test_artifact_paths_live_in_project_root() -> None:
    assert TRANSCRIPT_PATH == PROJECT_ROOT / "transcript.txt"
    assert REPORT_PATH == PROJECT_ROOT / "delivery_report.md"


# test_group_chat_settings_match_assignment_spec - test max rounds and termination token
def test_group_chat_settings_match_assignment_spec() -> None:
    assert MAX_ROUNDS == 15
    assert TERMINATION_TOKEN == "DEPLOYMENT_COMPLETE"
    assert "real-time task status notifications" in FEATURE_REQUEST
    assert len(REPORT_SECTIONS) == 5


# test_help_text_documents_cli_usage - test that HELP_TEXT documents run, custom feature, and --save
def test_help_text_documents_cli_usage() -> None:
    assert "delivery_team.py" in HELP_TEXT
    assert "--save" in HELP_TEXT
    assert "<feature request>" in HELP_TEXT


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
    assert settings.llm_temperature == 0.0


# test_get_settings_is_cached - test that get_settings returns the same cached instance
def test_get_settings_is_cached() -> None:
    get_settings.cache_clear()
    first = get_settings()
    second = get_settings()
    assert first is second
