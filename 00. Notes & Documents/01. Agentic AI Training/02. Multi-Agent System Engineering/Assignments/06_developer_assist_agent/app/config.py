"""Application configuration and environment loading."""

from __future__ import annotations

from functools import lru_cache
from pathlib import Path

from dotenv import load_dotenv
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

# PROJECT_ROOT - the root directory of the assignment project
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# DEFAULT_SAMPLE_DOC - sample LangGraph documentation used by the demo command
DEFAULT_SAMPLE_DOC = PROJECT_ROOT / "data" / "sample_langgraph_readme.txt"

# ENV_FILE - project-level environment file for this assignment
ENV_FILE = PROJECT_ROOT / ".env"

# MAX_TOOL_CALLS - maximum tool calls before the agent must finalise
MAX_TOOL_CALLS = 6

# HELP_TEXT - the help text for the developer assist CLI
HELP_TEXT = """\
Usage: python developer_assist.py "<question>"
       python developer_assist.py demo

Commands:
  <question>   Ask the ReAct developer assist agent a question
  demo         Run all four evaluator sample queries

Examples:
  python developer_assist.py "What stack should I use for real-time notifications?"
  python developer_assist.py demo
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
