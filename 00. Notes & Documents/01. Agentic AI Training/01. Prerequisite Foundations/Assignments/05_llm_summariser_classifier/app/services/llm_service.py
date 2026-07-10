"""OpenAI-backed summarise and classify operations."""

from __future__ import annotations

import json
from typing import Any, Protocol

from fastapi import HTTPException
from openai import OpenAI
from pydantic import ValidationError

from app.config import Settings, get_settings
from app.schemas.llm import ClassifyResult, SummariseResult
from app.schemas.prompts import (
    CLASSIFY_CORRECTIVE_HINT,
    CLASSIFY_SYSTEM_PROMPT,
    SUMMARISE_CORRECTIVE_HINT,
    SUMMARISE_SYSTEM_PROMPT,
)
from app.services.json_parser import LLMJsonParseError, extract_json_block


class ChatClient(Protocol):
    """Minimal protocol for test doubles."""

    class Chat:
        class Completions:
            def create(self, **kwargs: Any) -> Any: ...

        completions: Completions

    chat: Chat


class LLMService:
    """Wraps structured LLM calls for summarise and classify."""

    def __init__(
        self,
        settings: Settings | None = None,
        client: ChatClient | None = None,
    ) -> None:
        self.settings = settings or get_settings()
        self._client = client

    @property
    def client(self) -> ChatClient:
        if self._client is None:
            if not self.settings.openai_api_key:
                raise HTTPException(status_code=502, detail="OpenAI API key is not configured.")
            self._client = OpenAI(api_key=self.settings.openai_api_key)
        return self._client

    def _chat(self, messages: list[dict[str, str]]) -> str:
        response = self.client.chat.completions.create(
            model=self.settings.openai_model,
            messages=messages,
            temperature=self.settings.llm_temperature,
        )
        return response.choices[0].message.content or ""

    def _chat_json(
        self,
        messages: list[dict[str, str]],
        *,
        corrective_hint: str,
    ) -> dict[str, Any]:
        raw = self._chat(messages)
        try:
            return extract_json_block(raw)
        except json.JSONDecodeError:
            retry_messages = messages + [
                {"role": "assistant", "content": raw},
                {"role": "user", "content": corrective_hint},
            ]
            retry_raw = self._chat(retry_messages)
            try:
                return extract_json_block(retry_raw)
            except json.JSONDecodeError as exc:
                raise LLMJsonParseError("LLM returned invalid JSON after retry.") from exc

    def summarise_text(self, text: str) -> SummariseResult:
        """Return a concise summary and word count for the given text."""
        messages = [
            {"role": "system", "content": SUMMARISE_SYSTEM_PROMPT},
            {"role": "user", "content": text},
        ]
        try:
            payload = self._chat_json(messages, corrective_hint=SUMMARISE_CORRECTIVE_HINT)
            return SummariseResult(**payload)
        except LLMJsonParseError as exc:
            raise HTTPException(status_code=502, detail=str(exc)) from exc
        except ValidationError as exc:
            raise HTTPException(
                status_code=502,
                detail="LLM returned invalid summary fields.",
            ) from exc

    def classify_text(self, text: str) -> ClassifyResult:
        """Classify text into bug, feature, question, or feedback."""
        messages = [
            {"role": "system", "content": CLASSIFY_SYSTEM_PROMPT},
            {"role": "user", "content": text},
        ]
        try:
            payload = self._chat_json(messages, corrective_hint=CLASSIFY_CORRECTIVE_HINT)
            return ClassifyResult(**payload)
        except LLMJsonParseError as exc:
            raise HTTPException(status_code=502, detail=str(exc)) from exc
        except ValidationError as exc:
            raise HTTPException(
                status_code=502,
                detail="LLM returned an invalid classification.",
            ) from exc
