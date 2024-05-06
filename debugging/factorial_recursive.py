#!/usr/bin/python3

import sys

def factorial(n):
    """
    Calculate the factorial of a given integer using recursion.
    
    Parameters:
        n (int): The integer for which the factorial is to be calculated.
        
    Returns:
        int: The factorial of the given integer.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Command-line argument handling to retrieve the integer for which factorial is to be calculated
# The first command-line argument is assumed to be the integer for factorial calculation
# Usage: python3 factorial_recursive.py <integer>
# Example: python3 factorial_recursive.py 5
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 factorial_recursive.py <integer>")
        sys.exit(1)

    try:
        # Convert the command-line argument to an integer
        num = int(sys.argv[1])
    except ValueError:
        print("Please provide a valid integer.")
        sys.exit(1)

    # Calculate the factorial of the given integer
    result = factorial(num)
    print(result)
