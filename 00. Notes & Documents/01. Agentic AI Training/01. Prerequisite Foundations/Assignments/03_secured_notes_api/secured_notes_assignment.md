# Assignment 03 — Secured Notes API with Tests

**Source:** MAS_TRAINING-000_Prerequisite_Foundations  
**Track:** FastAPI & Web Services  
**Difficulty:** Medium  
**Marks:** 10  
**Estimated time:** ~3 hours  
**Required stack:** Python · FastAPI · Pydantic · pytest · Depends

---

## Pattern

FastAPI — CRUD, dependency injection, API-key auth, pagination, TestClient tests.

---

## Scenario

An internal tool needs a small notes backend that other services can read and write — but only with a valid API key, and without dumping thousands of records in a single response. You are building a secured, paginated, tested CRUD service. This is the closest foundation assignment to the production hygiene the MAS program expects: auth via dependencies, correct status codes, and real tests.

---

## What You Need to Build

A FastAPI application exposing CRUD endpoints over an **in-memory notes store** (a dict or list — no database needed). Writes require authentication via an API-key header, enforced through a FastAPI dependency. Listing is paginated.

### Data model

A **Note** has:

| Field | Type | Notes |
|-------|------|-------|
| `id` | int | Server-assigned |
| `title` | str | Required |
| `body` | str | Required |
| `created_at` | str | ISO timestamp, server-set |

Use Pydantic models: **NoteCreate** (input) and **Note** (output).

### Endpoints

| Method | Path | Auth | Description |
|--------|------|------|-------------|
| `POST` | `/notes` | Required | Create a note from `NoteCreate`; returns the created `Note` with **201**. |
| `GET` | `/notes?limit={n}&offset={m}` | None | List notes, paginated; returns items plus total count. |
| `GET` | `/notes/{id}` | None | Retrieve one note; **404** if not found. |
| `DELETE` | `/notes/{id}` | Required | Delete a note; **204** on success, **404** if not found. |

### List response shape

Paginated list responses must have:

```json
{
  "items": [...],
  "total": 0,
  "limit": 10,
  "offset": 0
}
```

### Behaviours & constraints

- **Auth dependency:** A single `Depends`-injected function checks an `X-API-Key` header against a key from the environment. Missing/wrong key → **401**. The same dependency guards **both write endpoints** — no copy-pasted checks.
- **Pagination:** `limit` defaults to **10** (max **100**), `offset` defaults to **0**. The list response has shape `{items: [...], total: int, limit: int, offset: int}`.
- **Validation:** Creating a note with an empty title or missing body returns **422** automatically via Pydantic.
- **Status codes:** **201** on create, **204** on delete, **404** for missing id, **401** for bad/missing key, **422** for validation.
- **Tests:** pytest tests using FastAPI's `TestClient` covering:
  - authed create succeeds
  - unauthed create is 401
  - list pagination works
  - get-missing is 404
  - delete works

### Environment & secrets

- API key loaded from environment variable (e.g. `NOTES_API_KEY`)
- `.env` in `.gitignore`; `.env.example` committed
- Never commit the real key

---

## Milestones

| Phase | What you're building | Time |
|-------|----------------------|------|
| **M1 — Models & Store** | Define `NoteCreate` / `Note` models and the in-memory store with server-assigned ids and timestamps. | 30 min |
| **M2 — CRUD Endpoints** | Implement create, list (paginated), get, and delete with correct status codes. | 45 min |
| **M3 — Auth Dependency** | Build the `X-API-Key` `Depends` function and guard both write endpoints; wire the key from the environment. | 40 min |
| **M4 — Tests & Docs** | Write the five `TestClient` tests; README with run command, auth instructions, and sample requests. | 35 min |

---

## Marking Rubric (10 marks)

Each criterion is worth **2 marks**.

| # | Criterion | 2 marks — Full | 1 mark — Partial | 0 marks — Missing |
|---|-----------|----------------|------------------|-------------------|
| 1 | **Structure & Correctness** | FastAPI CRUD with Pydantic input/output models; ids and timestamps server-assigned; correct status codes throughout | CRUD works but status codes wrong (e.g. 200 on create), or models conflated | Not CRUD; missing endpoints; wrong framework |
| 2 | **Core Functionality (Auth + Pagination)** | Auth enforced via a single `Depends` on both writes; 401 on bad key; pagination returns correct items + total | Auth present but duplicated inline rather than a dependency, or pagination ignores limit/offset | No auth, or writes are open; no pagination |
| 3 | **Error Handling & Robustness** | Missing id → 404; bad/missing key → 401; invalid body → 422; limit capped at 100 | Most handled; one wrong (e.g. missing id returns 500) | No error handling; crashes on missing id or bad input |
| 4 | **End-to-End Run** | All sample requests behave as specified; full create→list→get→delete cycle works | Cycle mostly works; one step wrong | Crashes or core cycle fails |
| 5 | **Documentation & Tests** | Five `TestClient` tests pass; README with run + auth instructions; `.env.example` committed | Runs; some tests missing or README thin | No tests; no README |

---

## Submission Checklist

- [ ] FastAPI CRUD service with in-memory store and Pydantic models
- [ ] Single `Depends` auth dependency guarding both write endpoints
- [ ] Paginated list response with `items` + `total` + `limit` + `offset`
- [ ] Five passing `TestClient` tests
- [ ] README with run command, auth header instructions, and `.env.example`

---

## Pass context (foundation course)

Foundation pass criteria: **30/50 overall**, with at least **12/30** across Assignments 01–03.
