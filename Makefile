run:
	python3 cmd/main.py
test_data:
	python3 -m unittest tests/test_translator.py
commit:
	./scripts/commit.sh