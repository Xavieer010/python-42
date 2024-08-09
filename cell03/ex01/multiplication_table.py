#!/usr/bin/python3

try:
    number = int(input("Enter a number: "))
except ValueError:
    print("Error.")
    exit()

print(f"Multiplication table for {number}:")
for i in range(1, 10):
    print(f"{number} x {i} = {number * i}")

