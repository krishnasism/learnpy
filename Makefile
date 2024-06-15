.PHONY: deps lint format test run


deps:
	pip install -r requirements-dev.txt

lint:
	ruff check

format:
	ruff format

test:
	pytest

run:
	typer src.main run run
