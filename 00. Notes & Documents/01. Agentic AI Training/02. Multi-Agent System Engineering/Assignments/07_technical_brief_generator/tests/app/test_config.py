"""Tests for configuration."""

from app.cli.commands import DEMO_TOPICS
from app.config import (
    ENV_FILE,
    HELP_TEXT,
    MAX_RETRIES,
    MIN_CLAIMS,
    PROJECT_ROOT,
    Settings,
    get_settings,
    load_env_file,
)


# test_project_root_points_at_assignment_folder - test that PROJECT_ROOT points at the assignment folder
def test_project_root_points_at_assignment_folder() -> None:
    assert PROJECT_ROOT.name == "07_technical_brief_generator"
    assert (PROJECT_ROOT / "brief_generator.py").is_file()


# test_env_file_lives_in_project_root - test that ENV_FILE points at the assignment .env file
def test_env_file_lives_in_project_root() -> None:
    assert ENV_FILE == PROJECT_ROOT / ".env"
    assert (PROJECT_ROOT / ".env.example").is_file()


# test_min_claims_matches_assignment_spec - test that MIN_CLAIMS is five
def test_min_claims_matches_assignment_spec() -> None:
    assert MIN_CLAIMS == 5


# test_max_retries_matches_assignment_spec - test that MAX_RETRIES is two
def test_max_retries_matches_assignment_spec() -> None:
    assert MAX_RETRIES == 2


# test_demo_topics_match_assignment_spec - test that demo topics match the evaluator list
def test_demo_topics_match_assignment_spec() -> None:
    assert DEMO_TOPICS == [
        "Event-driven architecture",
        "GraphQL vs REST APIs",
    ]


# test_help_text_documents_cli_usage - test that HELP_TEXT documents topic and demo commands
def test_help_text_documents_cli_usage() -> None:
    assert "brief_generator.py" in HELP_TEXT
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
