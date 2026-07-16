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

# DATA_DIR - directory that holds sample incident JSON files
DATA_DIR = PROJECT_ROOT / "data"

# THREAD_ID - MemorySaver thread id shared across a demo shift
THREAD_ID = "shift-2024-11-15"

# ONCALL_ROSTER - hardcoded on-call names for PagerDuty round-robin
ONCALL_ROSTER = ["Alice Chen", "Bob Kumar", "Carol Smith"]

# INCIDENT_FILES - demo incident JSON paths under data/
INCIDENT_FILES = [
    DATA_DIR / "incident_01.json",
    DATA_DIR / "incident_02.json",
    DATA_DIR / "incident_03.json",
]

# HELP_TEXT - the help text for the on-call incident CLI
HELP_TEXT = """\
Usage: python incident_handler.py data/incident_01.json
       python incident_handler.py demo

Commands:
  <incident.json>   Handle one incident file (paths under data/ are preferred)
  demo              Run all three sample incidents on the same shift thread

Examples:
  python incident_handler.py data/incident_01.json
  python incident_handler.py demo

Notes:
  All calls use thread_id = 'shift-2024-11-15' so MemorySaver keeps incident_history.
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
