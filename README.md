## English language learning program

![atl](./assets/kenguru.png)

### Project development 
```bash
pip install poetry # If not install (https://python-poetry.org/)
poetry install # Or try "python3 -m poetry install"
poetry shell # Create .venv and entry to shell

coding...

# Commit
make commit # Linux/MacOS
change 'version' in pyproject.toml # Windows
```

### Deploy and Run
```bash
docker build -t kenguru:latest .
docker run -d --name kenguru kenguru:latest
```