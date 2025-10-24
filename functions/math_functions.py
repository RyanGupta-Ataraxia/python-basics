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
    """Return division of two numbers. Returns None if dividing by zero."""
    if b == 0:
        return None
    return a / b


