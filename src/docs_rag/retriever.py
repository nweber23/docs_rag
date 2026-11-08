"""Embed a question and fetch the most similar chunks."""

from collections.abc import Callable

from docs_rag import llm, store
from docs_rag.store import Chunk


def retrieve(
    question: str,
    k: int,
    *,
    embed: Callable[[str], list[float]] = llm.embed_one,
    search: Callable[[list[float], int], list[Chunk]] = store.search,
) -> list[Chunk]:
    """Return up to ``k`` chunks, best match first.

    ``embed`` and ``search`` are injectable so tests can run offline.
    """
    chunks = search(embed(question), k)
    return sorted(chunks, key=lambda c: c.score, reverse=True)
