"""Application configuration and environment loading."""

from __future__ import annotations

from functools import lru_cache
from pathlib import Path

from dotenv import load_dotenv
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_SAMPLE_DOC = PROJECT_ROOT / "data" / "sample_langgraph_readme.txt"

MAX_TOOL_CALLS = 6

USAGE = """Usage:
  python developer_assist.py "<question>"
  python developer_assist.py demo
"""


def find_repo_root(start: Path | None = None) -> Path | None:
    start = start or PROJECT_ROOT
    for candidate in (start, *start.parents):
        if (candidate / "requirements.txt").is_file():
            return candidate
    return None


def load_env_files() -> None:
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
    openai_api_key: str = Field(default="", validation_alias="OPENAI_API_KEY")
    openai_model: str = Field(default="gpt-4o-mini", validation_alias="OPENAI_MODEL")
    llm_temperature: float = 0.0

    model_config = SettingsConfigDict(extra="ignore")


@lru_cache
def get_settings() -> Settings:
    load_env_files()
    return Settings()
