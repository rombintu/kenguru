FROM python:3.10-alpine3.17
COPY . .
RUN apk add poetry
RUN poetry install
CMD ["python3", "./cmd/main.py"]