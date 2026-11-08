"""Retrieval evaluation: hit@k for k = 1, 3, 5.

A question is a "hit@k" if the expected source file appears among the sources
of the top-k retrieved chunks. Only retrieval is measured, the LLM is not used.
"""

import json
from pathlib import Path

from docs_rag.retriever import retrieve

KS = (1, 3, 5)
QUESTIONS = Path("eval/questions.json")
RESULTS = Path("eval/results.md")


def main() -> None:
    items = json.loads(QUESTIONS.read_text(encoding="utf-8"))
    hits = dict.fromkeys(KS, 0)
    missed: list[str] = []
    for item in items:
        # Retrieve once with the largest k, then check prefixes.
        ranked = [c.source for c in retrieve(item["question"], max(KS))]
        for k in KS:
            if item["source"] in ranked[:k]:
                hits[k] += 1
        if item["source"] not in ranked:
            missed.append(f"- {item['question']} (expected `{item['source']}`)")

    total = len(items)
    lines = ["| k | hits | hit@k |", "|---|------|-------|"]
    for k in KS:
        lines.append(f"| {k} | {hits[k]}/{total} | {hits[k] / total:.0%} |")
    table = "\n".join(lines)
    print(table)

    report = f"# Evaluation results\n\n{total} questions, retrieval only.\n\n{table}\n"
    if missed:
        report += "\nNot found in the top 5:\n\n" + "\n".join(missed) + "\n"
    RESULTS.write_text(report, encoding="utf-8")
    print(f"Wrote {RESULTS}")


if __name__ == "__main__":
    main()
