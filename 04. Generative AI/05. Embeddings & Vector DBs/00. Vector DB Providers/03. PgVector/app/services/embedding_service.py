"""OpenAI embedding helpers."""

from __future__ import annotations

from openai import OpenAI


class EmbeddingService:
    def __init__(self, client: OpenAI, model: str) -> None:
        self._client = client
        self._model = model

    def embed_texts(self, texts: list[str]) -> list[list[float]]:
        response = self._client.embeddings.create(model=self._model, input=texts)
        return [item.embedding for item in response.data]

    def embed_query(self, text: str) -> list[float]:
        return self.embed_texts([text])[0]
