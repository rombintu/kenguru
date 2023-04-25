run:
	python3 cmd/main.py
test_data:
	python3 -m unittest tests/test_translator.py -v
test_store:
	python3 -m unittest tests/test_database.py -v
commit:
	./scripts/commit.sh