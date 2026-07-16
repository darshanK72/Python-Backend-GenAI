# Assignment 03 — Secured Notes API with Tests

**Track:** FastAPI & Web Services · **Difficulty:** Medium · **Marks:** 10 · **Est. time:** ~3 hrs

An in-memory CRUD notes service with API-key authentication, paginated listing, and comprehensive `TestClient` tests — the production hygiene pattern (auth via `Depends`, correct status codes, real tests) expected in the MAS program.

**Problem statement:** [`secured_notes_assignment.md`](secured_notes_assignment.md)

---

## Overview

An internal tool needs a small notes backend that other services can read and write — but only with a valid API key, and without returning thousands of records in one response. Writes are guarded by a single reusable `Depends` dependency; reads are open but paginated.

### What you will practice

- FastAPI CRUD with Pydantic input/output models
- Dependency injection (`Depends`) for auth and store access
- API-key header authentication (`X-API-Key`)
- Pagination with `limit` / `offset`
- Correct HTTP status codes (201, 204, 401, 404, 422)
- `TestClient` integration tests

### Tech stack

| Component | Choice |
|-----------|--------|
| Framework | FastAPI |
| Storage | In-memory dict (no database) |
| Validation | Pydantic |
| Auth | `X-API-Key` header via `Depends` |
| Tests | pytest + TestClient |

---

## Project structure

```
03_secured_notes_api/
├── app/
│   ├── main.py                 # FastAPI app entry point
│   ├── config.py               # Settings and .env loading
│   ├── dependencies.py         # API-key auth + note store injection
│   ├── endpoints/
│   │   └── notes.py            # CRUD routes
│   ├── schemas/
│   │   └── notes.py            # NoteCreate, Note, NoteListResponse
│   └── services/
│       └── note_store.py       # In-memory repository
├── tests/
│   ├── conftest.py
│   ├── endpoints/test_notes.py
│   ├── services/test_note_store.py
│   ├── schemas/test_note_schemas.py
│   ├── app/test_config.py
│   └── integration/test_crud_flow.py
├── .env.example
├── secured_notes_assignment.md
├── pytest.ini
├── requirements.txt
└── README.md
```

---

## Prerequisites

- Python 3.10+
- No external APIs required

---

## Setup

```bash
cd "01. Prerequisite Foundations/Assignments/03_secured_notes_api"
python -m venv .venv
.venv\Scripts\activate          # Windows
# source .venv/bin/activate     # macOS / Linux
pip install -r requirements.txt
copy .env.example .env          # Windows
# cp .env.example .env          # macOS / Linux
```

Default `.env`:

```env
NOTES_API_KEY=demo-key
```

---

## Configuration

Environment variables are loaded from **this assignment's** `.env` file only (`03_secured_notes_api/.env`). Copy `.env.example` to `.env` in the assignment folder before running.

| Variable | Required | Default | Description |
|----------|----------|---------|-------------|
| `NOTES_API_KEY` | No | `demo-key` | Expected value for `X-API-Key` header |
| `APP_TITLE` | No | `Secured Notes API` | Swagger title |
| `APP_DEBUG` | No | `true` | FastAPI debug mode |

---

## Run

```bash
fastapi dev app/main.py --port 8021
```

Alternative:

```bash
uvicorn app.main:app --reload --port 8021
```

- **Swagger UI:** http://127.0.0.1:8021/docs

---

## Authentication

Protected endpoints require the `X-API-Key` header:

```
X-API-Key: demo-key
```

| Endpoint | Auth required |
|----------|---------------|
| `POST /notes` | Yes |
| `DELETE /notes/{id}` | Yes |
| `GET /notes` | No |
| `GET /notes/{id}` | No |

Auth is enforced by a single `verify_api_key` dependency — no duplicated checks across endpoints.

---

## API reference

| Method | Path | Auth | Description |
|--------|------|------|-------------|
| `POST` | `/notes` | Yes | Create a note → **201** |
| `GET` | `/notes` | No | List notes (paginated) → **200** |
| `GET` | `/notes/{id}` | No | Get one note → **200** / **404** |
| `DELETE` | `/notes/{id}` | Yes | Delete a note → **204** / **404** |

