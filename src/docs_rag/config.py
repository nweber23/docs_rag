"""Settings read from environment variables (or a local .env file)."""

from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    llm_provider: str = "ollama"
    ollama_base_url: str = "http://localhost:11434"
    embed_model: str = "nomic-embed-text"
    chat_model: str = "llama3.2:3b"
    embed_dim: int = 768

    database_url: str = "postgresql://rag:rag@localhost:5432/rag"

    chunk_size: int = 800
    chunk_overlap: int = 150
    top_k: int = 5
    # Chunks with cosine similarity below this are treated as "not relevant".
    min_score: float = 0.4


@lru_cache
def get_settings() -> Settings:
    return Settings()
