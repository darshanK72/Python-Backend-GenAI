"""Application configuration."""

from __future__ import annotations

from functools import lru_cache
from pathlib import Path

from dotenv import load_dotenv
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

# PROJECT_ROOT - the root directory of the assignment project
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# DEFAULT_REPORTS_FILE - the default bug reports fixture file (all categories combined)
DEFAULT_REPORTS_FILE = PROJECT_ROOT / "data" / "reports.json"

# REPORT_CATEGORY_FILES - category-specific bug report fixture files
REPORT_CATEGORY_FILES = {
    "auth": PROJECT_ROOT / "data" / "auth.json",
    "performance": PROJECT_ROOT / "data" / "performance.json",
    "notifications": PROJECT_ROOT / "data" / "notifications.json",
    "settings": PROJECT_ROOT / "data" / "settings.json",
    "feature_requests": PROJECT_ROOT / "data" / "feature_requests.json",
}

# ENV_FILE - project-level environment file for this assignment
ENV_FILE = PROJECT_ROOT / ".env"

# HELP_TEXT - the help text for the prompt engineering toolkit CLI
HELP_TEXT = """\
Usage: python prompt_toolkit.py [reports_file]

Runs naive, structured, and few-shot extraction over each bug report in a JSON file.

Category files in data/:
  auth.json, performance.json, notifications.json, settings.json, feature_requests.json
  reports.json — all categories combined (default)

Examples:
  python prompt_toolkit.py
  python prompt_toolkit.py data/auth.json
  python prompt_toolkit.py data/reports.json
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
    extraction_temperature: float = 0.0

    model_config = SettingsConfigDict(extra="ignore")


# get_settings - return cached application settings loaded from environment
@lru_cache
def get_settings() -> Settings:
    load_env_file()
    return Settings()
