"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""

import math

def square_root(a):
    if a < 0:
        raise ValueError("Input must be a non-negative number")
    return math.sqrt(a)

def hypotenuse(a, b):
    return math.hypot(a, b)

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if a == 0:
        raise ZeroDivisionError("Denominator cannot be zero")
    return b / a

def logarithm(a, b):
    if b <= 0:
        raise ValueError("Logarithm base must be greater than zero")
    return math.log(b, a)

def exponent(a, b):
    return a**b

print(square_root(-3))