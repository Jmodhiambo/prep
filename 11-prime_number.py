#!/usr/bin/env python3
"""
Checks if a number is a Prime Number.
"""

from sys import argv


def is_prime(n: int) -> bool:
    """
    Validatates if the input number is a a Prime Number.
    Args:
        - n (int): Input number
    Return:
        - bool: True if prime number and False if not.
    """
    if not isinstance(n, int) or n < 1:
        raise ValueError("Input must be a positive Integer.")
    
    if n == 1:
        return False
    
    # Return True for all prime numbers under 10
    if n == 2 or n == 3 or n == 5 or n == 7:
        return True
    
    # Return false for all the even numbers above 2 since they cannot be prime
    if n % 2 == 0:
        return False

    for i in range(3, n):
        if n % i != 0:
            continue
        return False
    return True


if __name__ == "__main__":
    try:
        n = int(argv[1])
    except IndexError:
        n = 0
    print(is_prime(n))

# AI Approach
#!/usr/bin/env python3
"""Check if a number is prime."""

from math import isqrt

def is_prime(n: int) -> bool:
    """
    Returns True if n is a prime number, otherwise False.
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False

    # isqrt(n) returns the integer square root of n i.e. isqrt(37) → 6
    for i in range(3, isqrt(n) + 1, 2):
        if n % i == 0:
            return False
    return True


if __name__ == "__main__":
    from sys import argv

    try:
        n = int(argv[1])
        print(is_prime(n))
    except (IndexError, ValueError):
        print("Usage: ./prime.py <positive integer>")
