"""OpenAI chat client wrapper."""

from __future__ import annotations

from typing import Any, Protocol

from openai import OpenAI

from app.config import Settings, get_settings


class ChatClient(Protocol):
    """Minimal protocol for test doubles."""

    class Chat:
        class Completions:
            def create(self, **kwargs: Any) -> Any: ...

        completions: Completions

    chat: Chat


class LLMService:
    """Wraps OpenAI chat completions for grader and generator nodes."""

    # __init__ - initialise the service with optional settings and client
    def __init__(
        self,
        settings: Settings | None = None,
        client: ChatClient | None = None,
    ) -> None:
        self.settings = settings or get_settings()
        self._client = client

    # client - return the configured OpenAI client, creating one if needed
    @property
    def client(self) -> ChatClient:
        if self._client is None:
            if not self.settings.openai_api_key:
                raise RuntimeError("OPENAI_API_KEY is not set in the environment.")
            self._client = OpenAI(api_key=self.settings.openai_api_key)
        return self._client

    # chat - send messages to the model and return the assistant text
    def chat(self, messages: list[dict[str, str]], *, temperature: float | None = None) -> str:
        response = self.client.chat.completions.create(
            model=self.settings.openai_model,
            messages=messages,
            temperature=(
                self.settings.llm_temperature if temperature is None else temperature
            ),
        )
        return response.choices[0].message.content or ""
