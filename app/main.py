"""FastAPI TODO Application."""

from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from app.routers import todos, calculator

app = FastAPI(
    title="TODO App",
    description="Simple TODO application for testing AI coding agents",
    version="0.1.0",
)

# Include routers
app.include_router(todos.router, prefix="/api")
app.include_router(calculator.router, prefix="/api")

# Serve static files
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
def read_root():
    """Serve the main page."""
    return FileResponse("static/index.html")


@app.get("/health")
def health_check():
    """Health check endpoint."""
    return {"status": "healthy"}
