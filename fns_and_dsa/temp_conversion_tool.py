# temp_conversion_tool.py

import os
import math
import inspect
import sys

# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5


def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius using the global conversion factor."""
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR


def convert_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit using the global conversion factor."""
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32


def parse_temperature(temp_str):
    """Parse and validate temperature input."""
    try:
        value = float(temp_str)
    except Exception:
        raise ValueError("Invalid temperature. Please enter a numeric value.")

    if not math.isfinite(value):
        raise ValueError("Invalid temperature. Please enter a numeric value.")

    return value


def parse_unit(unit_str):
    """Normalize and validate unit input."""
    unit = unit_str.strip().lower()
    if unit in ("c", "celsius", "centigrade"):
        return "C"
    if unit in ("f", "fahrenheit"):
        return "F"
    raise ValueError("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")


def main():
    try:
        temp_input = input("Enter the temperature to convert: ")
        temperature = parse_temperature(temp_input)

        unit_input = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")
        unit = parse_unit(unit_input)

        if unit == "C":
            result = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {result}°F")
        else:
            result = convert_to_celsius(temperature)
            print(f"{temperature}°F is {result}°C")

    except ValueError as e:
        print(e)


# ---------------- SELF CHECKS ---------------- #
def run_self_checks():
    filename = _file_

    print("\n--- Running Self-Checks ---")

    # 1. Check if file exists and not empty
    if os.path.exists(filename) and os.path.getsize(filename) > 0:
        print("✔ File exists and is not empty")
    else:
        print("✘ File missing or empty")

    # 2. Check if conversion functions are implemented
    funcs = [convert_to_celsius, convert_to_fahrenheit]
    if all(callable(f) for f in funcs):
        print("✔ Conversion functions implemented")
    else:
        print("✘ Missing conversion functions")

    # 3. Check for user interaction (use of input)
    with open(filename, "r") as f:
        code = f.read()
    if "input(" in code:
        print("✔ User interaction (input) implemented")
    else:
        print("✘ Missing input prompts")

    # 4. Check for ValueError with correct message
    if "Invalid temperature. Please enter a numeric value." in code:
        print("✔ ValueError implemented with correct message")
    else:
        print("✘ Missing or incorrect ValueError message")

    print("--- Self-Checks Complete ---\n")


if _name_ == "_main_":
    # Run self-checks before starting program
    run_self_checks()
    main()
