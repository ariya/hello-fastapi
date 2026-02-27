FROM python:3.11-slim

COPY --from=ghcr.io/astral-sh/uv:0.8.4 /uv /uvx /bin/

ENV PYTHONUNBUFFERED=1
ENV PYTHONFAULTHANDLER=1

WORKDIR /app

COPY main.py pyproject.toml uv.lock* ./

RUN uv sync --no-dev --locked --no-install-project

EXPOSE 8000


CMD ["uv", "run", "main.py"]
