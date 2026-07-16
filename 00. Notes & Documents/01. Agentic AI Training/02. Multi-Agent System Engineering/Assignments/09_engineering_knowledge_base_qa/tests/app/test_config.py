"""Tests for configuration."""

from app.cli.commands import DEMO_QUERIES
from app.config import (
    CHUNK_OVERLAP,
    CHUNK_SIZE,
    EMBEDDING_MODEL,
    ENV_FILE,
    FAISS_INDEX_DIR,
    HELP_TEXT,
    PROJECT_ROOT,
    RETRIEVAL_K,
    WIKIPEDIA_ARTICLES,
    Settings,
    get_settings,
    load_env_file,
)


# test_project_root_points_at_assignment_folder - test that PROJECT_ROOT points at the assignment folder
def test_project_root_points_at_assignment_folder() -> None:
    assert PROJECT_ROOT.name == "09_engineering_kb_qa"
    assert (PROJECT_ROOT / "kb_qa.py").is_file()


# test_env_file_lives_in_project_root - test that ENV_FILE points at the assignment .env file
def test_env_file_lives_in_project_root() -> None:
    assert ENV_FILE == PROJECT_ROOT / ".env"
    assert (PROJECT_ROOT / ".env.example").is_file()


# test_faiss_index_dir_points_at_project_folder - test that FAISS_INDEX_DIR is under PROJECT_ROOT
def test_faiss_index_dir_points_at_project_folder() -> None:
    assert FAISS_INDEX_DIR == PROJECT_ROOT / "faiss_index"


# test_chunking_and_retrieval_defaults - test chunk size, overlap, and retrieval k
def test_chunking_and_retrieval_defaults() -> None:
    assert CHUNK_SIZE == 500
    assert CHUNK_OVERLAP == 50
    assert RETRIEVAL_K == 4
    assert EMBEDDING_MODEL == "text-embedding-3-small"


# test_wikipedia_corpus_has_seven_articles - test that the corpus matches the assignment list
def test_wikipedia_corpus_has_seven_articles() -> None:
    assert len(WIKIPEDIA_ARTICLES) == 7
    assert "Continuous integration" in WIKIPEDIA_ARTICLES
    assert "Technical debt" in WIKIPEDIA_ARTICLES


# test_demo_queries_match_assignment_spec - test that demo queries match the evaluator list
def test_demo_queries_match_assignment_spec() -> None:
    assert len(DEMO_QUERIES) == 4
    assert "trunk-based" in DEMO_QUERIES[0]
    assert "Federal Reserve" in DEMO_QUERIES[3]


# test_help_text_documents_cli_usage - test that HELP_TEXT documents ask, demo, and rebuild
def test_help_text_documents_cli_usage() -> None:
    assert "kb_qa.py" in HELP_TEXT
    assert "demo" in HELP_TEXT
    assert "rebuild_index.py" in HELP_TEXT


# test_load_env_file_loads_project_dotenv - test that load_env_file reads from the assignment .env file
def test_load_env_file_loads_project_dotenv(tmp_path, monkeypatch) -> None:
    monkeypatch.setattr("app.config.ENV_FILE", tmp_path / ".env")
    (tmp_path / ".env").write_text("OPENAI_API_KEY=from-project-env\n", encoding="utf-8")
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)

    load_env_file()
    settings = Settings()

    assert settings.openai_api_key == "from-project-env"


# test_settings_defaults - test that Settings provides expected default values
def test_settings_defaults() -> None:
    settings = Settings.model_construct()
    assert settings.openai_model == "gpt-4o-mini"
    assert settings.llm_temperature == 0.0


# test_get_settings_is_cached - test that get_settings returns the same cached instance
def test_get_settings_is_cached() -> None:
    get_settings.cache_clear()
    first = get_settings()
    second = get_settings()
    assert first is second
