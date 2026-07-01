# Sample knowledge base for RAG lessons
# Used by 01_naive_rag.py and 02_rag_with_openai.py

DOCUMENTS = [
    {
        "id": "1",
        "text": "Our Notes API stores notes in memory and exposes REST endpoints with FastAPI.",
        "source": "api-docs",
    },
    {
        "id": "2",
        "text": "Alembic manages database schema migrations for SQLAlchemy projects.",
        "source": "db-docs",
    },
    {
        "id": "3",
        "text": "JWT tokens are used for stateless authentication in APIs.",
        "source": "security-docs",
    },
]
