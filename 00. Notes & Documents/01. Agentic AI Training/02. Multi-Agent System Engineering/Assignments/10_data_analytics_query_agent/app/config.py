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

# DATA_DIR - directory that holds the SQLite analytics database
DATA_DIR = PROJECT_ROOT / "data"

# DB_PATH - path to the seeded SQLite database file
DB_PATH = DATA_DIR / "analytics.db"

# MAX_RETRIES - maximum validator-triggered generation retries
MAX_RETRIES = 2

# FAILURE_MESSAGE - response when SQL cannot be validated after max retries
FAILURE_MESSAGE = (
    "Unable to generate valid SQL after 2 attempts. Please rephrase your question."
)

# HELP_TEXT - the help text for the analytics query CLI
HELP_TEXT = """\
Usage: python seed_db.py
       python analytics_query.py "<question>"
       python analytics_query.py demo

Prerequisite:
  Seed the SQLite database once before asking questions:
    python seed_db.py

Commands:
  <question>   Ask a natural-language analytics question against the database
  demo         Run all four evaluator sample queries

Examples:
  python analytics_query.py "How many tasks are currently blocked?"
  python analytics_query.py demo
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
