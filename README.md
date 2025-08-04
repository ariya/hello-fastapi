# Hello, FastAPI

A minimal FastAPI-based server listening on `localhost` port `8000`.

[![Test with Python](https://github.com/ariya/hello-fastapi/actions/workflows/test-python.yml/badge.svg)](https://github.com/ariya/hello-fastapi/actions/workflows/test-python.yml)
[![Test with Podman](https://github.com/ariya/hello-fastapi/actions/workflows/test-podman.yml/badge.svg)](https://github.com/ariya/hello-fastapi/actions/workflows/test-podman.yml)
[![Test with Docker](https://github.com/ariya/hello-fastapi/actions/workflows/test-docker.yml/badge.svg)](https://github.com/ariya/hello-fastapi/actions/workflows/test-docker.yml)

Run with [uv](https://docs.astral.sh/uv/):
```
uv run python -m uvicorn main:app
```

Run with Podman:
```
podman build -t hello-fastapi .
podman run -d -p 8000:8000 hello-fastapi
```

Run with Docker:
```
docker build -t hello-fastapi .
docker run -d -p 8000:8000 hello-fastapi
```