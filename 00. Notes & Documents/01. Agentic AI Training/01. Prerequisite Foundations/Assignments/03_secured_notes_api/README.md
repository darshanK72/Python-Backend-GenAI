# Assignment 03 — Secured Notes API with Tests

In-memory CRUD notes service with API-key auth, pagination, and pytest tests.

Problem statement: [`secured_notes_assignment.md`](secured_notes_assignment.md)

## Project layout

```
03_secured_notes_api/
  app/
    main.py                 # FastAPI app entry point
    config.py               # Settings and .env loading
    dependencies.py         # API-key auth + note store injection
    endpoints/
      notes.py              # CRUD routes
    schemas/
      notes.py              # NoteCreate, Note, NoteListResponse
    services/
      note_store.py         # In-memory repository
  tests/
    conftest.py
    endpoints/test_notes.py
    services/test_note_store.py
    schemas/test_notes.py
    app/test_config.py
    integration/test_crud_flow.py
  .env.example
  requirements.txt
```

## Setup

```bash
cd "00. Notes & Documents/MAS_Foundation_Assignments/03_secured_notes_api"
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env
```

## Run

```bash
fastapi dev app/main.py --port 8021
# or
uvicorn app.main:app --reload --port 8021
```

Docs: http://127.0.0.1:8021/docs

## Auth

Protected endpoints (`POST /notes`, `DELETE /notes/{id}`) require:

```
X-API-Key: demo-key
```

## Sample requests

### Create note (auth required) → 201

```bash
curl -X POST http://127.0.0.1:8021/notes ^
  -H "X-API-Key: demo-key" ^
  -H "Content-Type: application/json" ^
  -d "{\"title\":\"Sprint retro\",\"body\":\"Discuss blockers\"}"
```

### List notes (paginated) → 200

```bash
curl "http://127.0.0.1:8021/notes?limit=10&offset=0"
```

### Get one note → 200 / 404

```bash
curl http://127.0.0.1:8021/notes/1
```

### Delete note (auth required) → 204

```bash
curl -X DELETE http://127.0.0.1:8021/notes/1 -H "X-API-Key: demo-key"
```

### Missing key on create → 401

```bash
curl -X POST http://127.0.0.1:8021/notes ^
  -H "Content-Type: application/json" ^
  -d "{\"title\":\"No key\",\"body\":\"Fails\"}"
```

### Empty title → 422

```bash
curl -X POST http://127.0.0.1:8021/notes ^
  -H "X-API-Key: demo-key" ^
  -H "Content-Type: application/json" ^
  -d "{\"title\":\"\",\"body\":\"Fails validation\"}"
```

## Tests

```bash
pytest tests/ -v
```

No network access required.
