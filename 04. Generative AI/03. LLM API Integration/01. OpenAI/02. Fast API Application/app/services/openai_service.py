"""OpenAI Chat Completions wrapper — chat, streaming, retries, and errors."""

from __future__ import annotations

import time
from collections.abc import Iterator

from openai import APIConnectionError, APIStatusError, OpenAI, RateLimitError

from app.config import Settings
from app.schemas.chat import ChatRequest, ChatResponse, UsageInfo


class OpenAIService:
    def __init__(self, client: OpenAI, settings: Settings) -> None:
        self._client = client
        self._settings = settings

    def _build_messages(self, payload: ChatRequest) -> list[dict[str, str]]:
        if payload.messages:
            return [m.model_dump() for m in payload.messages]

        messages: list[dict[str, str]] = []
        if payload.system_prompt:
            messages.append({"role": "system", "content": payload.system_prompt})
        if not payload.message:
            raise ValueError("Either message or messages must be provided")
        messages.append({"role": "user", "content": payload.message})
        return messages

    def _model(self, payload: ChatRequest) -> str:
        return payload.model or self._settings.openai_model

    def _create_completion(self, **kwargs):
        """Call chat.completions.create with exponential backoff on rate limits."""
        max_retries = self._settings.openai_max_retries
        for attempt in range(max_retries):
            try:
                return self._client.chat.completions.create(**kwargs)
            except RateLimitError:
                if attempt == max_retries - 1:
                    raise
                time.sleep(2**attempt)
        raise RuntimeError("Max retries exceeded")

    def chat(self, payload: ChatRequest) -> ChatResponse:
        response = self._create_completion(
            model=self._model(payload),
            messages=self._build_messages(payload),
            temperature=payload.temperature,
            max_tokens=payload.max_tokens,
        )
        choice = response.choices[0]
        usage = None
        if response.usage:
            usage = UsageInfo(
                prompt_tokens=response.usage.prompt_tokens,
                completion_tokens=response.usage.completion_tokens,
                total_tokens=response.usage.total_tokens,
            )
        return ChatResponse(
            content=choice.message.content or "",
            model=response.model,
            finish_reason=choice.finish_reason,
            usage=usage,
        )

    def stream_tokens(self, payload: ChatRequest) -> Iterator[str]:
        stream = self._create_completion(
            model=self._model(payload),
            messages=self._build_messages(payload),
            temperature=payload.temperature,
            max_tokens=payload.max_tokens,
            stream=True,
        )
        for chunk in stream:
            delta = chunk.choices[0].delta
            if delta.content:
                yield delta.content

    @staticmethod
    def map_openai_error(exc: Exception) -> tuple[int, str]:
        if isinstance(exc, RateLimitError):
            return 429, "OpenAI rate limit exceeded. Try again shortly."
        if isinstance(exc, APIConnectionError):
            return 502, "Could not connect to OpenAI. Check network and base URL."
        if isinstance(exc, APIStatusError):
            return exc.status_code or 502, exc.message
        if isinstance(exc, ValueError):
            return 422, str(exc)
        return 500, "Unexpected error while calling OpenAI."
