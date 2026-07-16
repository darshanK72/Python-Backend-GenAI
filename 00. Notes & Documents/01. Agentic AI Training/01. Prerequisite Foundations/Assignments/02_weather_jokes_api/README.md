# Assignment 02 — Weather & Jokes API Service

**Track:** FastAPI & Web Services · **Difficulty:** Medium · **Marks:** 10 · **Est. time:** ~3 hrs

A FastAPI gateway that wraps [OpenWeather](https://openweathermap.org/api) and [JokeAPI](https://v2.jokeapi.dev/) behind clean, typed, documented endpoints — the same service pattern used for agent-to-agent work in the MAS program.

**Problem statement:** [`weather_jokes_assignment.md`](weather_jokes_assignment.md)

---

## Overview

Third-party APIs return noisy JSON and require secret keys. This service normalises upstream responses into Pydantic models, maps upstream failures to correct HTTP status codes, and loads the weather API key from the environment. All endpoints appear in the auto-generated Swagger UI at `/docs`.

### What you will practice

- FastAPI routing with path and query parameters
- Pydantic `response_model` validation
- External HTTP calls with `httpx`
- Environment-based secrets (`.env` + `python-dotenv`)
- Upstream error mapping (404, 502, 422)

### Tech stack

| Component | Choice |
|-----------|--------|
| Framework | FastAPI |
| HTTP client | httpx (async) |
| Validation | Pydantic |
| Config | pydantic-settings + python-dotenv |
| Tests | pytest + TestClient |

---

## Project structure

```
02_weather_jokes_api/
├── app/
│   ├── main.py                 # FastAPI app factory and router registration
│   ├── config.py               # Settings and .env loading
│   ├── dependencies.py         # Injectable service dependencies
│   ├── endpoints/
│   │   ├── health.py           # GET /health
│   │   ├── weather.py          # GET /weather?city=
│   │   └── jokes.py            # GET /joke
│   ├── schemas/
│   │   └── responses.py        # Pydantic response models
│   └── services/
│       ├── weather_service.py  # OpenWeather client
│       └── joke_service.py     # JokeAPI client
├── tests/
│   ├── conftest.py
│   ├── endpoints/
│   ├── services/
│   ├── schemas/
│   ├── app/
│   └── integration/
├── .env.example
├── weather_jokes_assignment.md
├── pytest.ini
├── requirements.txt
└── README.md
```

---

## Prerequisites

- Python 3.10+
- Free [OpenWeather API key](https://openweathermap.org/api) (JokeAPI needs no key)

---

## Setup

```bash
cd "01. Prerequisite Foundations/Assignments/02_weather_jokes_api"
python -m venv .venv
.venv\Scripts\activate          # Windows
# source .venv/bin/activate     # macOS / Linux
pip install -r requirements.txt
copy .env.example .env          # Windows
# cp .env.example .env          # macOS / Linux
```

Edit `.env` and add your OpenWeather key:

```env
OPENWEATHER_API_KEY=your_openweather_api_key_here
```

---

## Configuration

Environment variables are loaded from **this assignment's** `.env` file only (`02_weather_jokes_api/.env`). Copy `.env.example` to `.env` in the assignment folder before running live API calls.

| Variable | Required | Default | Description |
|----------|----------|---------|-------------|
| `OPENWEATHER_API_KEY` | Yes (live calls) | — | OpenWeather API key |
| `APP_TITLE` | No | `Weather & Jokes API` | Swagger title |
| `APP_DEBUG` | No | `true` | FastAPI debug mode |

The key is sent to OpenWeather as query param `appid` — never exposed to API consumers.

---

## Run

```bash
fastapi dev app/main.py --port 8020
```

Alternative:

```bash
uvicorn app.main:app --reload --port 8020
```

- **Swagger UI:** http://127.0.0.1:8020/docs
- **Health check:** http://127.0.0.1:8020/health

---

## API reference

| Method | Path | Auth | Description |
|--------|------|------|-------------|
| `GET` | `/health` | None | Liveness check |
| `GET` | `/weather` | None | Current weather for a city (`city` query param, required) |
| `GET` | `/joke` | None | Random joke normalised to setup/delivery shape |

### Response models

```python
class HealthResponse(BaseModel):
    status: str

class WeatherResponse(BaseModel):
    city: str
    temp_c: float
    conditions: str

class JokeResponse(BaseModel):
    setup: str
    delivery: str
```

Single-line jokes are normalised: `setup` = joke text, `delivery` = `""`.

---

## Sample requests

### GET /health → 200

```bash
curl http://127.0.0.1:8020/health
```

```json
{"status": "ok"}
```

### GET /weather?city=London → 200

```bash
curl "http://127.0.0.1:8020/weather?city=London"
```

```json
{"city": "London", "temp_c": 12.4, "conditions": "light rain"}
```

### GET /weather?city=NotARealCity → 404

```bash
curl -i "http://127.0.0.1:8020/weather?city=NotARealCity"
```

```json
{"detail": "City not found: NotARealCity"}
```

### GET /weather (no city) → 422

```bash
curl -i "http://127.0.0.1:8020/weather"
```

FastAPI returns a validation error because `city` is a required query parameter.

### GET /joke → 200

```bash
curl http://127.0.0.1:8020/joke
```

```json
{"setup": "Why did the developer go broke?", "delivery": "Because he used up all his cache."}
```

---

## Error handling

| Situation | HTTP status | Detail |
|-----------|-------------|--------|
| Health / successful weather or joke | 200 | Typed response body |
| Unknown city (OpenWeather 404) | 404 | `City not found: {city}` |
| Missing or empty `city` param | 422 | FastAPI validation error |
| Upstream unreachable | 502 | `Weather service is unreachable.` / `Joke service is unreachable.` |
| Upstream unexpected error | 502 | `Weather/Joke service returned an unexpected error.` |
| Missing `OPENWEATHER_API_KEY` | 502 | `OpenWeather API key is not configured.` |

Upstream failures never leak raw tracebacks to the client.

---

## Tests

```bash
pytest tests/ -v
```

Upstream APIs are **mocked** — no network access or API keys required:

- Endpoint tests override `WeatherService` / `JokeService` via `app.dependency_overrides`
- Service tests mock `httpx.AsyncClient`
- Integration tests patch HTTP clients at the service layer

---

## Submission checklist

- [ ] FastAPI app with `/health`, `/weather`, `/joke` and Pydantic `response_model`s
- [ ] API key loaded from environment; `.env` in `.gitignore`; `.env.example` committed
- [ ] README with run command and four sample requests + responses
- [ ] All endpoints visible with correct schemas in `/docs`

**Foundation pass criteria:** 30/50 overall, with at least **12/30** across Assignments 01–03.
