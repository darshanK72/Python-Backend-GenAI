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

# MIN_PLAN_STEPS - minimum number of delivery steps the planner must return
MIN_PLAN_STEPS = 4

# MAX_PLAN_STEPS - maximum number of delivery steps the planner may return
MAX_PLAN_STEPS = 6

# PLANNER_TEMPERATURE - OpenAI temperature for the planner node
PLANNER_TEMPERATURE = 0.7

# EXECUTOR_TEMPERATURE - OpenAI temperature for the executor node
EXECUTOR_TEMPERATURE = 0.2

# HELP_TEXT - the help text for the feature scoping CLI
HELP_TEXT = """\
Usage: python feature_scoper.py "<feature request>"
       python feature_scoper.py demo

Commands:
  <feature request>   Scope a single feature into a delivery plan
  demo                Run both evaluator sample features (A and B)

Examples:
  python feature_scoper.py "Add email notifications when a task's status changes to blocked"
  python feature_scoper.py demo
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
