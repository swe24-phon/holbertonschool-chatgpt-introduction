#!/usr/bin/python3
import sys


def factorial(n):
    """
    Calculate the factorial of a non-negative integer n.

    The factorial of a non-negative integer n is the product of all
    positive integers less than or equal to n. It is denoted by n!.

    Parameters:
    n (int): A non-negative integer whose factorial is to be computed.

    Returns:
    int: The factorial of the input integer n.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


if __name__ == "__main__":
    """
    Main entry point of the script.

    This script calculates the factorial of a number provided as a
    command-line argument and prints the result.

    Usage:
    ./script_name.py <number>

    Example:
    ./script_name.py 5
    """
    f = factorial(int(sys.argv[1]))
    print(f)
