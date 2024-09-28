def perform_operation(num1, num2, operation):
    # Dictionary to map operation strings to corresponding functions
    operations = {
        "add": lambda x, y: x + y,
        "subtract": lambda x, y: x - y,
        "multiply": lambda x, y: x * y,
        "divide": lambda x, y: x / y if y != 0 else "Cannot divide by zero"
    }
    
    # Check if the operation is valid
    if operation not in operations:
        return "Not a valid operation"
    
    try:
        # Perform the requested operation
        result = operations[operation](num1, num2)
    except ZeroDivisionError:
        result = "Cannot divide by zero"
    except Exception as e:
        result = f"An error occurred: {str(e)}"
    
    return result
