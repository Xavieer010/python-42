#!/usr/bin/python3

entrada = input("Give me a number: ")

entrada = entrada.replace(',', '.')

try:
    numero = float(entrada)
    
    if '.' in entrada:
        parte_decimal = entrada.split('.')[1]
        if parte_decimal == '0' or parte_decimal == '00':
            print("This number is an integer.")
        else:
            print("This number is a decimal.")
    else:
        print("This number is an integer.")
except ValueError:
    print("The input provided is not a valid number.")

