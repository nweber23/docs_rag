.PHONY: up down ingest ask test eval lint serve

UV ?= uv

up:
	docker compose up -d --wait
	docker compose exec ollama ollama pull nomic-embed-text
	docker compose exec ollama ollama pull llama3.2:3b

down:
	docker compose down

ingest:
	$(UV) run python -m docs_rag.ingest

# usage: make ask Q="How do I ...?"
ask:
	$(UV) run python -m docs_rag.ask "$(Q)"

serve:
	$(UV) run uvicorn docs_rag.api:app --reload

test:
	$(UV) run pytest

eval:
	$(UV) run python scripts/evaluate.py

lint:
	$(UV) run ruff check .
	$(UV) run ruff format --check .
	$(UV) run mypy src
