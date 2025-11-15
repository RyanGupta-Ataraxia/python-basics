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
