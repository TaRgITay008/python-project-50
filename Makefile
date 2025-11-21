install:
uv sync

test:
uv run pytest

test-coverage:
uv run pytest --cov=hexlet_code

lint:
uv run ruff check hexlet_code tests

format:
uv run ruff format hexlet_code tests

check: lint test

package-install:
uv build && pip install dist/*.whl

.PHONY: install test lint format check package-install
