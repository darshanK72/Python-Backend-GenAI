"""Application configuration and environment loading."""

from __future__ import annotations

from functools import lru_cache
from pathlib import Path

from dotenv import load_dotenv
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

# PROJECT_ROOT - the root directory of the assignment project
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# ENV_FILE - project-level environment file for this assignment
ENV_FILE = PROJECT_ROOT / ".env"

# MIN_CLAIMS - minimum verifiable claims required before the quality gate passes
MIN_CLAIMS = 5

# MAX_RETRIES - maximum researcher retries when claim_count stays below MIN_CLAIMS
MAX_RETRIES = 2

# HELP_TEXT - the help text for the technical brief generator CLI
HELP_TEXT = """\
Usage: python brief_generator.py "<topic>"
       python brief_generator.py demo

Commands:
  <topic>   Generate a structured technical brief for the given topic
  demo      Run both evaluator sample topics

Examples:
  python brief_generator.py "Event-driven architecture"
  python brief_generator.py demo
"""


# load_env_file - load environment variables from the project .env file
def load_env_file() -> None:
    """Load environment variables from this assignment's .env file."""
    if ENV_FILE.is_file():
        load_dotenv(ENV_FILE)


load_env_file()


class Settings(BaseSettings):
    """Runtime settings loaded from environment variables."""

    openai_api_key: str = Field(default="", validation_alias="OPENAI_API_KEY")
    openai_model: str = Field(default="gpt-4o-mini", validation_alias="OPENAI_MODEL")
    llm_temperature: float = 0.0

    model_config = SettingsConfigDict(extra="ignore")


# get_settings - return cached application settings loaded from environment
@lru_cache
def get_settings() -> Settings:
    load_env_file()
    return Settings()
