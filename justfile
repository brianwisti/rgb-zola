serve:
	zola serve

images:
	python scripts/meta.py

build:
	zola build

pip:
	pip install -r requirements.txt

test: build
	pytest tests
