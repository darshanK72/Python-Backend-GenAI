# Assignment 02 — Weather & Jokes API Service

FastAPI gateway over [OpenWeather](https://openweathermap.org/api) and [JokeAPI](https://v2.jokeapi.dev/).

Problem statement: [`weather_jokes_assignment.md`](weather_jokes_assignment.md)

## Project layout

```
02_weather_jokes_api/
  app/
    main.py                 # FastAPI app factory and router registration
    config.py               # Settings and .env loading
    dependencies.py         # Injectable service dependencies
    endpoints/
      health.py             # GET /health
      weather.py            # GET /weather?city=
      jokes.py              # GET /joke
    schemas/
      responses.py          # Pydantic response models
    services/
      weather_service.py    # OpenWeather client
      joke_service.py       # JokeAPI client
  tests/
    test_api.py
  .env.example
  requirements.txt
```

## Setup

```bash
cd "00. Notes & Documents/MAS_Foundation_Assignments/02_weather_jokes_api"
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env
# Add your OpenWeather API key to .env
```

Get a free key at [OpenWeather](https://openweathermap.org/api). JokeAPI needs no key.

## Run

```bash
fastapi dev app/main.py --port 8020
# or
uvicorn app.main:app --reload --port 8020
```

Swagger UI: http://127.0.0.1:8020/docs

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

FastAPI returns a validation error because `city` is required.

### GET /joke → 200

```bash
curl http://127.0.0.1:8020/joke
```

```json
{"setup": "Why did the developer go broke?", "delivery": "Because he used up all his cache."}
```

Single-line jokes are normalised to `setup` with an empty `delivery`.

## Tests

Upstream APIs are mocked — no network access or API keys required.

```bash
pytest tests/ -v
```

### Test layout

```
tests/
  conftest.py                  # Shared fixtures (client, settings, mocks)
  endpoints/
    conftest.py                # Dependency override helpers
    test_health.py
    test_weather.py
    test_jokes.py
  services/
    conftest.py                # httpx mock helpers
    test_weather_service.py
    test_joke_service.py
  schemas/
    test_responses.py
  app/
    test_config.py
  integration/
    test_full_stack.py
```

## Error mapping

| Situation | Status | Detail |
|-----------|--------|--------|
| Unknown city (OpenWeather 404) | 404 | `City not found: {city}` |
| Upstream unreachable | 502 | `Weather/Joke service is unreachable.` |
| Missing `city` query param | 422 | FastAPI validation error |
| Missing OpenWeather API key | 502 | `OpenWeather API key is not configured.` |
