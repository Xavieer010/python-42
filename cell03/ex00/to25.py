#!/usr/bin/python3

valor = int(input("Enter a number less than 25:"))
if valor > 25:
    print("Error")
else:
    while valor <= 25:
        print(f"Inside the loop, my variable is {valor}")
        valor += 1
