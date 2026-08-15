#!/usr/bin/env python3
"""This module computes factorial using recursion and iteration"""

def factorial_iterative(n: int) -> int:
    """
    Get the factorial of a number using iteration
    Arg:
        n: the number to find its factorial value
    Return:
        factorial n
    """
    if n < 0:
        raise ValueError("The number must be 0 or greater. Please try again!")

    if n == 0:
        return 1

    factorial: int = 1

    while n > 0:
        factorial *= n

        n -= 1

    return factorial


def factorial_recursive(n: int) -> int:
    """
    Get the factorial of a number using recursion
    Arg:
        n: the number to find its factorial value
    Return:
        factorial n
    """
    if n < 0:
        raise ValueError("The number must be 0 or greater. Please try again!")

    # The base case to end the recursion
    if n == 0 or n == 1:
        return 1

    return n * factorial_recursive(n - 1)


if __name__ == "__main__":
    print(factorial_iterative(5))
    print(factorial_recursive(5))

#AI Version
# The main distinction with mine is that it does not modify the original value of n
def factorial_iterative(n: int) -> int:
    """Return the factorial of n using iteration."""
    if n < 0:
        raise ValueError("n must be non negative.")

    result: int = 1

    for value in range(2, n + 1):
        result *= value

    return result

# The main distinction with mine is that it does not modify the original value of n
# Uses a helper function to avoid negative number validation in every recrusive call.
def factorial_recursive(n: int) -> int:
    """Return the factorial of n using recursion."""
    if n < 0:
        raise ValueError("n must be non negative.")

    def calculate(value: int) -> int:
        if value == 0:
            return 1

        return value * calculate(value - 1)

    return calculate(n)

# Notes
# Iterative:
# Time:  O(n)
# Space: O(1) - We only maintain a fixed number of variables such as result and i. So the auxiliary space is O(1)

# Recursive:
# Time:  O(n)
# Space: O(n) - Each recursive call is stored in stack hence the space complexity is O(n)

# The number of operations determines time complexity. The amount of additional memory that grows with the input determines space complexity.