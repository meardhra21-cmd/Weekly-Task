def calculator():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("1.Add  2.Subtract  3.Multiply  4.Divide")
    ch = int(input("Choose operation: "))

    if ch == 1:
        print("Result:", a + b)
    elif ch == 2:
        print("Result:", a - b)
    elif ch == 3:
        print("Result:", a * b)
    elif ch == 4:
        print("Result:", a / b)
    else:
        print("Invalid choice")


def string_operations():
    s = input("Enter a string: ")
    print("1.Length  2.Uppercase  3.Lowercase")
    ch = int(input("Choose operation: "))

    if ch == 1:
        print("Length:", len(s))
    elif ch == 2:
        print("Uppercase:", s.upper())
    elif ch == 3:
        print("Lowercase:", s.lower())
    else:
        print("Invalid choice")


def number_utilities():
    n = int(input("Enter a number: "))
    print("1.Even/Odd  2.Positive/Negative")
    ch = int(input("Choose operation: "))

    if ch == 1:
        if n % 2 == 0:
            print("Even number")
        else:
            print("Odd number")
    elif ch == 2:
        if n >= 0:
            print("Positive number")
        else:
            print("Negative number")
    else:
        print("Invalid choice")


def main_menu():
    print("\n--- Main Menu ---")
    print("1. Calculator")
    print("2. String Operations")
    print("3. Number Utilities")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        calculator()
    elif choice == 2:
        string_operations()
    elif choice == 3:
        number_utilities()
    else:
        print("Invalid choice")


main_menu()
