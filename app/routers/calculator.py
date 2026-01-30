from fastapi import APIRouter, HTTPException

router = APIRouter()

@router.get("/calculate/{operation}")
def calculate(operation: str, a: float, b: float):
    """
    Basic calculator with error handling
    Operations: add, subtract, multiply, divide
    Example: /calculate/add?a=5&b=3
    """
    try:
        if operation == "add":
            result = a + b
        elif operation == "subtract":
            result = a - b
        elif operation == "multiply":
            result = a * b
        elif operation == "divide":
            if b == 0:
                raise ValueError("Division by zero")
            result = a / b
        else:
            raise ValueError("Invalid operation")
        
        return {"operation": operation, "result": result}
    
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
