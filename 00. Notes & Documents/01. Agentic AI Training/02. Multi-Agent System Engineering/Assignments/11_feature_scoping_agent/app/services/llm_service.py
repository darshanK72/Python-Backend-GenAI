"""OpenAI chat client wrapper."""

from __future__ import annotations

from typing import Any, Protocol

from openai import OpenAI

from app.config import Settings, get_settings


class ChatClient(Protocol):
    """Minimal OpenAI-compatible chat client protocol for injection in tests."""

    class Chat:
        class Completions:
            def create(self, **kwargs: Any) -> Any: ...

        completions: Completions

    chat: Chat


class LLMService:
    """Thin OpenAI chat wrapper with injectable client for tests."""

    # __init__ - store settings and optional pre-built client
    def __init__(
        self,
        settings: Settings | None = None,
        client: ChatClient | None = None,
    ) -> None:
        self.settings = settings or get_settings()
        self._client = client

    # client - lazily construct the OpenAI client when an API key is configured
    @property
    def client(self) -> ChatClient:
        if self._client is None:
            if not self.settings.openai_api_key:
                raise RuntimeError("OPENAI_API_KEY is not set in the environment.")
            self._client = OpenAI(api_key=self.settings.openai_api_key)
        return self._client

    # chat - send chat messages and return the assistant content string
    def chat(self, messages: list[dict[str, str]], *, temperature: float | None = None) -> str:
        """Send chat messages and return the assistant content string."""
        response = self.client.chat.completions.create(
            model=self.settings.openai_model,
            messages=messages,
            temperature=(
                self.settings.llm_temperature if temperature is None else temperature
            ),
        )
        return response.choices[0].message.content or ""
