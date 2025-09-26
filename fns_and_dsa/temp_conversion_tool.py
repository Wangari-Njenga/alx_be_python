# temp_conversion_tool.py

import math

# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5


def convert_to_celsius(fahrenheit):
    """
    Convert Fahrenheit to Celsius using the global conversion factor.
    (Reads the global FAHRENHEIT_TO_CELSIUS_FACTOR.)
    """
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR


def convert_to_fahrenheit(celsius):
    """
    Convert Celsius to Fahrenheit using the global conversion factor.
    (Reads the global CELSIUS_TO_FAHRENHEIT_FACTOR.)
    """
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32


def parse_temperature(temp_str):
    """
    Parse and validate temperature input.
    Raises ValueError("Invalid temperature. Please enter a numeric value.") on failure.
    """
    if temp_str is None:
        raise ValueError("Invalid temperature. Please enter a numeric value.")

    temp_str = temp_str.strip()
    if temp_str == "":
        raise ValueError("Invalid temperature. Please enter a numeric value.")

    try:
        value = float(temp_str)
    except ValueError:
        # Must raise the exact message required
        raise ValueError("Invalid temperature. Please enter a numeric value.")

    # Reject NaN and infinities
    if not math.isfinite(value):
        raise ValueError("Invalid temperature. Please enter a numeric value.")

    return value


def parse_unit(unit_str):
    """
    Normalize and validate unit input.
    Returns 'C' or 'F'. Raises ValueError for invalid unit.
    """
    if unit_str is None:
        raise ValueError("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

    unit = unit_str.strip().lower()
    if unit in ("c", "celsius", "centigrade", "°c", "degc", "degree c", "degrees c"):
        return "C"
    if unit in ("f", "fahrenheit", "°f", "degf", "degree f", "degrees f"):
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
            # Show the numeric inputs/outputs clearly as floats
            print(f"{float(temperature)}°C is {result}°F")
        else:  # unit == "F"
            result = convert_to_celsius(temperature)
            print(f"{float(temperature)}°F is {result}°C")

    except ValueError as e:
        # Print the validation error (includes the exact temperature error message when applicable)
        print(e)


if _name_ == "_main_":
    main()
