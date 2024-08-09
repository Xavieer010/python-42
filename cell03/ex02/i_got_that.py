#!/usr/bin/python3

user_input = input("What are you gonna say? ")

while user_input.strip().upper() != "STOP":
    user_input = input("I got that! Anything else? ")

print("Program has ended.")

