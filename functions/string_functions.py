# string_functions.py
# Essential string functions for Python Basics

def reverse_string(s):
    """Return the reverse of a string."""
    return s[::-1]

def count_vowels(s):
    """Return the number of vowels in a string."""
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)

def is_palindrome(s):
    """Check if a string is a palindrome."""
    s_clean = ''.join(c.lower() for c in s if c.isalnum())  # ignore case & non-alphanum
    return s_clean == s_clean[::-1]

def capitalize_words(s):
    """Capitalize the first letter of each word in a string."""
    return ' '.join(word.capitalize() for word in s.split())
