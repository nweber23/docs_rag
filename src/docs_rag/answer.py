"""Build a grounded prompt, call the LLM, return answer plus sources."""

from collections.abc import Callable
from dataclasses import dataclass

from docs_rag import llm
from docs_rag.config import get_settings
from docs_rag.retriever import retrieve
from docs_rag.store import Chunk

NO_ANSWER = "I don't know based on the provided documents."

SYSTEM_PROMPT = f"""You answer questions using ONLY the numbered context passages.
Rules:
- If the context does not contain the answer, reply exactly: {NO_ANSWER}
- Do not use outside knowledge and do not guess.
- Be concise. Cite the passages you used like [1] or [2]."""


@dataclass(frozen=True)
class Answer:
    answer: str
    sources: list[str]


def build_prompt(question: str, chunks: list[Chunk]) -> str:
    context = "\n\n".join(f"[{i}] (source: {c.source})\n{c.text}" for i, c in enumerate(chunks, 1))
    return f"Context:\n{context}\n\nQuestion: {question}"


def answer_question(
    question: str,
    k: int | None = None,
    *,
    retrieve_fn: Callable[[str, int], list[Chunk]] = retrieve,
    chat_fn: Callable[[str, str], str] = llm.chat,
) -> Answer:
    settings = get_settings()
    chunks = retrieve_fn(question, k or settings.top_k)
    # Drop weak matches. With nothing relevant left we skip the LLM entirely.
    relevant = [c for c in chunks if c.score >= settings.min_score]
    if not relevant:
        return Answer(NO_ANSWER, [])

    reply = chat_fn(SYSTEM_PROMPT, build_prompt(question, relevant))
    if NO_ANSWER in reply:
        return Answer(NO_ANSWER, [])
    sources = list(dict.fromkeys(c.source for c in relevant))  # unique, ordered
    return Answer(reply, sources)
