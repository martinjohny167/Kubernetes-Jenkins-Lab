#!/usr/bin/env python3

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

if __name__ == "__main__":
    print("Simple Calculator")
    print("Sum: ", add(10, 5))
    print("Difference: ", subtract(10, 5))
    print("Product: ", multiply(10, 5))
    print("Quotient: ", divide(10, 5)) 