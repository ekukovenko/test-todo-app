import logging

from fastapi import FastAPI
from fastapi.responses import FileResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles

from app.routers import todos

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

app.include_router(todos.router, prefix="/api")

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
async def read_root():
    return RedirectResponse(url="/static/index.html")


@app.get("/health", status_code=200)
async def health_check():
    logger.info("Health check called")
    return {"status": "healthy"}