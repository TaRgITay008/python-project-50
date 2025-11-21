install:
uv sync

test:
uv run pytest -vv --color=yes --exitfirst tests

lint:
uv run ruff check hexlet_code tests

build:
@echo "Build complete"

setup: install build
