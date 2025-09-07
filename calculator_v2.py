import random
import math

zero_messages = [
    "Error: Division by zero is forbidden!",
    "Uh oh, dividing by zero tears a hole in the universe.",
    "Nice try — you can’t divide by zero 😅",
    "Dividing by zero? Not on my watch!",
    "Infinity is a cool concept, but not valid math here."
]

print("Welcome to Calculator 2.0!")
expression = input("Enter your math expression: ")

allowed_names = {}
allowed_names.update(math.__dict__)  # allow math functions

try:
    result = eval(expression, {"__builtins__": None}, allowed_names)
    print("Result:", result)
except ZeroDivisionError:
    print(random.choice(zero_messages))
except Exception as e:
    print("Error:", e)