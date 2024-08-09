#!/usr/bin/python3

def print_multiplication_tables():
    i = 0
    while i <= 10:
        print(f"Table de {i}: ", end="")
        j = 0
        while j <= 10:
            print(i * j, end=" ")
            j += 1
        print()
        i += 1

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
        print("none")
    else:
        print_multiplication_tables()
