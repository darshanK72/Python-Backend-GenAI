"""Anthropic Claude Messages API wrapper."""

from __future__ import annotations

import time
from collections.abc import Iterator

import anthropic
from anthropic import APIConnectionError, APIStatusError, RateLimitError

from app.config import Settings
from app.schemas.chat import ChatRequest, ChatResponse, UsageInfo


class ClaudeService:
    def __init__(self, client: anthropic.Anthropic, settings: Settings) -> None:
        self._client = client
        self._settings = settings

    def _model(self, payload: ChatRequest) -> str:
        return payload.model or self._settings.claude_model

    def _build_messages(self, payload: ChatRequest) -> list[dict[str, str]]:
        if payload.messages:
            return [{"role": m.role, "content": m.content} for m in payload.messages]
        if not payload.message:
            raise ValueError("Either message or messages must be provided")
        return [{"role": "user", "content": payload.message}]

    def _system(self, payload: ChatRequest) -> str | None:
        return payload.system_prompt

    def _create_with_retry(self, **kwargs):
        max_retries = self._settings.claude_max_retries
        for attempt in range(max_retries):
            try:
                return self._client.messages.create(**kwargs)
            except RateLimitError:
                if attempt == max_retries - 1:
                    raise
                time.sleep(2**attempt)
        raise RuntimeError("Max retries exceeded")

    @staticmethod
    def _text_from_message(message) -> str:
        return " ".join(
            block.text for block in message.content if block.type == "text"
        )

    def chat(self, payload: ChatRequest) -> ChatResponse:
        kwargs = {
            "model": self._model(payload),
            "max_tokens": payload.max_tokens,
            "temperature": payload.temperature,
            "messages": self._build_messages(payload),
        }
        if self._system(payload):
            kwargs["system"] = self._system(payload)

        message = self._create_with_retry(**kwargs)
        usage = None
        if message.usage:
            usage = UsageInfo(
                prompt_tokens=message.usage.input_tokens,
                completion_tokens=message.usage.output_tokens,
                total_tokens=message.usage.input_tokens + message.usage.output_tokens,
            )
        return ChatResponse(
            content=self._text_from_message(message),
            model=message.model,
            finish_reason=message.stop_reason,
            usage=usage,
        )

    def stream_tokens(self, payload: ChatRequest) -> Iterator[str]:
        kwargs = {
            "model": self._model(payload),
            "max_tokens": payload.max_tokens,
            "temperature": payload.temperature,
            "messages": self._build_messages(payload),
        }
        if self._system(payload):
            kwargs["system"] = self._system(payload)

        with self._client.messages.stream(**kwargs) as stream:
            yield from stream.text_stream

    def count_tokens(
        self,
        text: str,
        model: str,
        system_prompt: str | None = None,
    ) -> int:
        kwargs = {
            "model": model,
            "messages": [{"role": "user", "content": text}],
        }
        if system_prompt:
            kwargs["system"] = system_prompt
        result = self._client.messages.count_tokens(**kwargs)
        return result.input_tokens

    @staticmethod
    def map_error(exc: Exception) -> tuple[int, str]:
        if isinstance(exc, RateLimitError):
            return 429, "Claude rate limit exceeded. Try again shortly."
        if isinstance(exc, APIConnectionError):
            return 502, "Could not connect to Anthropic. Check network."
        if isinstance(exc, APIStatusError):
            return exc.status_code or 502, exc.message
        if isinstance(exc, ValueError):
            return 422, str(exc)
        return 500, f"Unexpected error while calling Claude: {exc}"
