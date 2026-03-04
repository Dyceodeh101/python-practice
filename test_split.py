expression = input("Enter calculation:")
parts = expression.split()

num1 = float(parts[0])
operator = parts[1]
num2 = float(parts[2])

print(num1, operator, num2)