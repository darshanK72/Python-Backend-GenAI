"""Google Gemini generate_content wrapper."""

from __future__ import annotations

import time
from collections.abc import Iterator
from typing import Any, Callable

from google import genai

from app.config import Settings
from app.schemas.chat import ChatRequest, ChatResponse, UsageInfo


def _is_rate_limit_error(exc: Exception) -> bool:
    msg = str(exc).lower()
    return any(token in msg for token in ("429", "resource exhausted", "quota"))


def _is_auth_error(exc: Exception) -> bool:
    msg = str(exc).lower()
    return any(token in msg for token in ("401", "permission denied", "api key", "unauthorized"))


class GeminiService:
    def __init__(self, client: genai.Client, settings: Settings) -> None:
        self._client = client
        self._settings = settings

    def _model(self, payload: ChatRequest) -> str:
        return payload.model or self._settings.gemini_model

    def _role_for_gemini(self, role: str) -> str:
        if role in ("assistant", "model"):
            return "model"
        if role == "user":
            return "user"
        raise ValueError(f"Unsupported role for Gemini: {role}")

    def _build_contents(self, payload: ChatRequest) -> str | list[dict[str, Any]]:
        if payload.messages:
            return [
                {
                    "role": self._role_for_gemini(m.role),
                    "parts": [{"text": m.content}],
                }
                for m in payload.messages
            ]
        if not payload.message:
            raise ValueError("Either message or messages must be provided")
        return payload.message

    def _build_config(self, payload: ChatRequest) -> dict[str, Any]:
        config: dict[str, Any] = {
            "temperature": payload.temperature,
            "max_output_tokens": payload.max_tokens,
        }
        if payload.system_instruction and not payload.messages:
            config["system_instruction"] = payload.system_instruction
        elif payload.system_instruction and payload.messages:
            config["system_instruction"] = payload.system_instruction
        return config

    def _call_with_retry(self, fn: Callable[..., Any], *args, **kwargs):
        max_retries = self._settings.gemini_max_retries
        for attempt in range(max_retries):
            try:
                return fn(*args, **kwargs)
            except Exception as exc:
                if _is_rate_limit_error(exc) and attempt < max_retries - 1:
                    time.sleep(2**attempt)
                    continue
                raise
        raise RuntimeError("Max retries exceeded")

    def _usage_from_response(self, response) -> UsageInfo | None:
        meta = getattr(response, "usage_metadata", None)
        if not meta:
            return None
        return UsageInfo(
            prompt_tokens=meta.prompt_token_count or 0,
            completion_tokens=meta.candidates_token_count or 0,
            total_tokens=meta.total_token_count or 0,
        )

    def chat(self, payload: ChatRequest) -> ChatResponse:
        response = self._call_with_retry(
            self._client.models.generate_content,
            model=self._model(payload),
            contents=self._build_contents(payload),
            config=self._build_config(payload),
        )
        return ChatResponse(
            content=response.text or "",
            model=self._model(payload),
            finish_reason=getattr(response, "finish_reason", None),
            usage=self._usage_from_response(response),
        )

    def stream_tokens(self, payload: ChatRequest) -> Iterator[str]:
        stream = self._call_with_retry(
            self._client.models.generate_content_stream,
            model=self._model(payload),
            contents=self._build_contents(payload),
            config=self._build_config(payload),
        )
        for chunk in stream:
            if chunk.text:
                yield chunk.text

    def count_tokens(self, text: str, model: str) -> int:
        result = self._client.models.count_tokens(model=model, contents=text)
        return result.total_tokens

    @staticmethod
    def map_error(exc: Exception) -> tuple[int, str]:
        if _is_rate_limit_error(exc):
            return 429, "Gemini rate limit or quota exceeded. Try again shortly."
        if _is_auth_error(exc):
            return 401, "Invalid or unauthorized GOOGLE_API_KEY."
        msg = str(exc).lower()
        if "invalid" in msg:
            return 400, str(exc)
        if isinstance(exc, ValueError):
            return 422, str(exc)
        return 500, f"Unexpected error while calling Gemini: {exc}"
