#!/usr/bin/python3

number1 = int(input("Give me the first number: "))
number2 = int(input("Give me the second number: "))

print("Thank you!")

print(f"{number1} + {number2} = {number1 + number2}")
print(f"{number1} - {number2} = {number1 - number2}")
print(f"{number1} * {number2} = {number1 * number2}")

if number2 != 0:
    print(f"{number1} // {number2} = {number1 // number2}")
else:
    print("Division by zero is not allowed.")

