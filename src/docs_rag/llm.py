"""Thin Ollama client: embeddings and chat over its HTTP API."""

import httpx

from docs_rag.config import get_settings

TIMEOUT = httpx.Timeout(300.0)


class LLMError(RuntimeError):
    """The model backend is unreachable or returned an error."""


def _post(path: str, payload: dict[str, object]) -> dict[str, object]:
    url = get_settings().ollama_base_url + path
    try:
        response = httpx.post(url, json=payload, timeout=TIMEOUT)
        response.raise_for_status()
    except httpx.HTTPError as exc:
        raise LLMError(f"Ollama request to {path} failed: {exc}") from exc
    result: dict[str, object] = response.json()
    return result


def embed(texts: list[str]) -> list[list[float]]:
    """Embed several texts in one request."""
    data = _post("/api/embed", {"model": get_settings().embed_model, "input": texts})
    embeddings = data["embeddings"]
    assert isinstance(embeddings, list)
    return [[float(x) for x in vec] for vec in embeddings]


def embed_one(text: str) -> list[float]:
    return embed([text])[0]


def chat(system: str, user: str) -> str:
    """Single-turn chat completion. Temperature 0 for reproducible answers."""
    data = _post(
        "/api/chat",
        {
            "model": get_settings().chat_model,
            "stream": False,
            "options": {"temperature": 0},
            "messages": [
                {"role": "system", "content": system},
                {"role": "user", "content": user},
            ],
        },
    )
    message = data["message"]
    assert isinstance(message, dict)
    return str(message["content"]).strip()
