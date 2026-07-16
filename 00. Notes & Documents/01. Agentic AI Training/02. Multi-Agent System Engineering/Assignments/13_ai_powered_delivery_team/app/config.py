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

# MAX_ROUNDS - maximum SelectorGroupChat turns before forced stop
MAX_ROUNDS = 15

# TERMINATION_TOKEN - text token that ends the group chat when spoken by DevOps
TERMINATION_TOKEN = "DEPLOYMENT_COMPLETE"

# TRANSCRIPT_PATH - saved group-chat transcript path
TRANSCRIPT_PATH = PROJECT_ROOT / "transcript.txt"

# REPORT_PATH - saved delivery_report.md path
REPORT_PATH = PROJECT_ROOT / "delivery_report.md"

# FEATURE_REQUEST - evaluator feature that kicks off the delivery simulation
FEATURE_REQUEST = (
    "Add real-time task status notifications so that team members are instantly "
    "alerted via the app when any of their assigned tasks are updated."
)

# REPORT_SECTIONS - required headings in delivery_report.md
REPORT_SECTIONS = [
    "Executive Summary",
    "Technical Design",
    "Test Coverage",
    "Deployment Configuration",
    "Open Questions",
]

# HELP_TEXT - the help text for the delivery team CLI
HELP_TEXT = """\
Usage: python delivery_team.py
       python delivery_team.py "<feature request>"
       python delivery_team.py --save
       python delivery_team.py --save "<feature request>"

Commands:
  (default)           Run with the evaluator sample feature request
  <feature request>   Run with your own feature brief
  --save              Also write transcript.txt and delivery_report.md

Examples:
  python delivery_team.py
  python delivery_team.py "Add OAuth login for GitHub accounts"
  python delivery_team.py --save "Add CSV export for the backlog"
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
