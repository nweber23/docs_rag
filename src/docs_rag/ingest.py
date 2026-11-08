"""CLI: read Markdown files, chunk them, embed them, store them."""

from pathlib import Path
from typing import Annotated

import typer

from docs_rag import llm, store
from docs_rag.chunking import chunk_text
from docs_rag.config import get_settings

app = typer.Typer(add_completion=False)
BATCH = 32


@app.command()
def ingest(
    data_dir: Annotated[Path, typer.Option(help="Folder with .md files")] = Path("data"),
    chunk_size: Annotated[int | None, typer.Option(help="Characters per chunk")] = None,
    chunk_overlap: Annotated[int | None, typer.Option(help="Overlap between chunks")] = None,
) -> None:
    settings = get_settings()
    size = chunk_size or settings.chunk_size
    overlap = settings.chunk_overlap if chunk_overlap is None else chunk_overlap

    files = sorted(data_dir.rglob("*.md"))
    if not files:
        typer.echo(f"No .md files in {data_dir}", err=True)
        raise typer.Exit(1)

    conn = store.connect()
    store.reset(conn)
    total = 0
    for path in files:
        source = path.relative_to(data_dir).as_posix()
        chunks = chunk_text(path.read_text(encoding="utf-8"), size, overlap)
        embeddings: list[list[float]] = []
        for i in range(0, len(chunks), BATCH):
            embeddings += llm.embed(chunks[i : i + BATCH])
        store.add_chunks(conn, source, chunks, embeddings)
        total += len(chunks)
        typer.echo(f"{source}: {len(chunks)} chunks")
    typer.echo(f"Done: {len(files)} files, {total} chunks")


if __name__ == "__main__":
    app()
