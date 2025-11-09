"""
Problem: Factorial of a Number
Difficulty: Easy
"""

"""This is math.factorial wrapper implementation."""
# import math

# def factorial(n: int) -> int:
#     # simple wrapper around math.factorial for now
#     return math.factorial(n)

def factorial(n):
    res = 1
    for i in range(2, n + 1):
        res *= i
    return res

if __name__ == "__main__":
    print(factorial(5))
