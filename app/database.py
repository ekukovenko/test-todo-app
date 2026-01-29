"""In-memory database for TODO app."""

from typing import Dict, List, Optional

from app.models import Todo, TodoCreate, TodoUpdate, Priority


class Database:
    """In-memory database for TODOs."""

    def __init__(self):
        self._todos: Dict[int, Todo] = {}
        self._counter = 0

    def create(self, todo_create: TodoCreate) -> Todo:
        """Create a new TODO."""
        self._counter += 1
        todo = Todo(
            id=self._counter,
            title=todo_create.title,
            description=todo_create.description,
            priority=todo_create.priority,
            completed=False,
        )
        self._todos[self._counter] = todo
        return todo

    def get(self, todo_id: int) -> Optional[Todo]:
        """Get a TODO by ID."""
        return self._todos.get(todo_id)

    def get_all(self) -> List[Todo]:
        """Get all TODOs."""
        return list(self._todos.values())

    def update(self, todo_id: int, todo_update: TodoUpdate) -> Optional[Todo]:
        """Update an existing TODO."""
        todo = self._todos.get(todo_id)
        if not todo:
            return None

        update_data = todo_update.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(todo, key, value)
        
        self._todos[todo_id] = todo
        return todo

    def delete(self, todo_id: int) -> bool:
        """Delete a TODO by ID."""
        if todo_id in self._todos:
            del self._todos[todo_id]
            return True
        return False


db = Database()