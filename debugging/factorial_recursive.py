#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculate the factorial of a non-negative integer using recursion.

    Parameters:
        n (int): The non-negative integer for which factorial is to be calculated.

    Returns:
        int: The factorial of the input integer.

    Raises:
        ValueError: If the input integer is negative.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Get the integer input from command-line argument
f = factorial(int(sys.argv[1]))
print(f)
