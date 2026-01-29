import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles

from app.routers import todos

logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Context manager for managing the lifespan of the FastAPI application.
    """
    logger.info("Application startup event")
    yield
    logger.info("Application shutdown event")


app = FastAPI(
    title="TODO App",
    description="A simple TODO app with FastAPI and a in-memory database.",
    version="0.1.0",
    lifespan=lifespan,
)

app.include_router(todos.router)
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
async def root() -> RedirectResponse:
    """
    Redirects the root URL to the static index.html file.
    """
    return RedirectResponse(url="/static/index.html")


@app.get("/health")
async def health_check() -> dict[str, str]:
    """
    Health check endpoint to verify the API is running.
    """
    logging.info("Health check called")
    return {"status": "healthy"}