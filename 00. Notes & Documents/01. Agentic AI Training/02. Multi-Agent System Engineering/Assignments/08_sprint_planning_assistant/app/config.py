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

# MCP_SERVER_SCRIPT - path to the FastMCP sprint backlog server script
MCP_SERVER_SCRIPT = PROJECT_ROOT / "mcp_server.py"

# MCP_SERVER_HOST - host where the developer runs mcp_server.py
MCP_SERVER_HOST = "127.0.0.1"

# MCP_SERVER_PORT - port where the developer runs mcp_server.py
MCP_SERVER_PORT = 8000

# MCP_SERVER_URL - HTTP endpoint the MCP client connects to
MCP_SERVER_URL = f"http://{MCP_SERVER_HOST}:{MCP_SERVER_PORT}/mcp"

# DEFAULT_VELOCITY - default sprint velocity used by the capacity checker
DEFAULT_VELOCITY = 40

# HELP_TEXT - the help text for the sprint planning assistant CLI
HELP_TEXT = """\
Usage: python sprint_planner.py "<request>"
       python sprint_planner.py demo

Prerequisite:
  Start the MCP server in a separate terminal first:
    python mcp_server.py

Commands:
  <request>   Route a sprint planning request through the supervisor agent
  demo        Run all five evaluator sample requests

Examples:
  python sprint_planner.py "Check capacity"
  python sprint_planner.py demo
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
    mcp_server_url: str = Field(default=MCP_SERVER_URL, validation_alias="MCP_SERVER_URL")

    model_config = SettingsConfigDict(extra="ignore")


# get_settings - return cached application settings loaded from environment
@lru_cache
def get_settings() -> Settings:
    load_env_file()
    return Settings()
