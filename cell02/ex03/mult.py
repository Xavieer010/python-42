#!/usr/bin/python3

number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))
number3 = number1 * number2
if number3.is_integer():
    print(f"Result: {int(number3)}")
else:
    print(f"Result: {number3}")
if number3 == 0:
  print("The result is zero")
elif number3 > 0:
  print("The result is positive")
else:
  print("The result is negative")
