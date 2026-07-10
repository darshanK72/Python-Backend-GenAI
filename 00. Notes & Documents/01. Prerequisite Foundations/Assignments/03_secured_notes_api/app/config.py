"""Application configuration and environment loading."""

from __future__ import annotations

from functools import lru_cache
from pathlib import Path

from dotenv import load_dotenv
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

PROJECT_ROOT = Path(__file__).resolve().parent.parent


def find_repo_root(start: Path | None = None) -> Path | None:
    start = start or PROJECT_ROOT
    for candidate in (start, *start.parents):
        if (candidate / "requirements.txt").is_file():
            return candidate
    return None


def load_env_files() -> None:
    """Load repo root .env first, then project-local .env overrides."""
    repo_root = find_repo_root()
    local_env = PROJECT_ROOT / ".env"

    if repo_root is not None:
        global_env = repo_root / ".env"
        if global_env.is_file():
            load_dotenv(global_env, override=False)
    if local_env.is_file():
        load_dotenv(local_env, override=True)


load_env_files()


class Settings(BaseSettings):
    """Runtime settings loaded from environment variables."""

    app_title: str = Field(default="Secured Notes API", validation_alias="APP_TITLE")
    app_debug: bool = Field(default=True, validation_alias="APP_DEBUG")
    notes_api_key: str = Field(default="demo-key", validation_alias="NOTES_API_KEY")

    model_config = SettingsConfigDict(extra="ignore")


@lru_cache
def get_settings() -> Settings:
    load_env_files()
    return Settings()
