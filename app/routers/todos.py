"""TODO CRUD endpoints."""

from fastapi import APIRouter, HTTPException

from app.database import db
from app.models import Todo, TodoCreate, TodoUpdate

router = APIRouter(prefix="/todos", tags=["todos"])


@router.post("/", response_model=Todo, status_code=201)
def create_todo(todo: TodoCreate) -> Todo:
    """Create a new TODO."""
    return db.create(todo)


@router.get("/", response_model=list[Todo])
def list_todos() -> list[Todo]:
    """List all TODOs."""
    return db.get_all()


@router.get("/{todo_id}", response_model=Todo)
def get_todo(todo_id: int) -> Todo:
    """Get a TODO by ID."""
    todo = db.get(todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="TODO not found")
    return todo


@router.patch("/{todo_id}", response_model=Todo)
def update_todo(todo_id: int, todo: TodoUpdate) -> Todo:
    """Update a TODO."""
    updated = db.update(todo_id, todo)
    if not updated:
        raise HTTPException(status_code=404, detail="TODO not found")
    return updated


@router.delete("/{todo_id}", status_code=204)
def delete_todo(todo_id: int) -> None:
    """Delete a TODO."""
    if not db.delete(todo_id):
        raise HTTPException(status_code=404, detail="TODO not found")
