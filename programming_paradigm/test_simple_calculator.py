from simple_calculator import SimpleCalculator

def main():
    calc = SimpleCalculator()

    print("Welcome to the Simple Calculator!")
    print("Available operations: add, subtract, multiply, divide")

    operation = input("Enter operation: ").strip().lower()
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
    except ValueError:
        print("Error: Please enter numeric values only.")
        return

    if operation == "add":
        result = calc.add(a, b)
    elif operation == "subtract":
        result = calc.subtract(a, b)
    elif operation == "multiply":
        result = calc.multiply(a, b)
    elif operation == "divide":
        result = calc.divide(a, b)
        if result is None:
            print("Error: Cannot divide by zero.")
            return
    else:
        print("Invalid operation.")
        return

    print(f"Result: {result}")

if __name__ == "__main__":
    main()
