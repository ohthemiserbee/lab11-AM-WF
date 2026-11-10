"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""

import math

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

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def logarithm(a, b):
    if b <= 0:
        raise ValueError
    else:    
        return math.log(b, a)

def exponent(a, b):
    return a**b

print(divide(0, 2))
print(logarithm(2, 0))