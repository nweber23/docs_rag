import pytest

from docs_rag.chunking import chunk_text


def test_short_text_is_one_chunk() -> None:
    assert chunk_text("hello world", size=100, overlap=10) == ["hello world"]


def test_chunks_respect_size_and_cover_text() -> None:
    text = " ".join(f"word{i}" for i in range(200))
    chunks = chunk_text(text, size=100, overlap=20)
    assert len(chunks) > 1
    assert all(len(c) <= 100 for c in chunks)
    assert chunks[0].startswith("word0")
    assert chunks[-1].endswith("word199")


def test_consecutive_chunks_overlap() -> None:
    text = " ".join(f"w{i}" for i in range(300))
    chunks = chunk_text(text, size=100, overlap=30)
    for a, b in zip(chunks, chunks[1:], strict=False):
        assert b.split()[0] in a  # first word of next chunk was already in previous


def test_prefers_paragraph_boundary() -> None:
    text = "a" * 60 + "\n\n" + "b" * 60
    chunks = chunk_text(text, size=80, overlap=0)
    assert chunks[0] == "a" * 60


def test_invalid_parameters() -> None:
    with pytest.raises(ValueError):
        chunk_text("x", size=0, overlap=0)
    with pytest.raises(ValueError):
        chunk_text("x", size=10, overlap=10)
