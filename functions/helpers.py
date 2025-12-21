def square(num):
    return num * num

def cube(num):
    return num ** 3

def is_even(num):
    return num % 2 == 0

def is_odd(num):
    return num % 2 != 0

def simple_interest(p, r, t):
    return (p * r * t) / 100

def percentage(part, whole):
    if whole == 0:
        return None
    return (part / whole) * 100

def celsius_to_fahrenheit(c):
    """Converts Celsius to Fahrenheit."""
    return (c * 9 / 5) + 32

def is_prime(n):
    """Returns True if number is prime, else False."""
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
