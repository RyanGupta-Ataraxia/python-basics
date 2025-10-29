from functions.string_functions import *
from functions.list_functions import *
from functions.dictionary_functions import *
from functions.math_functions import*

print("Welcome to Ryan Gupta’s Python Basics Toolkit!")
print("Choose a category:")
print("1. String functions")
print("2. List functions")
print("3. Dictionary functions")
print("4. Math functions")

choice = input("Enter 1, 2,3 or 4: ")

if choice == "1":
    text = input("Enter a string: ")
    print("1. Reverse string")
    print("2. Count vowels")
    print("3. Check palindrome")
    print("4. Capitalize words")
    func = input("Enter your choice: ")

    if func == "1":
        print(reverse_string(text))
    elif func == "2":
        print(count_vowels(text))
    elif func == "3":
        print(is_palindrome(text))
    elif func == "4":
        print(capitalize_words(text))

elif choice == "2":
    nums = input("Enter numbers separated by spaces: ")
    nums = [float(n) for n in nums.split()]
    print("1. Sum list")
    print("2. Average list")
    print("3. Find max")
    print("4. Remove duplicates")
    func = input("Enter your choice: ")

    if func == "1":
        print(sum_list(nums))
    elif func == "2":
        print(average_list(nums))
    elif func == "3":
        print(find_max(nums))
    elif func == "4":
        print(remove_duplicates(nums))

elif choice == "3":
    d1 = {'a': 1, 'b': 2}
    d2 = {'b': 3, 'c': 4}
    print("Merging example dictionaries:", merge_dicts(d1, d2))

elif choice == "4":
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")

    # Validate numeric input (allow floats)
    if not num1.replace('.', '', 1).lstrip('-').isdigit() or not num2.replace('.', '', 1).lstrip('-').isdigit():
        print("Invalid input! Please enter valid numbers (e.g., 12 or 3.5).")
    else:
        num1 = float(num1)
        num2 = float(num2)

        print("1. Add numbers")
        print("2. Subtract numbers")
        print("3. Multiply numbers")
        print("4. Divide numbers")
        func = input("Enter your choice: ")

        if func == "1":
            print(add(num1, num2))
        elif func == "2":
            print(subtract(num1, num2))
        elif func == "3":
            print(multiply(num1, num2))
        elif func == "4":
            print(divide(num1, num2))
        else:
            print("Invalid math choice.")

    

else:
