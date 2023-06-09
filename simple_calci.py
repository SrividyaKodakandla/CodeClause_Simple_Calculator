# -*- coding: utf-8 -*-
"""simple_calci.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/18DwEOpxcVMP3nH52dwmOlqviArm0mw8n
"""

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero!"
    else:
        return x / y


print("Select operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Continue or exit")
choice = input("Enter choice (1-4): ")

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

result = 0

if choice == '1':
    result = add(num1, num2)
    operation = "+"
elif choice == '2':
    result = subtract(num1, num2)
    operation = "-"
elif choice == '3':
    result = multiply(num1, num2)
    operation = "*"
elif choice == '4':
    result = divide(num1, num2)

    

if isinstance(result, float):
    print(f"{num1} {operation} {num2} = {result:.2f}")
else:
    print(result)