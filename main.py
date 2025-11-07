
from functions.string_functions import *
from functions.list_functions import *
from functions.dictionary_functions import *
from functions.math_functions import *
from functions.file_functions import *

def main():
    print("Welcome to Ryan Gupta’s Python Basics Toolkit!")
    print("----------------------------------------------")

    while True:
        try:
            print("\nChoose a category:")
            print("1. String functions")
            print("2. List functions")
            print("3. Dictionary functions")
            print("4. Math functions")
            print("5. File functions")
            print("6. Exit")

            choice = input("Enter 1, 2, 3, 4, 5 or 6: ").strip()

            # ---------- STRING FUNCTIONS ----------
            if choice == "1":
                text = input("Enter a string: ").strip()
                print("1. Reverse string")
                print("2. Count vowels")
                print("3. Check palindrome")
                print("4. Capitalize words")
                func = input("Enter your choice: ").strip()

                if func == "1":
                    print(reverse_string(text))
                elif func == "2":
                    print(count_vowels(text))
                elif func == "3":
                    print(is_palindrome(text))
                elif func == "4":
                    print(capitalize_words(text))
                else:
                    print("Invalid string function choice.")

            # ---------- LIST FUNCTIONS ----------
            elif choice == "2":
                nums_input = input("Enter numbers separated by spaces: ").strip()
                try:
                    nums = [float(n) for n in nums_input.split()]
                except ValueError:
                    print("Invalid input. Please enter only numbers.")
                    continue

                print("1. Sum list")
                print("2. Average list")
                print("3. Find max")
                print("4. Remove duplicates")
                func = input("Enter your choice: ").strip()

                if func == "1":
                    print(sum_list(nums))
                elif func == "2":
                    print(average_list(nums))
                elif func == "3":
                    print(find_max(nums))
                elif func == "4":
                    print(remove_duplicates(nums))
                else:
                    print("Invalid list function choice.")

            # ---------- DICTIONARY FUNCTIONS ----------
            elif choice == "3":
                d1 = {'a': 1, 'b': 2}
                d2 = {'b': 3, 'c': 4}
                print("Merging example dictionaries:", merge_dicts(d1, d2))

            # ---------- MATH FUNCTIONS ----------
            elif choice == "4":
                num1 = input("Enter first number: ").strip()
                num2 = input("Enter second number: ").strip()

                try:
                    num1 = float(num1)
                    num2 = float(num2)
                except ValueError:
                    print("Invalid input. Please enter valid numeric values.")
                    continue

                print("1. Add numbers")
                print("2. Subtract numbers")
                print("3. Multiply numbers")
                print("4. Divide numbers")
                func = input("Enter your choice: ").strip()

                if func == "1":
                    print(add(num1, num2))
                elif func == "2":
                    print(subtract(num1, num2))
                elif func == "3":
                    print(multiply(num1, num2))
                elif func == "4":
                    result = divide(num1, num2)
                    if result is not None:
                        print(result)
                else:
                    print("Invalid math function choice.")

            # ---------- FILE FUNCTIONS ----------
            elif choice == "5":
                filename = input("Enter filename: ").strip()
                print("1. Write to file")
                print("2. Read from file")
                print("3. Append to file")
                func = input("Enter your choice: ").strip()

                if func == "1":
                    content = input("Enter content to write: ")
                    write_to_file(filename, content)
                elif func == "2":
                    content = read_from_file(filename)
                    if content is not None:
                        print(content)
                elif func == "3":
                    content = input("Enter content to append: ")
                    append_to_file(filename, content)
                else:
                    print("Invalid file function choice.")

            elif choice == "6":
                print("Thanks for using Ryan Gupta’s Python Toolkit!")
                break

            else:
                print("Invalid category choice. Try again.")

        except Exception as e:
            print(f"Unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
