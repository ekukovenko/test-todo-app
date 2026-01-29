# TODO App

Simple TODO application for testing AI coding agents.

## Features

- Create, read, update, delete TODOs
- Priority levels (low, medium, high)
- Mark TODOs as completed
- Simple web interface

## Running locally

```bash
# Install dependencies
pip install -e ".[dev]"

# Run the app
uvicorn app.main:app --reload

# Run tests
pytest -v
```

## Docker

```bash
docker-compose up -d
```

App will be available at http://localhost:8000

## API Endpoints

- `GET /api/todos/` - List all TODOs
- `POST /api/todos/` - Create a new TODO
- `GET /api/todos/{id}` - Get a TODO by ID
- `PATCH /api/todos/{id}` - Update a TODO
- `DELETE /api/todos/{id}` - Delete a TODO
