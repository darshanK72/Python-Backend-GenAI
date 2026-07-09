# Chroma — Vector Store API

Embedded **Chroma** with persistent disk storage (notebooks 06–07).

## Layout

```
01. Chroma/
  app/              # FastAPI application
  .env.example      # optional local overrides
  chroma_data/      # created at runtime (CHROMA_PERSIST_PATH)
```

## Run

```bash
cd "01. Chroma"
uvicorn app.main:app --reload --port 8013
```

- Swagger UI: http://127.0.0.1:8013/docs
- Data path: `./chroma_data` (override with `CHROMA_PERSIST_PATH`)

## Environment

| Variable | Default | Description |
|----------|---------|-------------|
| `OPENAI_API_KEY` | — | Required for embeddings |
| `OPENAI_EMBEDDING_MODEL` | `text-embedding-3-small` | Embedding model |
| `CHROMA_PERSIST_PATH` | `./chroma_data` | On-disk Chroma path |
| `CHROMA_COLLECTION` | `notes_docs` | Collection name |

Copy `.env.example` → `.env` in this folder for local overrides (loads after repo root `.env`).
