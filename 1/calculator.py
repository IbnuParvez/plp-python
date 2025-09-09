from typing import Callable, Dict


def add(a: float, b: float) -> float:
    return a + b


def subtract(a: float, b: float) -> float:
    return a - b


def multiply(a: float, b: float) -> float:
    return a * b


def divide(a: float, b: float) -> float:
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b


OPERATIONS: Dict[str, Callable[[float, float], float]] = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def get_float(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")


def get_operation() -> str:
    while True:
        op = input("Enter your preferred operation (+, -, *, /): ").strip()
        if op in OPERATIONS:
            return op
        print("Please choose a valid operation: +, -, *, /")


def main() -> None:
    while True:
        x = get_float("What is your first number? ")
        y = get_float("What is your second number? ")
        operation = get_operation()
        try:
            result = OPERATIONS[operation](x, y)
            print(f"{x} {operation} {y} = {result}")
        except ZeroDivisionError as exc:
            print(exc)

        again = input("Do you want to perform another calculation? (y/n): ").strip().lower()
        if again != "y":
            break


if __name__ == "__main__":
    main()