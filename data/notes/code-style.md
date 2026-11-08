# Code style guide

- Maximum line length is 100 characters, enforced by ruff.
- All public functions need full type hints. We run mypy in strict mode in CI.
- We pin Python 3.13 for all internal services until the end of the year.
- Docstrings use the plain "summary line, blank line, details" format.
- Commit messages follow Conventional Commits, for example `fix(api): handle empty body`.

## Reviews

Every pull request needs one approving review. Pull requests that touch more than 400
changed lines should be split into smaller ones.
