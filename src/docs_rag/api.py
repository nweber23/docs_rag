"""FastAPI app: POST /ask and GET /health."""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from docs_rag.answer import answer_question
from docs_rag.llm import LLMError

app = FastAPI(title="docs-rag")


class AskRequest(BaseModel):
    question: str = Field(min_length=3, max_length=1000)
    k: int | None = Field(default=None, ge=1, le=20)


class AskResponse(BaseModel):
    answer: str
    sources: list[str]


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/ask", response_model=AskResponse)
def ask(req: AskRequest) -> AskResponse:
    try:
        result = answer_question(req.question, req.k)
    except LLMError as exc:
        raise HTTPException(status_code=502, detail=str(exc)) from exc
    return AskResponse(answer=result.answer, sources=result.sources)
