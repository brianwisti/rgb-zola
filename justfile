serve:
	zola serve

images:
	python scripts/meta.py

build:
	zola build

quality:
	markdownlint './content/blog/**/*.md'

qualitycount:
	markdownlint './content/blog/**/*.md' 2>&1 > /dev/null | wc -l

pip:
	pip install -r requirements.txt

test: build
	pytest tests
