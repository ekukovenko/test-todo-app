"""Tests for TODO API."""

import pytest

from fastapi.testclient import TestClient

from app.database import db
from app.main import app


@pytest.fixture(autouse=True)
def reset_db():
    """Reset database before each test."""
    db._todos.clear()
    db._counter = 0
    yield


@pytest.fixture
def client():
    """Test client fixture."""
    return TestClient(app)


class TestCreateTodo:
    """Tests for POST /api/todos."""

    def test_create_todo_success(self, client):
        """Should create a new TODO."""
        response = client.post(
            "/api/todos/",
            json={"title": "Buy groceries", "priority": "high"},
        )
        assert response.status_code == 201
        data = response.json()
        assert data["id"] == 1
        assert data["title"] == "Buy groceries"
        assert data["priority"] == "high"
        assert data["completed"] is False

    def test_create_todo_default_priority(self, client):
        """Should use medium priority by default."""
        response = client.post("/api/todos/", json={"title": "Test task"})
        assert response.status_code == 201
        assert response.json()["priority"] == "medium"

    def test_create_todo_empty_title(self, client):
        """Should reject empty title."""
        response = client.post("/api/todos/", json={"title": ""})
        assert response.status_code == 422


class TestListTodos:
    """Tests for GET /api/todos."""

    def test_list_empty(self, client):
        """Should return empty list."""
        response = client.get("/api/todos/")
        assert response.status_code == 200
        assert response.json() == []

    def test_list_with_todos(self, client):
        """Should return all TODOs."""
        client.post("/api/todos/", json={"title": "Task 1"})
        client.post("/api/todos/", json={"title": "Task 2"})

        response = client.get("/api/todos/")
        assert response.status_code == 200
        assert len(response.json()) == 2


class TestGetTodo:
    """Tests for GET /api/todos/{id}."""

    def test_get_existing(self, client):
        """Should return existing TODO."""
        client.post("/api/todos/", json={"title": "Test"})
        response = client.get("/api/todos/1")
        assert response.status_code == 200
        assert response.json()["title"] == "Test"

    def test_get_not_found(self, client):
        """Should return 404 for non-existing TODO."""
        response = client.get("/api/todos/999")
        assert response.status_code == 404


class TestUpdateTodo:
    """Tests for PATCH /api/todos/{id}."""

    def test_update_title(self, client):
        """Should update TODO title."""
        client.post("/api/todos/", json={"title": "Old title"})
        response = client.patch("/api/todos/1", json={"title": "New title"})
        assert response.status_code == 200
        assert response.json()["title"] == "New title"

    def test_mark_completed(self, client):
        """Should mark TODO as completed."""
        client.post("/api/todos/", json={"title": "Test"})
        response = client.patch("/api/todos/1", json={"completed": True})
        assert response.status_code == 200
        assert response.json()["completed"] is True

    def test_update_not_found(self, client):
        """Should return 404 for non-existing TODO."""
        response = client.patch("/api/todos/999", json={"title": "Test"})
        assert response.status_code == 404


class TestDeleteTodo:
    """Tests for DELETE /api/todos/{id}."""

    def test_delete_existing(self, client):
        """Should delete existing TODO."""
        client.post("/api/todos/", json={"title": "Test"})
        response = client.delete("/api/todos/1")
        assert response.status_code == 204

        # Verify deleted
        response = client.get("/api/todos/1")
        assert response.status_code == 404

    def test_delete_not_found(self, client):
        """Should return 404 for non-existing TODO."""
        response = client.delete("/api/todos/999")
        assert response.status_code == 404
