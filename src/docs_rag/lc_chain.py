"""LangChain variant of retrieval + answering (LCEL).

Same behaviour as retriever.py + answer.py, built from LangChain parts. Storage is still our
own pgvector table: the retriever below just wraps ``store.search``.
"""

import re

from langchain_core.documents import Document
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.retrievers import BaseRetriever
from langchain_core.runnables import RunnableLambda
from langchain_ollama import ChatOllama, OllamaEmbeddings

from docs_rag import store
from docs_rag.answer import NO_ANSWER, SYSTEM_PROMPT, Answer
from docs_rag.config import get_settings


class PgVectorRetriever(BaseRetriever):
    """LangChain retriever backed by our pgvector table."""

    k: int = 5
    min_score: float = 0.4

    def _get_relevant_documents(self, query: str, **_: object) -> list[Document]:
        settings = get_settings()
        embeddings = OllamaEmbeddings(model=settings.embed_model, base_url=settings.ollama_base_url)
        chunks = store.search(embeddings.embed_query(query), self.k)
        return [
            Document(page_content=c.text, metadata={"source": c.source, "score": c.score})
            for c in chunks
            if c.score >= self.min_score
        ]


def _format_context(docs: list[Document]) -> str:
    return "\n\n".join(
        f"[{i}] (source: {d.metadata['source']})\n{d.page_content}" for i, d in enumerate(docs, 1)
    )


def answer_question(question: str, k: int | None = None) -> Answer:
    settings = get_settings()
    docs = PgVectorRetriever(k=k or settings.top_k, min_score=settings.min_score).invoke(question)
    if not docs:
        return Answer(NO_ANSWER, [])

    prompt = ChatPromptTemplate.from_messages(
        [("system", "{system}"), ("human", "Context:\n{context}\n\nQuestion: {question}")]
    )
    llm = ChatOllama(model=settings.chat_model, base_url=settings.ollama_base_url, temperature=0)
    chain = prompt | llm | StrOutputParser() | RunnableLambda(str.strip)
    reply = chain.invoke(
        {"system": SYSTEM_PROMPT, "context": _format_context(docs), "question": question}
    )
    if NO_ANSWER in reply:
        return Answer(NO_ANSWER, [])

    cited = {int(n) for n in re.findall(r"\[(\d+)\]", reply)}
    used = [d for i, d in enumerate(docs, 1) if i in cited] or docs
    return Answer(reply, list(dict.fromkeys(d.metadata["source"] for d in used)))
