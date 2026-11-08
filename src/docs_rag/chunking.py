"""Split text into overlapping chunks."""


def chunk_text(text: str, size: int, overlap: int) -> list[str]:
    """Split ``text`` into chunks of at most ``size`` characters.

    Consecutive chunks share about ``overlap`` characters so that a sentence cut at a
    boundary still appears whole in one of them. We prefer to cut at a paragraph
    break, then a line break, then a space, instead of in the middle of a word.
    """
    if size <= 0:
        raise ValueError("size must be positive")
    if not 0 <= overlap < size:
        raise ValueError("overlap must be >= 0 and smaller than size")

    text = text.strip()
    chunks: list[str] = []
    start = 0
    while start < len(text):
        end = min(start + size, len(text))
        if end < len(text):
            end = _best_cut(text, end, min_end=start + size // 2)
        piece = text[start:end].strip()
        if piece:
            chunks.append(piece)
        if end >= len(text):
            break
        start = max(end - overlap, start + 1)
    return chunks


def _best_cut(text: str, end: int, min_end: int) -> int:
    """Return a cut position in (min_end, end], preferring natural boundaries."""
    for sep in ("\n\n", "\n", " "):
        pos = text.rfind(sep, min_end, end)
        if pos != -1:
            return pos + len(sep)
    return end
