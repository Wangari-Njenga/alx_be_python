#Prompt user to input two numbers and an operator

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operation = input("Enter the operation(+, -, *, /): ")

#Perform calculation based on the operator using match-case
match operation:
    case "+":
        result = num1 + num2
    case "-":
        result = num1 - num2
    case "*":
        result = num1 * num2
    case "/":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Error! Division by zero."
    
print(f"The result is: {result}")
