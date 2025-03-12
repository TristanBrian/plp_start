# Basic Calculator Program

# Ask the user for input
num1 = float(input("Enter the first number: "))  # Convert input to float for decimal support
operation = input("Enter the operation (+, -, *, /): ")
num2 = float(input("Enter the second number: "))

# Perform the operation based on user input
if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    if num2 == 0:
        result = "Error: Division by zero is not allowed!"
    else:
        result = num1 / num2
else:
    result = "Error: Invalid operation!"

# Display the result
print(f"{num1} {operation} {num2} = {result}")