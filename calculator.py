def calculate(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '^':
        return num1 ** num2
    elif operator == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero"
    else:
        return "Error: Invalid operator"


history = []


while True:
    operation = input("Enter operation (+,-,*,^,/), 'history' to view history', 'clear' to clear history, or 'exit' to quit: ")
    if operation.lower() == 'exit':
        print("Exiting the calculator. Goodbye!")
        break
    if operation.lower() == 'clear':
        history.clear()
        print("History cleared.")
        continue
    if operation.lower() == 'history':
        if not history:
            print("No calculations yet.")
        else:
            print("Calculation History:")
            for entry in history:
                print(entry)
        continue
    print("DEBUG: operation was", operation)

    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Please enter valid numbers.")
        continue

    result = calculate(num1, num2, operation)

    entry = f"{num1} {operation} {num2} = {result}"
    history.append(entry)

    print("Result:", result)