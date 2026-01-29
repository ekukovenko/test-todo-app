"""Simple in-memory database for TODOs."""

from app.models import Todo, TodoCreate, TodoUpdate


class TodoDatabase:
    """In-memory TODO storage."""

    def __init__(self):
        self._todos: dict[int, Todo] = {}
        self._counter: int = 0

    def create(self, todo: TodoCreate) -> Todo:
        """Create a new TODO."""
        self._counter += 1
        new_todo = Todo(
            id=self._counter,
            title=todo.title,
            description=todo.description,
            priority=todo.priority,
            completed=False,
        )
        self._todos[new_todo.id] = new_todo
        return new_todo

    def get(self, todo_id: int) -> Todo | None:
        """Get a TODO by ID."""
        return self._todos.get(todo_id)

    def get_all(self) -> list[Todo]:
        """Get all TODOs."""
        return list(self._todos.values())

    def update(self, todo_id: int, todo: TodoUpdate) -> Todo | None:
        """Update a TODO."""
        existing = self._todos.get(todo_id)
        if not existing:
            return None

        update_data = todo.model_dump(exclude_unset=True)
        updated = existing.model_copy(update=update_data)
        self._todos[todo_id] = updated
        return updated

    def delete(self, todo_id: int) -> bool:
        """Delete a TODO."""
        if todo_id in self._todos:
            del self._todos[todo_id]
            return True
        return False


# Global database instance
db = TodoDatabase()
