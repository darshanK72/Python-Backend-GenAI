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

# DATA_DIR - directory for SQLite DB and session_store.json
DATA_DIR = PROJECT_ROOT / "data"

# DB_PATH - path to the seeded project_management SQLite database
DB_PATH = DATA_DIR / "project_management.db"

# FAISS_INDEX_DIR - directory for the local FAISS knowledge-base index
FAISS_INDEX_DIR = PROJECT_ROOT / "faiss_index"

# SESSION_STORE_PATH - JSON file backing cross-process session history
SESSION_STORE_PATH = DATA_DIR / "session_store.json"

# MCP_SERVER_SCRIPT - path to the FastMCP tool server script
MCP_SERVER_SCRIPT = PROJECT_ROOT / "mcp_server.py"

# MCP_SERVER_HOST - host where the developer runs mcp_server.py
MCP_SERVER_HOST = "127.0.0.1"

# MCP_SERVER_PORT - port where the developer runs mcp_server.py
MCP_SERVER_PORT = 8000

# MCP_SERVER_URL - HTTP endpoint the MCP client connects to
MCP_SERVER_URL = f"http://{MCP_SERVER_HOST}:{MCP_SERVER_PORT}/mcp"

# THREAD_ID - MemorySaver / session thread used across the demo
THREAD_ID = "capstone-session-01"

# CHUNK_SIZE - character chunk size for Wikipedia ingestion
CHUNK_SIZE = 500

# CHUNK_OVERLAP - character overlap between adjacent chunks
CHUNK_OVERLAP = 50

# RAG_K - number of FAISS neighbours returned by rag_search
RAG_K = 3

# WIKIPEDIA_ARTICLES - corpus titles used by rebuild_index.py
WIKIPEDIA_ARTICLES = [
    "Software engineering",
    "Agile software development",
    "Continuous integration",
    "DevOps",
    "Technical debt",
    "Microservices",
    "Test-driven development",
]

# DEMO_QUERIES - evaluator 4-query capstone session
DEMO_QUERIES = [
    "What is the difference between microservices and a monolith?",
    "Which of our tasks are currently blocked?",
    "What have I asked you so far?",
    (
        "Based on our conversation, are there DevOps best practices I should "
        "apply to the blocked tasks?"
    ),
]

# HELP_TEXT - the help text for the unified engineering assistant CLI
HELP_TEXT = """\
Usage: python rebuild_index.py
       python seed_db.py
       python mcp_server.py
       python engineering_assistant.py "<question>"
       python engineering_assistant.py demo

Prerequisite:
  Start the FastMCP server in a separate terminal before asking questions:
    python mcp_server.py

Backend setup (once):
  python rebuild_index.py   # FAISS knowledge base
  python seed_db.py         # project_management.db

Commands:
  <question>   Ask one question (same thread_id across runs)
  demo         Run the required 4-query capstone session

Examples:
  python engineering_assistant.py "Which of our tasks are currently blocked?"
  python engineering_assistant.py demo
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
