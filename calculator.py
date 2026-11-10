"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""

import math

<<<<<<< HEAD
def square_root(a):
    if a < 0:
        raise ValueError("Input must be a non-negative number")
    return math.sqrt(a)

def hypotenuse(a, b):
    return math.hypot(a, b)
=======
# First example
def add(a, b): 
    return a + b
def sub(a, b):
    return a - b
def mul(a, b):
    return a * b
def div(a, b):
    if a == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return b / a
def log(a, b):
    if b <= 0:
        raise ValueError("Logarithms cannot operate on numbers equal to or less than zero")
    return math.log(b, a)
def exp(a, b):
    return a ** b

import math
>>>>>>> 0962cc854d2e5611befa1118e436cdbb6fd1b634

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

<<<<<<< HEAD
def divide(a, b):
    if a == 0:
        raise ZeroDivisionError("Denominator cannot be zero")
    return b / a

=======
>>>>>>> 0962cc854d2e5611befa1118e436cdbb6fd1b634
def logarithm(a, b):
    if b <= 0:
        raise ValueError("Logarithm base must be greater than zero")
    return math.log(b, a)

def exponent(a, b):
    return a**b

print(square_root(-3))