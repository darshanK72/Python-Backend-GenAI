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

# RESEARCH_AGENT_URL - default base URL for the ResearchAgent A2A server
RESEARCH_AGENT_URL = "http://localhost:8001"

# RESEARCH_AGENT_PORT - HTTP port for the ResearchAgent service
RESEARCH_AGENT_PORT = 8001

# WRITER_AGENT_PORT - HTTP port for the WriterAgent service
WRITER_AGENT_PORT = 8002

# DEMO_TOPICS - evaluator sample topics for the writer demo command
DEMO_TOPICS = [
    "Event-driven architecture",
    "Observability in microservices",
]

# HELP_TEXT - the help text for starting services and the writer CLI
HELP_TEXT = """\
Usage: uvicorn research_agent:app --port 8001
       uvicorn writer_agent:app --port 8002
       python writer_agent.py "<topic>"
       python writer_agent.py demo

Services (two terminals):
  ResearchAgent   A2A server on port 8001 (AgentCard + /tasks/send)
  WriterAgent API LangGraph brief API on port 8002

CLI (ResearchAgent must already be running):
  <topic>   Discover ResearchAgent, delegate research, write a ~300-word brief
  demo      Run both evaluator sample topics

Examples:
  uvicorn research_agent:app --port 8001
  python writer_agent.py "Event-driven architecture"
  python writer_agent.py demo
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
    research_agent_url: str = Field(
        default=RESEARCH_AGENT_URL,
        validation_alias="RESEARCH_AGENT_URL",
    )

    model_config = SettingsConfigDict(extra="ignore")


# get_settings - return cached application settings loaded from environment
@lru_cache
def get_settings() -> Settings:
    load_env_file()
    return Settings()
