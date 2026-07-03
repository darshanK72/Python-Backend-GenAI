"""Curriculum sample chunks."""

SAMPLE_DOCUMENTS: list[dict] = [
    {
        "id": "c1",
        "text": "The Notes API is built with FastAPI and stores notes in memory for demos.",
        "metadata": {"source": "api-docs", "doc_type": "api"},
    },
    {
        "id": "c2",
        "text": "Alembic applies SQLAlchemy schema migrations. Run alembic upgrade head after pulling new revisions.",
        "metadata": {"source": "db-docs", "doc_type": "api"},
    },
    {
        "id": "c3",
        "text": "JWT bearer tokens authenticate API requests. Clients send Authorization: Bearer <token>.",
        "metadata": {"source": "security-docs", "doc_type": "policy"},
    },
    {
        "id": "c4",
        "text": "Pytest fixtures share database setup across tests. Use conftest.py for session-scoped engines.",
        "metadata": {"source": "test-docs", "doc_type": "runbook"},
    },
    {
        "id": "c5",
        "text": "Alembic autogenerate compares SQLAlchemy models to the live database schema and drafts revision files.",
        "metadata": {"source": "db-docs", "doc_type": "api"},
    },
]
