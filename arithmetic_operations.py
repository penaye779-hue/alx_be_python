def perform_operation(num1: float, num2: float, operation: str):
    """
    Perform an arithmetic operation between two numbers.
    Supports: add, subtract, multiply, divide.
    """

    operation = operation.lower().strip()

    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 == 0:
            return "Error: Division by zero"
        return num1 / num2
    else:
        return "Error: Invalid operation"
