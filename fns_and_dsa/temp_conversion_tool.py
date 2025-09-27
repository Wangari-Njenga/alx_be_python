# temp_conversion_tool.py

# --- Global Conversion Factors ---
FAHRENHEIT_FACTOR = 9 / 5
CELSIUS_OFFSET = 32


# --- Conversion Functions ---
def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit using global factors."""
    return (celsius * FAHRENHEIT_FACTOR) + CELSIUS_OFFSET


def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius using global factors."""
    return (fahrenheit - CELSIUS_OFFSET) / FAHRENHEIT_FACTOR


# --- Main Program for User Interaction ---
def main():
    print("Welcome to the Temperature Conversion Tool!")

    while True:
        print("\nChoose an option:")
        print("1. Convert Celsius to Fahrenheit")
        print("2. Convert Fahrenheit to Celsius")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ").strip()

        if choice == "1":
            try:
                celsius = float(input("Enter temperature in Celsius: "))
                fahrenheit = celsius_to_fahrenheit(celsius)
                print(f"{celsius:.2f}°C = {fahrenheit:.2f}°F")
            except ValueError:
                print("❌ Invalid input! Please enter a numeric value.")

        elif choice == "2":
            try:
                fahrenheit = float(input("Enter temperature in Fahrenheit: "))
                celsius = fahrenheit_to_celsius(fahrenheit)
                print(f"{fahrenheit:.2f}°F = {celsius:.2f}°C")
            except ValueError:
                print("❌ Invalid input! Please enter a numeric value.")

        elif choice == "3":
            print("Goodbye! 👋")
            break

        else:
            print("❌ Invalid choice! Please enter 1, 2, or 3.")


# Run the program only if this file is executed directly
if _name_ == "_main_":
    main()
