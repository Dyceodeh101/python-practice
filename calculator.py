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
    user_input = input("Enter calculation, 'history', 'clear', or 'exit': ").strip()
    if user_input.lower() == 'exit':
        print("Exiting the calculator. Goodbye!")
        break
    if user_input.lower() == 'clear':
        history.clear()
        print("History cleared.")
        continue
    if user_input.lower() == 'history':
        if not history:
            print("No calculations yet.")
        else:
            print("Calculation History:")
            for entry in history:
                print(entry)
        continue

    expr = user_input
    for op in ['+', '-', '*', '/', '^']:
        expr = expr.replace(op, f' {op} ')

    parts = expr.split()

    if len(parts) != 3:
        print("Invalid input format. Please enter in the format: number operator number (e.g., 2 + 3).")
        continue

    
    num1 = float(parts[0])
    operation = parts[1]
    num2 = float(parts[2])
    
    if operation not in ['+', '-', '*', '/', '^']:
        print("Invalid operator. Please use one of the following: +, -, *, /, ^.")
        continue

    result = calculate(num1, num2, operation)

    entry = f"{num1} {operation} {num2} = {result}"
    history.append(entry)

    print("Result:", result)