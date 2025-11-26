<<<<<<< HEAD
# arithmetic_operations.py

def perform_operation(num1, num2, operation):
    """
    Perform basic arithmetic operations on two numbers.

    Parameters:
        num1 (float): First number
        num2 (float): Second number
        operation (str): 'add', 'subtract', 'multiply', or 'divide'

    Returns:
        float or str: Result of the operation, or an error message for invalid operation/division by zero
    """
    operation = operation.strip().lower()  # clean input

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
        return f"Error: Invalid operation '{operation}'"

=======
def perform_operation(num1, num2, operation):
    """
    Performs basic arithmetic operations.
    :param num1: float
    :param num2: float
    :param operation: string ('add', 'subtract', 'multiply', 'divide')
    :return: result of the operation or an error message
    """

    if operation == "add":
        return num1 + num2

    elif operation == "subtract":
        return num1 - num2

    elif operation == "multiply":
        return num1 * num2

    elif operation == "divide":
        # Handle division by zero
        if num2 == 0:
            return "Error: Division by zero is not allowed."
        return num1 / num2

    else:
        return "Error: Invalid operation."
>>>>>>> fa8be54b243c0dc2f52a69156f3935ddaaa7c6f0
