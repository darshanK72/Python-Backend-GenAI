# Vector Databases — Hands-On FastAPI Apps

Three FastAPI services demonstrate the same retrieval API on different vector stores (notebooks 05–08).

| # | Database | Port | Folder |
|---|----------|------|--------|
| 01 | **Chroma** (embedded, local) | 8013 | `01. Chroma/` |
| 02 | **Pinecone** (managed cloud) | 8014 | `02. Pinecone/` |
| 03 | **pgvector** (PostgreSQL extension) | 8015 | `03. PgVector/` |

Each topic folder contains `app/` (FastAPI code) and `.env.example`. Run `uvicorn` from the topic folder.

## Shared API

| Method | Path | Purpose |
|--------|------|---------|
| `GET` | `/health` | Service + store status |
| `POST` | `/api/v1/documents` | Upsert one document |
| `POST` | `/api/v1/documents/batch` | Upsert many documents |
| `GET` | `/api/v1/documents/{id}` | Fetch by id |
| `DELETE` | `/api/v1/documents/{id}` | Delete by id |
| `GET` | `/api/v1/documents` | Count indexed documents |
| `POST` | `/api/v1/search` | Semantic search |
| `POST` | `/api/v1/seed` | Load curriculum sample chunks |

Embeddings: **OpenAI** `text-embedding-3-small` (1536 dimensions). Set `OPENAI_API_KEY` in the repo root `.env`.

## Quick start — Chroma

```bash
cd "01. Chroma"
uvicorn app.main:app --reload --port 8013
```

http://127.0.0.1:8013/docs → `POST /api/v1/seed` → `POST /api/v1/search`

## Quick start — Pinecone

1. Create a serverless index: dimension **1536**, metric **cosine**.
2. Copy `.env.example` → `.env`; set `PINECONE_API_KEY` and `PINECONE_INDEX_NAME`.

```bash
cd "02. Pinecone"
uvicorn app.main:app --reload --port 8014
```

## Quick start — pgvector

```bash
cd "03. PgVector"
docker compose up -d
# copy .env.example → .env
uvicorn app.main:app --reload --port 8015
```

## Prerequisites

- Repo venv: `pip install -r requirements.txt`
- `OPENAI_API_KEY` for all three
- Pinecone account + index for **02**
- Docker for **03** (or Postgres with `vector` extension)
