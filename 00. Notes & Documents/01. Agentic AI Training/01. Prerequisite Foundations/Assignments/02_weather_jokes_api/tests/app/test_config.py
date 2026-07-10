"""Tests for configuration and dependency injection."""

from pathlib import Path

from app.config import PROJECT_ROOT, Settings, find_repo_root, get_settings
from app.dependencies import get_joke_service, get_weather_service
from app.services.joke_service import JokeService
from app.services.weather_service import WeatherService


def test_project_root_points_at_assignment_folder() -> None:
    assert PROJECT_ROOT.name == "02_weather_jokes_api"
    assert (PROJECT_ROOT / "app" / "main.py").is_file()


def test_find_repo_root_from_project_folder() -> None:
    repo_root = find_repo_root(PROJECT_ROOT)
    assert repo_root is not None
    assert (repo_root / "requirements.txt").is_file()


def test_find_repo_root_returns_none_for_isolated_path(tmp_path: Path) -> None:
    assert find_repo_root(tmp_path) is None


def test_settings_defaults() -> None:
    settings = Settings.model_construct()
    assert settings.app_title == "Weather & Jokes API"
    assert settings.openweather_url.startswith("https://")
    assert settings.jokeapi_url.startswith("https://")
    assert settings.http_timeout_seconds == 10.0


def test_get_settings_is_cached() -> None:
    get_settings.cache_clear()
    first = get_settings()
    second = get_settings()
    assert first is second


def test_get_weather_service_returns_weather_service() -> None:
    get_weather_service.cache_clear()
    service = get_weather_service()
    assert isinstance(service, WeatherService)


def test_get_joke_service_returns_joke_service() -> None:
    get_joke_service.cache_clear()
    service = get_joke_service()
    assert isinstance(service, JokeService)
