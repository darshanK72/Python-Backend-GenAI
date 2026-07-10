"""OpenAI chat client wrapper."""

from __future__ import annotations

import json
from typing import Any, Protocol

from openai import OpenAI

from app.config import Settings, get_settings
from app.services.token_tracker import TokenTracker


class ChatClient(Protocol):
    """Minimal protocol for test doubles."""

    class Chat:
        class Completions:
            def create(self, **kwargs: Any) -> Any: ...

        completions: Completions

    chat: Chat


class LLMService:
    """Wraps OpenAI chat completions with token tracking."""

    def __init__(
        self,
        settings: Settings | None = None,
        token_tracker: TokenTracker | None = None,
        client: ChatClient | None = None,
        *,
        emit_usage: bool = False,
    ) -> None:
        self.settings = settings or get_settings()
        self.token_tracker = token_tracker or TokenTracker()
        self._client = client
        self.emit_usage = emit_usage

    @property
    def client(self) -> ChatClient:
        if self._client is None:
            if not self.settings.openai_api_key:
                raise RuntimeError("OPENAI_API_KEY is not set in the environment.")
            self._client = OpenAI(api_key=self.settings.openai_api_key)
        return self._client

    def chat(self, messages: list[dict[str, str]], *, temperature: float | None = None) -> str:
        response = self.client.chat.completions.create(
            model=self.settings.openai_model,
            messages=messages,
            temperature=self.settings.extraction_temperature if temperature is None else temperature,
        )
        self.token_tracker.record(response.usage)
        if self.emit_usage:
            print(self.token_tracker.format_last_call(response.usage))
        return response.choices[0].message.content or ""

    def parse_structured(
        self,
        raw_text: str,
        original_messages: list[dict[str, str]],
        *,
        corrective_instruction: str,
    ) -> dict[str, Any]:
        from app.services.json_parser import StructuredParseError, extract_json_block

        try:
            return extract_json_block(raw_text)
        except json.JSONDecodeError:
            retry_messages = original_messages + [
                {"role": "assistant", "content": raw_text},
                {"role": "user", "content": corrective_instruction},
            ]
            retry_text = self.chat(retry_messages)
            try:
                return extract_json_block(retry_text)
            except json.JSONDecodeError as exc:
                raise StructuredParseError(
                    f"Could not parse structured JSON after retry: {exc}",
                ) from exc
