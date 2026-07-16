"""Tests for configuration."""

from app.config import (
    DATA_DIR,
    ENV_FILE,
    HELP_TEXT,
    INCIDENT_FILES,
    ONCALL_ROSTER,
    PROJECT_ROOT,
    Settings,
    THREAD_ID,
    get_settings,
    load_env_file,
)


# test_project_root_points_at_assignment_folder - test that PROJECT_ROOT points at the assignment folder
def test_project_root_points_at_assignment_folder() -> None:
    assert PROJECT_ROOT.name == "12_oncall_incident_handler"
    assert (PROJECT_ROOT / "incident_handler.py").is_file()


# test_env_file_lives_in_project_root - test that ENV_FILE points at the assignment .env file
def test_env_file_lives_in_project_root() -> None:
    assert ENV_FILE == PROJECT_ROOT / ".env"
    assert (PROJECT_ROOT / ".env.example").is_file()


# test_incident_files_live_under_data_dir - test sample incidents live under data/
def test_incident_files_live_under_data_dir() -> None:
    assert DATA_DIR == PROJECT_ROOT / "data"
    assert INCIDENT_FILES == [
        DATA_DIR / "incident_01.json",
        DATA_DIR / "incident_02.json",
        DATA_DIR / "incident_03.json",
    ]
    for path in INCIDENT_FILES:
        assert path.is_file()


# test_thread_id_and_roster_match_assignment_spec - test MemorySaver thread and roster
def test_thread_id_and_roster_match_assignment_spec() -> None:
    assert THREAD_ID == "shift-2024-11-15"
    assert ONCALL_ROSTER == ["Alice Chen", "Bob Kumar", "Carol Smith"]


# test_help_text_documents_cli_usage - test that HELP_TEXT documents incident and demo
def test_help_text_documents_cli_usage() -> None:
    assert "incident_handler.py" in HELP_TEXT
    assert "demo" in HELP_TEXT
    assert "data/incident_01.json" in HELP_TEXT


# test_load_env_file_loads_project_dotenv - test that load_env_file reads from the assignment .env file
def test_load_env_file_loads_project_dotenv(tmp_path, monkeypatch) -> None:
    monkeypatch.setattr("app.config.ENV_FILE", tmp_path / ".env")
    (tmp_path / ".env").write_text("OPENAI_API_KEY=from-project-env\n", encoding="utf-8")
    monkeypatch.setenv("OPENAI_API_KEY", "placeholder")
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
