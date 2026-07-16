"""Tests for configuration."""

from app.config import (
    DEFAULT_REPORTS_FILE,
    ENV_FILE,
    PROJECT_ROOT,
    REPORT_CATEGORY_FILES,
    Settings,
    get_settings,
    load_env_file,
)
from app.services.report_loader import load_reports


# test_project_root_points_at_assignment_folder - test that PROJECT_ROOT points at the assignment folder
def test_project_root_points_at_assignment_folder() -> None:
    assert PROJECT_ROOT.name == "04_prompt_engineering_toolkit"
    assert (PROJECT_ROOT / "prompt_toolkit.py").is_file()


# test_env_file_lives_in_project_root - test that ENV_FILE points at the assignment .env file
def test_env_file_lives_in_project_root() -> None:
    assert ENV_FILE == PROJECT_ROOT / ".env"
    assert (PROJECT_ROOT / ".env.example").is_file()


# test_default_reports_file_points_at_data_fixture - test that DEFAULT_REPORTS_FILE points at reports.json
def test_default_reports_file_points_at_data_fixture() -> None:
    assert DEFAULT_REPORTS_FILE == PROJECT_ROOT / "data" / "reports.json"
    assert DEFAULT_REPORTS_FILE.is_file()


# test_report_category_files_exist - test that each category report file exists and has five reports
def test_report_category_files_exist() -> None:
    assert set(REPORT_CATEGORY_FILES) == {
        "auth",
        "performance",
        "notifications",
        "settings",
        "feature_requests",
    }
    for path in REPORT_CATEGORY_FILES.values():
        assert path.is_file()
        assert len(load_reports(path)) >= 5


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
    assert settings.extraction_temperature == 0.0


# test_get_settings_is_cached - test that get_settings returns the same cached instance
def test_get_settings_is_cached() -> None:
    get_settings.cache_clear()
    first = get_settings()
    second = get_settings()
    assert first is second