### Query parameters (`GET /notes`)

| Param | Default | Constraints |
|-------|---------|-------------|
| `limit` | `10` | `1`–`100` |
| `offset` | `0` | `≥ 0` |

### Data models

```python
class NoteCreate(BaseModel):
    title: str = Field(min_length=1)
    body: str = Field(min_length=1)

class Note(BaseModel):
    id: int              # server-assigned
    title: str
    body: str
    created_at: str      # UTC ISO timestamp

class NoteListResponse(BaseModel):
    items: list[Note]
    total: int
    limit: int
    offset: int
```

---

## Sample requests

### Create note → 201

```bash
curl -X POST http://127.0.0.1:8021/notes ^
  -H "X-API-Key: demo-key" ^
  -H "Content-Type: application/json" ^
  -d "{\"title\":\"Sprint retro\",\"body\":\"Discuss blockers and release timing\"}"
```

```json
{
  "id": 1,
  "title": "Sprint retro",
  "body": "Discuss blockers and release timing",
  "created_at": "2026-07-09T06:15:00.123456+00:00"
}
```

### List notes (paginated) → 200

```bash
curl "http://127.0.0.1:8021/notes?limit=10&offset=0"
```

```json
{
  "items": [
    {
      "id": 1,
      "title": "Sprint retro",
      "body": "Discuss blockers and release timing",
      "created_at": "2026-07-09T06:15:00.123456+00:00"
    }
  ],
  "total": 1,
  "limit": 10,
  "offset": 0
}
```

### Get one note → 200 / 404

```bash
curl http://127.0.0.1:8021/notes/1
```

```json
{"detail": "Note not found."}
```

### Delete note → 204

```bash
curl -X DELETE http://127.0.0.1:8021/notes/1 -H "X-API-Key: demo-key"
```

Returns empty body with status `204`.

### Missing API key on create → 401

```bash
curl -X POST http://127.0.0.1:8021/notes ^
  -H "Content-Type: application/json" ^
  -d "{\"title\":\"No key\",\"body\":\"Fails\"}"
```

```json
{"detail": "Invalid or missing API key."}
```

### Empty title → 422

```bash
curl -X POST http://127.0.0.1:8021/notes ^
  -H "X-API-Key: demo-key" ^
  -H "Content-Type: application/json" ^
  -d "{\"title\":\"\",\"body\":\"Fails validation\"}"
```

---

## Full CRUD cycle

```bash
# 1. Create
curl -X POST http://127.0.0.1:8021/notes -H "X-API-Key: demo-key" -H "Content-Type: application/json" -d "{\"title\":\"Note 1\",\"body\":\"First note\"}"

# 2. List
curl "http://127.0.0.1:8021/notes?limit=10&offset=0"

# 3. Get by id
curl http://127.0.0.1:8021/notes/1

# 4. Delete
curl -X DELETE http://127.0.0.1:8021/notes/1 -H "X-API-Key: demo-key"
```

---

## Error handling

| Situation | Status | Detail |
|-----------|--------|--------|
| Create success | 201 | `Note` JSON |
| List / get success | 200 | `NoteListResponse` / `Note` |
| Delete success | 204 | Empty body |
| Missing / wrong `X-API-Key` | 401 | `Invalid or missing API key.` |
| Note not found | 404 | `Note not found.` |
| Empty title or body | 422 | Pydantic validation error |
| `limit` > 100 or < 1 | 422 | Pydantic validation error |

---

## Tests

```bash
pytest tests/ -v
```

Five `TestClient` scenarios covered:

- Authed create succeeds
- Unauthed create returns 401
- List pagination returns correct `items` + `total`
- Get missing note returns 404
- Delete works and returns 204

Tests use an in-memory store reset between runs — no network required.

---

## Submission checklist

- [ ] FastAPI CRUD with in-memory store and Pydantic models
- [ ] Single `Depends` auth dependency guarding both write endpoints
- [ ] Paginated list response with `items` + `total` + `limit` + `offset`
- [ ] Five passing `TestClient` tests
- [ ] README with run command, auth header instructions, and `.env.example`

**Foundation pass criteria:** 30/50 overall, with at least **12/30** across Assignments 01–03.
