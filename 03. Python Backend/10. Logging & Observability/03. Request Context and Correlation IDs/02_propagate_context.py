# 02 — Propagate request ID across service calls
# Run: python 02_propagate_context.py

import json
from contextvars import ContextVar

request_id: ContextVar[str] = ContextVar("request_id")


def api_handler(headers: dict) -> dict:
    request_id.set(headers.get("X-Request-ID", "generated-id"))
    return downstream_call()


def downstream_call() -> dict:
    return {"request_id": request_id.get(), "status": "ok"}


if __name__ == "__main__":
    result = api_handler({"X-Request-ID": "abc-123"})
    print(json.dumps(result))
