def calculate(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero"
    else:
        return "Error: Invalid operator"

while True:
    operation = input("Enter operation (+,-,*,/) or 'exit' to quit: ")
    if operation.lower() == 'exit':
        print("Exiting the calculator. Goodbye!")
        break
    
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    
    result = calculate(num1, num2, operation)
    print("Result:", result)