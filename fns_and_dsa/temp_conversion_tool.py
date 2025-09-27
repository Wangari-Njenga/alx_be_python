# temp_conversion_tool.py

# --- Global Conversion Factors ---
FAHRENHEIT_FACTOR = 9 / 5
CELSIUS_OFFSET = 32


# --- Conversion Functions ---
def celsius_to_fahrenheit(celsius):
    return (celsius * FAHRENHEIT_FACTOR) + CELSIUS_OFFSET


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - CELSIUS_OFFSET) / FAHRENHEIT_FACTOR


# --- Main Program for User Interaction ---
def main():
    while True:
        print("\nTemperature Conversion Tool")
        print("1. Convert Celsius to Fahrenheit")
        print("2. Convert Fahrenheit to Celsius")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            try:
                celsius = float(input("Enter temperature in Celsius: "))
                fahrenheit = celsius_to_fahrenheit(celsius)
                print(f"{celsius:.2f} Celsius = {fahrenheit:.2f} Fahrenheit")
            except ValueError:
                print("Invalid input")

        elif choice == "2":
            try:
                fahrenheit = float(input("Enter temperature in Fahrenheit: "))
                celsius = fahrenheit_to_celsius(fahrenheit)
                print(f"{fahrenheit:.2f} Fahrenheit = {celsius:.2f} Celsius")
            except ValueError:
                print("Invalid input")

        elif choice == "3":
            break
        else:
            print("Invalid choice")


# Run program
if _name_ == "_main_":
    main()
