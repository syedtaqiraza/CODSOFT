def calculate():
    # Prompt user for input
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Choose an operation (+, -, *, /): ")

    # Perform calculation based on operation choice
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        # Check for division by zero
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Error: Division by zero!"
    else:
        result = "Error: Invalid operation!"

    # Display the result
    print("Result:", result)

# Call the function to execute the calculation
calculate()