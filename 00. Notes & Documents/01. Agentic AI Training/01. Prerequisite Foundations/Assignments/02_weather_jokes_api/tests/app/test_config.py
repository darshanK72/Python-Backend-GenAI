"""Tests for configuration and dependency injection."""

from app.config import ENV_FILE, PROJECT_ROOT, Settings, get_settings, load_env_file
from app.dependencies import get_joke_service, get_weather_service
from app.services.joke_service import JokeService
from app.services.weather_service import WeatherService


# test_project_root_points_at_assignment_folder - test that PROJECT_ROOT points at the assignment folder
def test_project_root_points_at_assignment_folder() -> None:
    assert PROJECT_ROOT.name == "02_weather_jokes_api"
    assert (PROJECT_ROOT / "app" / "main.py").is_file()


# test_env_file_lives_in_project_root - test that ENV_FILE points at the assignment .env file
def test_env_file_lives_in_project_root() -> None:
    assert ENV_FILE == PROJECT_ROOT / ".env"
    assert (PROJECT_ROOT / ".env.example").is_file()


# test_load_env_file_loads_project_dotenv - test that load_env_file reads from the assignment .env file
def test_load_env_file_loads_project_dotenv(tmp_path, monkeypatch) -> None:
    monkeypatch.setattr("app.config.ENV_FILE", tmp_path / ".env")
    (tmp_path / ".env").write_text("OPENWEATHER_API_KEY=from-project-env\n", encoding="utf-8")
    monkeypatch.delenv("OPENWEATHER_API_KEY", raising=False)

    load_env_file()
    settings = Settings()

    assert settings.openweather_api_key == "from-project-env"


# test_settings_defaults - test that Settings provides expected default values
def test_settings_defaults() -> None:
    settings = Settings.model_construct()
    assert settings.app_title == "Weather & Jokes API"
    assert settings.openweather_url.startswith("https://")
    assert settings.jokeapi_url.startswith("https://")
    assert settings.http_timeout_seconds == 10.0


# test_get_settings_is_cached - test that get_settings returns the same cached instance
def test_get_settings_is_cached() -> None:
    get_settings.cache_clear()
    first = get_settings()
    second = get_settings()
    assert first is second


# test_get_weather_service_returns_weather_service - test that get_weather_service returns a WeatherService
def test_get_weather_service_returns_weather_service() -> None:
    get_weather_service.cache_clear()
    service = get_weather_service()
    assert isinstance(service, WeatherService)


# test_get_joke_service_returns_joke_service - test that get_joke_service returns a JokeService
def test_get_joke_service_returns_joke_service() -> None:
    get_joke_service.cache_clear()
    service = get_joke_service()
    assert isinstance(service, JokeService)
