def introduce(name, age, country="India"):
    return f"My name is {name}, I am {age} years old from {country}."

print(introduce("Ryan", 15))
print(introduce(name="Ryan", age=15, country="Germany"))


def total_sum(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total
print(total_sum(1, 2, 3, 4, 10))

def describe_person(**info):
    for key, value in info.items():
        print(f"{key}: {value}")
describe_person(name="Ryan", hobby="Astronomy", mood="Curious")

def bigger(a, b):
    return a if a > b else b
print (bigger(4,5))

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
print(is_prime(49))


from projects.student_grade_calculator import*
print(student_grade_calculator(4,90,90,99,99))