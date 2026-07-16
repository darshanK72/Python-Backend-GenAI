"""httpx client helpers for A2A discovery and delegation."""

from __future__ import annotations

from typing import Any, Protocol
from uuid import uuid4

import httpx

from app.config import RESEARCH_AGENT_URL


class HttpClient(Protocol):
    """Minimal httpx-compatible client protocol for injection in tests."""

    def get(self, url: str, **kwargs: Any) -> Any: ...
    def post(self, url: str, **kwargs: Any) -> Any: ...


# _unavailable_error - clear RuntimeError when ResearchAgent is down
def _unavailable_error(base_url: str, exc: Exception) -> RuntimeError:
    return RuntimeError(
        f"ResearchAgent unreachable at {base_url}. "
        "Start it first with: uvicorn research_agent:app --port 8001"
    )


# discover_agent - GET /.well-known/agent.json and return the AgentCard
def discover_agent(
    base_url: str = RESEARCH_AGENT_URL,
    *,
    client: HttpClient | None = None,
) -> dict:
    """GET /.well-known/agent.json and return the AgentCard."""
    http = client or httpx.Client(timeout=30.0)
    owns_client = client is None
    try:
        response = http.get(f"{base_url}/.well-known/agent.json")
        response.raise_for_status()
        return response.json()
    except (httpx.ConnectError, httpx.TimeoutException) as exc:
        raise _unavailable_error(base_url, exc) from exc
    finally:
        if owns_client:
            http.close()


# delegate_task - POST /tasks/send and return (task_id, research output)
def delegate_task(
    topic: str,
    *,
    base_url: str = RESEARCH_AGENT_URL,
    client: HttpClient | None = None,
    task_id: str | None = None,
) -> tuple[str, str]:
    """POST /tasks/send and return (task_id, research output)."""
    http = client or httpx.Client(timeout=60.0)
    owns_client = client is None
    task_id = task_id or str(uuid4())
    payload = {
        "id": task_id,
        "message": {"role": "user", "content": topic},
    }
    try:
        response = http.post(f"{base_url}/tasks/send", json=payload)
        response.raise_for_status()
        data = response.json()
        return task_id, data["output"]
    except (httpx.ConnectError, httpx.TimeoutException) as exc:
        raise _unavailable_error(base_url, exc) from exc
    finally:
        if owns_client:
            http.close()


# fetch_task - GET /tasks/{task_id} for async polling clients
def fetch_task(
    task_id: str,
    *,
    base_url: str = RESEARCH_AGENT_URL,
    client: HttpClient | None = None,
) -> dict:
    """GET /tasks/{task_id} for async polling clients."""
    http = client or httpx.Client(timeout=30.0)
    owns_client = client is None
    try:
        response = http.get(f"{base_url}/tasks/{task_id}")
        response.raise_for_status()
        return response.json()
    except (httpx.ConnectError, httpx.TimeoutException) as exc:
        raise _unavailable_error(base_url, exc) from exc
    finally:
        if owns_client:
            http.close()
