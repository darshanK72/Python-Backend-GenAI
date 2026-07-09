# pgvector — Vector Store API

**PostgreSQL + pgvector** — vectors alongside relational data (notebooks 05, 08).

## Layout

```
03. PgVector/
  app/
  docker-compose.yml
  .env.example
```

## Run Postgres

```bash
cd "03. PgVector"
docker compose up -d
```

Postgres on **localhost:5433** (see `docker-compose.yml`).

## Run API

```bash
cd "03. PgVector"
# copy .env.example → .env
uvicorn app.main:app --reload --port 8015
```

Swagger UI: http://127.0.0.1:8015/docs

## Environment

| Variable | Default | Description |
|----------|---------|-------------|
| `OPENAI_API_KEY` | — | Required for embeddings |
| `DATABASE_URL` | see `.env.example` | SQLAlchemy URL (`postgresql+psycopg://...`) |
| `PGVECTOR_TABLE` | `documents` | Table name in responses |
