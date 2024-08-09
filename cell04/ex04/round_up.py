#!/usr/bin/python3

import math

entrada = input("Give me a number: ")

entrada = entrada.replace(',', '.')

try:
    numero = float(entrada)
    numero_arredondado = math.ceil(numero)
    print(numero_arredondado)
except ValueError:
    print("Invalid input.")
