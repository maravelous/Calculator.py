print("Welcome to the Python Calculator!")

num1 = float(input("Enter the first number: "))
op = input("Enter an operation (+, -, *, /): ")
num2 = float(input("Enter the second number: "))

if op == "+":
    print(num1 + num2)
elif op ++ "-":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
elif op == "/":
    if num2 != 0:
        print(num1 / num2)
    else:
        print("Error: Cannot divide by zero.")
else:
    print("Invalid operation.")
