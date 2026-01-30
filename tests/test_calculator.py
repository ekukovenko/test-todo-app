import pytest
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

# Test cases for calculator operations
@pytest.mark.parametrize("operation, a, b, expected", [
    ("add", 5, 3, 8),
    ("subtract", 10, 4, 6),
    ("multiply", 7, 2, 14),
    ("divide", 15, 3, 5),
])
def test_calculator_operations(operation, a, b, expected):
    """Test valid calculator operations."""
    response = client.get(f"/api/calculate/{operation}?a={a}&b={b}")
    assert response.status_code == 200
    assert response.json() == {"operation": operation, "result": expected}

# Test error cases
@pytest.mark.parametrize("operation, a, b, detail", [
    ("divide", 10, 0, "Division by zero"),
    ("power", 2, 3, "Invalid operation"),
])
def test_calculator_errors(operation, a, b, detail):
    """Test calculator error handling."""
    response = client.get(f"/api/calculate/{operation}?a={a}&b={b}")
    assert response.status_code == 400
    assert response.json()["detail"] == detail

# Test missing parameters
def test_missing_parameters():
    """Test missing query parameters."""
    response = client.get("/api/calculate/add")
    assert response.status_code == 422
