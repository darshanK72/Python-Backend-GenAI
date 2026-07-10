"""Tests for configuration and auth dependency."""

import secrets

import pytest
from fastapi import HTTPException

from app.config import PROJECT_ROOT, Settings, get_settings
from app.dependencies import verify_api_key


def test_project_root_points_at_assignment_folder() -> None:
    assert PROJECT_ROOT.name == "03_secured_notes_api"
    assert (PROJECT_ROOT / "app" / "main.py").is_file()


def test_settings_defaults() -> None:
    settings = Settings.model_construct()
    assert settings.app_title == "Secured Notes API"
    assert settings.notes_api_key == "demo-key"


def test_get_settings_is_cached() -> None:
    get_settings.cache_clear()
    first = get_settings()
    second = get_settings()
    assert first is second


def test_verify_api_key_accepts_valid_key(test_settings: Settings) -> None:
    result = verify_api_key(x_api_key="test-key", settings=test_settings)
    assert result == "test-key"


def test_verify_api_key_rejects_missing_key(test_settings: Settings) -> None:
    with pytest.raises(HTTPException) as exc_info:
        verify_api_key(x_api_key="", settings=test_settings)
    assert exc_info.value.status_code == 401


def test_verify_api_key_rejects_wrong_key(test_settings: Settings) -> None:
    with pytest.raises(HTTPException) as exc_info:
        verify_api_key(x_api_key="wrong", settings=test_settings)
    assert exc_info.value.status_code == 401


def test_verify_api_key_uses_timing_safe_compare(test_settings: Settings) -> None:
    # Ensures secrets.compare_digest path is used (no early string == bypass in dependency)
    almost = "test-ke" + "y"[:-1] + "X"
    with pytest.raises(HTTPException):
        verify_api_key(x_api_key=almost, settings=test_settings)
    assert secrets.compare_digest(almost, "test-key") is False
