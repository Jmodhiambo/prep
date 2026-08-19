#!/usr/bin/env python3
"""This function reverses digits of an integer."""

def reverse_digits(n: int) -> int:
    """
    Reverse the digits of the integer n
    Args:
        n: the integer to be reversed
    Returns:
        A reversed n
    Raises:
        A ValueError if n is not an integer
    """

    if type(n) is not int:
        raise ValueError("The input must be a number.")

    is_negative: bool = False
    if n < 0:
        n = abs(n)
        is_negative = True

    reversed_digits: int = 0
    current: int = n

    while current > 0:
        # Increase the 
        reversed_digits *= 10

        # Add the last digit
        reversed_digits += current % 10

        current //= 10

    if is_negative:
        reversed_digits = 0 - reversed_digits

    return reversed_digits


if __name__ == "__main__":
    print(reverse_digits(123))
    print(reverse_digits(-456))
    print(reverse_digits(100))