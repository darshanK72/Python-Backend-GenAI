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

# FAISS_INDEX_DIR - directory where the FAISS vector index is saved
FAISS_INDEX_DIR = PROJECT_ROOT / "faiss_index"

# CHUNK_SIZE - character length of each Wikipedia article chunk
CHUNK_SIZE = 500

# CHUNK_OVERLAP - characters overlapped between consecutive chunks
CHUNK_OVERLAP = 50

# RETRIEVAL_K - number of chunks retrieved from FAISS per question
RETRIEVAL_K = 4

# EMBEDDING_MODEL - OpenAI embedding model used for indexing and search
EMBEDDING_MODEL = "text-embedding-3-small"

# WIKIPEDIA_ARTICLES - corpus article titles fetched for the knowledge base
WIKIPEDIA_ARTICLES = [
    "Software engineering",
    "Agile software development",
    "Continuous integration",
    "DevOps",
    "Technical debt",
    "Microservices",
    "Test-driven development",
]

# HELP_TEXT - the help text for the engineering KB Q&A CLI
HELP_TEXT = """\
Usage: python rebuild_index.py
       python kb_qa.py "<question>"
       python kb_qa.py demo

Prerequisite:
  Build the FAISS index once before asking questions:
    python rebuild_index.py

Commands:
  <question>   Ask a corrective RAG question against the engineering KB
  demo         Run all four evaluator sample queries

Examples:
  python kb_qa.py "What is trunk-based development and why do teams adopt it?"
  python kb_qa.py demo
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
