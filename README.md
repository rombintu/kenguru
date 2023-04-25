## English language learning program

![atl](./assets/kenguru.png)

### Project development 
```bash
pip install poetry # If not install (https://python-poetry.org/)
poetry install # Or try "python3 -m poetry install"
poetry shell # Create .venv and entry to shell
```
### Deploy and Run
```bash
docker build -t kenguru:latest .
docker run -d --name kenguru kenguru:latest
```