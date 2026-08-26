.PHONY: install catalog validate links compile test check

install:
	python -m pip install -r requirements-dev.txt

catalog:
	python scripts/build_catalog.py

validate:
	python scripts/validate_archive.py

links:
	python scripts/check_internal_links.py

compile:
	python -m compileall -q scripts tests

test:
	python -m unittest discover -s tests -v

check: catalog validate links compile test
	git diff --check
