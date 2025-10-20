# list_functions.py
# Essential list functions for Python Basics

def sum_list(numbers):
    """Return the sum of all numbers in the list."""
    return sum(numbers)

def average_list(numbers):
    """Return the average (mean) of the numbers in the list."""
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

def find_max(numbers):
    """Return the maximum number in the list."""
    return max(numbers)

def remove_duplicates(lst):
    """Return a new list with duplicates removed, preserving order."""
    result = []
    for item in lst:
        if item not in result:
            result.append(item)
    return result
