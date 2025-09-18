#A for loop to print the multiplication table of a given number

number = int(input("Enter a number to see its multiplication table: "))

print(f"Multiplication table for {number}:")
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")
