from docs_rag.answer import NO_ANSWER, answer_question, build_prompt
from docs_rag.retriever import retrieve
from docs_rag.store import Chunk


def test_retrieve_orders_best_first() -> None:
    unordered = [Chunk("low", "a.md", 0.2), Chunk("high", "b.md", 0.9), Chunk("mid", "c.md", 0.5)]
    result = retrieve("q", 3, embed=lambda _: [0.0], search=lambda _e, _k: unordered)
    assert [c.text for c in result] == ["high", "mid", "low"]


def test_prompt_contains_context_and_question() -> None:
    prompt = build_prompt("What is X?", [Chunk("X is a thing.", "x.md", 0.9)])
    assert "X is a thing." in prompt
    assert "x.md" in prompt
    assert "What is X?" in prompt


def test_answer_returns_sources() -> None:
    chunks = [Chunk("Paris is the capital.", "geo.md", 0.9), Chunk("More.", "geo.md", 0.8)]
    result = answer_question(
        "Capital of France?",
        retrieve_fn=lambda _q, _k: chunks,
        chat_fn=lambda _s, _u: "Paris [1]",
    )
    assert result.answer == "Paris [1]"
    assert result.sources == ["geo.md"]


def test_no_relevant_chunks_skips_llm() -> None:
    def fail(_s: str, _u: str) -> str:
        raise AssertionError("LLM must not be called")

    weak = [Chunk("unrelated", "a.md", 0.05)]
    result = answer_question("Anything?", retrieve_fn=lambda _q, _k: weak, chat_fn=fail)
    assert result.answer == NO_ANSWER
    assert result.sources == []


def test_model_says_no_answer_drops_sources() -> None:
    chunks = [Chunk("Something related.", "a.md", 0.9)]
    result = answer_question(
        "Obscure?", retrieve_fn=lambda _q, _k: chunks, chat_fn=lambda _s, _u: NO_ANSWER
    )
    assert result.answer == NO_ANSWER
    assert result.sources == []
