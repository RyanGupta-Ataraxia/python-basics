# math_functions.py
# Essential math functions

def add(a, b):
    """Return the sum of two numbers."""
    return a + b

def subtract(a, b):
    """Return the difference of two numbers."""
    return a - b

def multiply(a, b):
    """Return the product of two numbers."""
    return a * b

def divide(a, b):
    """Safely divide two numbers with error handling."""
    try:
        a, b = float(a), float(b)
        return a / b
    except ValueError:
        return "Error: Please enter valid numbers."
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."

