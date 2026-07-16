"""Tests for configuration."""

from app.cli.commands import DEMO_QUERIES
from app.config import (
    DATA_DIR,
    DB_PATH,
    ENV_FILE,
    FAILURE_MESSAGE,
    HELP_TEXT,
    MAX_RETRIES,
    PROJECT_ROOT,
    Settings,
    get_settings,
    load_env_file,
)


# test_project_root_points_at_assignment_folder - test that PROJECT_ROOT points at the assignment folder
def test_project_root_points_at_assignment_folder() -> None:
    assert PROJECT_ROOT.name == "10_data_analytics_query_agent"
    assert (PROJECT_ROOT / "analytics_query.py").is_file()


# test_env_file_lives_in_project_root - test that ENV_FILE points at the assignment .env file
def test_env_file_lives_in_project_root() -> None:
    assert ENV_FILE == PROJECT_ROOT / ".env"
    assert (PROJECT_ROOT / ".env.example").is_file()


# test_database_paths_point_at_data_folder - test DB_PATH lives under DATA_DIR
def test_database_paths_point_at_data_folder() -> None:
    assert DATA_DIR == PROJECT_ROOT / "data"
    assert DB_PATH == DATA_DIR / "analytics.db"


# test_max_retries_matches_assignment_spec - test that MAX_RETRIES is two
def test_max_retries_matches_assignment_spec() -> None:
    assert MAX_RETRIES == 2
    assert "2 attempts" in FAILURE_MESSAGE


# test_demo_queries_match_assignment_spec - test that demo queries cover four evaluator types
def test_demo_queries_match_assignment_spec() -> None:
    assert len(DEMO_QUERIES) == 4
    assert "blocked" in DEMO_QUERIES[0]
    assert "average story points" in DEMO_QUERIES[3].lower()


# test_help_text_documents_cli_usage - test that HELP_TEXT documents ask, demo, and seed
def test_help_text_documents_cli_usage() -> None:
    assert "analytics_query.py" in HELP_TEXT
    assert "demo" in HELP_TEXT
    assert "seed_db.py" in HELP_TEXT


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
