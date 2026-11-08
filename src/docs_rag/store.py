"""PostgreSQL + pgvector storage."""

from dataclasses import dataclass

import psycopg
from pgvector.psycopg import register_vector

from docs_rag.config import get_settings


@dataclass(frozen=True)
class Chunk:
    text: str
    source: str
    score: float = 0.0  # cosine similarity, 1.0 = identical direction


def connect() -> psycopg.Connection:
    settings = get_settings()
    conn = psycopg.connect(settings.database_url, autocommit=True)
    conn.execute("CREATE EXTENSION IF NOT EXISTS vector")
    register_vector(conn)
    return conn


def init_schema(conn: psycopg.Connection) -> None:
    dim = get_settings().embed_dim
    conn.execute(
        f"""
        CREATE TABLE IF NOT EXISTS chunks (
            id SERIAL PRIMARY KEY,
            source TEXT NOT NULL,
            position INT NOT NULL,
            text TEXT NOT NULL,
            embedding vector({dim}) NOT NULL
        )
        """
    )


def reset(conn: psycopg.Connection) -> None:
    """Drop all chunks so ingestion is idempotent."""
    conn.execute("DROP TABLE IF EXISTS chunks")
    init_schema(conn)


def add_chunks(
    conn: psycopg.Connection, source: str, texts: list[str], embeddings: list[list[float]]
) -> None:
    rows = [(source, i, t, e) for i, (t, e) in enumerate(zip(texts, embeddings, strict=True))]
    with conn.cursor() as cur:
        cur.executemany(
            "INSERT INTO chunks (source, position, text, embedding) VALUES (%s, %s, %s, %s)",
            rows,
        )


def search(embedding: list[float], k: int) -> list[Chunk]:
    """Top-k chunks by cosine similarity (pgvector ``<=>`` is cosine distance)."""
    with connect() as conn:
        rows = conn.execute(
            """
            SELECT text, source, 1 - (embedding <=> %s::vector) AS score
            FROM chunks
            ORDER BY embedding <=> %s::vector
            LIMIT %s
            """,
            (embedding, embedding, k),
        ).fetchall()
    return [Chunk(text=r[0], source=r[1], score=float(r[2])) for r in rows]
