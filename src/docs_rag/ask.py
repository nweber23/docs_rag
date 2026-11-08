"""CLI: ask one question from the terminal."""

import sys

from docs_rag.answer import answer_question


def main() -> None:
    if len(sys.argv) < 2:
        sys.exit('usage: python -m docs_rag.ask "your question"')
    result = answer_question(" ".join(sys.argv[1:]))
    print(result.answer)
    if result.sources:
        print("Sources:", ", ".join(result.sources))


if __name__ == "__main__":
    main()
