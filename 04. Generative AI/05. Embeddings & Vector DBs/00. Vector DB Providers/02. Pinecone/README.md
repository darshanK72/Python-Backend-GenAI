# Pinecone — Vector Store API

Managed **Pinecone** serverless index (notebooks 05, 08).

## Layout

```
02. Pinecone/
  app/
  .env.example
```

## Prerequisites

1. [Pinecone](https://www.pinecone.io/) account and API key
2. Serverless index: **dimension 1536**, metric **cosine**

## Run

```bash
cd "02. Pinecone"
# copy .env.example → .env
uvicorn app.main:app --reload --port 8014
```

Swagger UI: http://127.0.0.1:8014/docs

## Environment

| Variable | Default | Description |
|----------|---------|-------------|
| `OPENAI_API_KEY` | — | Required for embeddings |
| `PINECONE_API_KEY` | — | Pinecone API key |
| `PINECONE_INDEX_NAME` | — | Existing index name |
| `PINECONE_NAMESPACE` | `notes-docs` | Namespace for vectors |
