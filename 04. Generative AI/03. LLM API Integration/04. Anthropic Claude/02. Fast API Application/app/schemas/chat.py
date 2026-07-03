"""Request and response models for Claude Messages API."""

from __future__ import annotations

from pydantic import BaseModel, Field


class ChatMessage(BaseModel):
    role: str = Field(description="One of: user, assistant")
    content: str = Field(min_length=1)


class ChatRequest(BaseModel):
    message: str | None = Field(
        default=None,
        description="Single user message (ignored if messages is provided)",
    )
    messages: list[ChatMessage] | None = Field(
        default=None,
        description="Multi-turn user/assistant history",
    )
    system_prompt: str | None = Field(
        default="You are a helpful assistant.",
        description="Claude system parameter (separate from messages)",
    )
    model: str | None = Field(default=None, description="Override default model")
    temperature: float = Field(default=0.7, ge=0.0, le=1.0)
    max_tokens: int = Field(default=512, ge=1, le=8192)


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
    text: str = Field(min_length=1)
    model: str | None = None
    system_prompt: str | None = None


class TokenCountResponse(BaseModel):
    token_count: int
    model: str
    method: str = "anthropic_count_tokens"
