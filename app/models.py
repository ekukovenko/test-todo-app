"""Pydantic models for TODO app."""

from pydantic import BaseModel, Field
from enum import Enum


class Priority(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


class TodoCreate(BaseModel):
    """Schema for creating a new TODO."""

    title: str = Field(..., min_length=1, max_length=200)
    description: str | None = None
    priority: Priority = Priority.MEDIUM


class TodoUpdate(BaseModel):
    """Schema for updating a TODO."""

    title: str | None = Field(None, min_length=1, max_length=200)
    description: str | None = None
    priority: Priority | None = None
    completed: bool | None = None


class Todo(BaseModel):
    """Schema for TODO response."""

    id: int
    title: str
    description: str | None = None
    priority: Priority
    completed: bool = False
