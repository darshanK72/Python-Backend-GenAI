"""Application settings — loads global repo .env first, then project-local .env."""

from __future__ import annotations

from functools import lru_cache
from pathlib import Path

from dotenv import load_dotenv
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

PROJECT_ROOT = Path(__file__).resolve().parent.parent


def find_repo_root(start: Path | None = None) -> Path:
    start = start or PROJECT_ROOT
    for candidate in (start, *start.parents):
        if (candidate / "requirements.txt").is_file():
            return candidate
    raise RuntimeError("Could not find repo root (requirements.txt)")


REPO_ROOT = find_repo_root()


def load_env_files() -> None:
    global_env = REPO_ROOT / ".env"
    local_env = PROJECT_ROOT / ".env"
    if global_env.is_file():
        load_dotenv(global_env, override=False)
    if local_env.is_file():
        load_dotenv(local_env, override=True)


load_env_files()


class Settings(BaseSettings):
    anthropic_api_key: str = Field(default="", validation_alias="ANTHROPIC_API_KEY")
    claude_model: str = Field(
        default="claude-sonnet-4-20250514",
        validation_alias="CLAUDE_MODEL",
    )
    app_title: str = Field(default="Claude Chat API", validation_alias="APP_TITLE")
    app_debug: bool = Field(default=True, validation_alias="APP_DEBUG")
    claude_max_retries: int = Field(default=3, validation_alias="CLAUDE_MAX_RETRIES")

    model_config = SettingsConfigDict(extra="ignore")


@lru_cache
def get_settings() -> Settings:
    load_env_files()
    return Settings()
