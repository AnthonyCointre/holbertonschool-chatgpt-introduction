#!/usr/bin/python3
import sys
"""
factorial - Calculate the factorial of a non-negative integer.
@n: A non-negative integer whose factorial is to be calculated.
Returns: The factorial of the input integer.
"""
def factorial(n):
	if n == 0:
		return 1
	else:
		return n * factorial(n-1)

f = factorial(int(sys.argv[1]))
print(f)
