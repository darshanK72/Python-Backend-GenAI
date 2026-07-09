"""Request and response models for chat endpoints."""

from __future__ import annotations

from pydantic import BaseModel, Field


class ChatMessage(BaseModel):
    role: str = Field(description="One of: system, user, assistant")
    content: str = Field(min_length=1)


class ChatRequest(BaseModel):
    message: str | None = Field(
        default=None,
        description="Single user message (ignored if messages is provided)",
    )
    messages: list[ChatMessage] | None = Field(
        default=None,
        description="Full conversation history for multi-turn chat",
    )
    system_prompt: str | None = Field(
        default="You are a helpful assistant.",
        description="System instruction when using a single message",
    )
    model: str | None = Field(default=None, description="Override default model")
    temperature: float = Field(default=0.7, ge=0.0, le=2.0)
    max_tokens: int = Field(default=512, ge=1, le=4096)


class UsageInfo(BaseModel):
    prompt_tokens: int
    completion_tokens: int
    total_tokens: int


class ChatResponse(BaseModel):
    content: str
    model: str
    finish_reason: str | None = None
    usage: UsageInfo | None = None


class TokenCountRequest(BaseModel):
    text: str = Field(min_length=1, description="Text to count before sending to the API")
    model: str | None = Field(default=None, description="Model used to pick the tiktoken encoding")


class TokenCountResponse(BaseModel):
    token_count: int
    model: str
    encoding: str
