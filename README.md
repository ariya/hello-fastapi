# Hello, FastAPI

A minimal FastAPI-based server listening on `localhost` port `8000`.

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