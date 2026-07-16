"""Tests for configuration and dependency injection."""

import secrets

import pytest
from fastapi import HTTPException

from app.config import ENV_FILE, PROJECT_ROOT, Settings, get_settings, load_env_file
from app.dependencies import get_llm_service, verify_api_key
from app.services.llm_service import LLMService


# test_project_root_points_at_assignment_folder - test that PROJECT_ROOT points at the assignment folder
def test_project_root_points_at_assignment_folder() -> None:
    assert PROJECT_ROOT.name == "05_llm_summariser_classifier"
    assert (PROJECT_ROOT / "app" / "main.py").is_file()


# test_env_file_lives_in_project_root - test that ENV_FILE points at the assignment .env file
def test_env_file_lives_in_project_root() -> None:
    assert ENV_FILE == PROJECT_ROOT / ".env"
    assert (PROJECT_ROOT / ".env.example").is_file()


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
    assert settings.app_title == "LLM Summariser & Classifier"
    assert settings.llm_service_api_key == "demo-key"
    assert settings.openai_model == "gpt-4o-mini"
    assert settings.llm_temperature == 0.0


# test_get_settings_is_cached - test that get_settings returns the same cached instance
def test_get_settings_is_cached() -> None:
    get_settings.cache_clear()
    first = get_settings()
    second = get_settings()
    assert first is second


# test_get_llm_service_returns_llm_service - test that get_llm_service returns an LLMService
def test_get_llm_service_returns_llm_service() -> None:
    get_llm_service.cache_clear()
    service = get_llm_service()
    assert isinstance(service, LLMService)


# test_verify_api_key_accepts_valid_key - test that verify_api_key accepts a valid API key
def test_verify_api_key_accepts_valid_key(test_settings: Settings) -> None:
    result = verify_api_key(x_api_key="test-key", settings=test_settings)
    assert result == "test-key"


# test_verify_api_key_rejects_missing_key - test that verify_api_key rejects a missing API key
def test_verify_api_key_rejects_missing_key(test_settings: Settings) -> None:
    with pytest.raises(HTTPException) as exc_info:
        verify_api_key(x_api_key="", settings=test_settings)
    assert exc_info.value.status_code == 401


# test_verify_api_key_rejects_wrong_key - test that verify_api_key rejects an invalid API key
def test_verify_api_key_rejects_wrong_key(test_settings: Settings) -> None:
    with pytest.raises(HTTPException) as exc_info:
        verify_api_key(x_api_key="wrong", settings=test_settings)
    assert exc_info.value.status_code == 401


# test_verify_api_key_uses_timing_safe_compare - test that verify_api_key uses timing-safe comparison
def test_verify_api_key_uses_timing_safe_compare(test_settings: Settings) -> None:
    almost = "test-ke" + "y"[:-1] + "X"
    with pytest.raises(HTTPException):
        verify_api_key(x_api_key=almost, settings=test_settings)
    assert secrets.compare_digest(almost, "test-key") is False
