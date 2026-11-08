# docs-rag explained

## 1. Chunking and chunk size

An embedding turns a whole text into one vector, so a long document blurs many topics into one
point. We split documents into chunks of 800 characters with 150 characters of overlap, so an
idea cut at a boundary still appears whole in one chunk. Small chunks give precise matches but
lose context (the answer may be in the next chunk). Large chunks keep context but dilute the
vector and fill the prompt with noise. The cut prefers paragraph, line, then word boundaries.
Size and overlap are configurable (`CHUNK_SIZE`, `CHUNK_OVERLAP`, or CLI flags).

Files: `src/docs_rag/chunking.py`, `src/docs_rag/ingest.py`, `src/docs_rag/config.py`,
`tests/test_chunking.py`.

## 2. Embeddings and cosine similarity

An embedding model maps text to a list of 768 numbers so that texts with similar meaning end up
pointing in similar directions. Cosine similarity compares the angle between two vectors and
ignores their length, which is what we want: a short question and a long passage can still be
"about the same thing". Values near 1 mean same direction, near 0 unrelated. pgvector computes
cosine distance with the `<=>` operator; we return `1 - distance` as the score and sort by it.

Files: `src/docs_rag/llm.py` (embed), `src/docs_rag/store.py` (`search`),
`src/docs_rag/retriever.py`.

## 3. Grounding and the "no answer" case

The system prompt tells the model to use only the numbered passages, to cite them, and to reply
with one fixed sentence if the answer is missing. Two code checks back this up. If no retrieved
chunk reaches the minimum similarity (`MIN_SCORE`), the model is never called. If the model
returns the fixed sentence, we return it with no sources. Temperature is 0 so answers are
repeatable. This reduces hallucination but cannot guarantee it, especially with a small model.

Files: `src/docs_rag/answer.py`, `tests/test_answer.py`.

## 4. What hit@k measures

hit@k is the share of questions where the expected source file is among the top k retrieved
chunks. It tells you whether retrieval finds the right place. It does not tell you whether the
answer text is correct, whether the model stayed faithful to the context, or how good the
ranking is beyond "somewhere in the top k". It also depends on the question set: 20 questions
written by the author are easy. It says nothing about questions that have no answer.

Files: `scripts/evaluate.py`, `eval/questions.json`, `eval/results.md`.

## 5. RAG vs. fine-tuning vs. plain prompting

Plain prompting works when everything fits in the context window and rarely changes. RAG is
better when the knowledge is large, changes often, is private, or when you need citations: you
update the index, not the model. Fine-tuning is better for teaching style, format or a skill,
not for adding facts, and it is slow to update. RAG is worse when questions need reasoning over
the whole corpus (summaries, counting), when documents are tiny enough to paste into the prompt,
or when retrieval keeps missing the right passage.

Files: `README.md` (design decisions, limitations), `src/docs_rag/answer.py`.
