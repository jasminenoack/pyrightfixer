install:
	pip install -e .

dev:
	pip install -e '.[dev]'

test:
	pytest

format:
	black pyrightfixer tests

typecheck:
	pyright pyrightfixer

clean:
	rm -rf dist build *.egg-info
