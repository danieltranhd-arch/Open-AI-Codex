def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


def main():
    operations = {
        "add": add,
        "subtract": subtract,
        "multiply": multiply,
        "divide": divide,
    }

    print("Simple Calculator")
    print("Available operations: add, subtract, multiply, divide")

    operation = input("Choose an operation: ").strip().lower()
    if operation not in operations:
        print("Invalid operation selected.")
        return

    try:
        first_number = float(input("Enter the first number: "))
        second_number = float(input("Enter the second number: "))
        result = operations[operation](first_number, second_number)
    except ValueError as error:
        print(f"Error: {error}")
        return

    print(f"Result: {result}")


if __name__ == "__main__":
    main()
