import uvicorn

from datetime import datetime
from fastapi import FastAPI
from fastapi.responses import PlainTextResponse, HTMLResponse
from fastapi.routing import APIRoute


def custom_generate_unique_id(route: APIRoute) -> str:
    tag = route.tags[0] if route.tags else "no-tag"
    return f"{tag}-{route.name}"


app = FastAPI(
    title="Hello FastAPI",
    version="0.1.0",
    openapi_url="/openapi.json",
    docs_url="/docs",
    redoc_url="/redoc",
    generate_unique_id_function=custom_generate_unique_id,
)


@app.get("/", response_class=HTMLResponse)
async def read_root():
    return HTMLResponse(content="<h1>Hello, FastAPI!</h1>", status_code=200)


@app.get("/health")
def health():
    return PlainTextResponse(content=f"OK {int(datetime.now().timestamp())}")


uvicorn.run(app, host="0.0.0.0", port=8000)
