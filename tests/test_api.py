import pytest
from fastapi.testclient import TestClient

from docs_rag import api
from docs_rag.answer import Answer
from docs_rag.llm import LLMError

client = TestClient(api.app)


def test_health() -> None:
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_ask_ok(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(api, "answer_question", lambda q, k: Answer("42", ["guide.md"]))
    response = client.post("/ask", json={"question": "What is the answer?"})
    assert response.status_code == 200
    assert response.json() == {"answer": "42", "sources": ["guide.md"]}


def test_ask_validation_error() -> None:
    assert client.post("/ask", json={"question": "x"}).status_code == 422
    assert client.post("/ask", json={}).status_code == 422
    assert client.post("/ask", json={"question": "valid?", "k": 0}).status_code == 422


def test_ask_backend_down(monkeypatch: pytest.MonkeyPatch) -> None:
    def boom(q: str, k: int | None) -> Answer:
        raise LLMError("ollama unreachable")

    monkeypatch.setattr(api, "answer_question", boom)
    response = client.post("/ask", json={"question": "Hello there?"})
    assert response.status_code == 502
    assert "ollama" in response.json()["detail"]
