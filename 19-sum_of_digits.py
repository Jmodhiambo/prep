#!/usr/bin/env python3
"""Solutions for calculating the digital root of a non-negative integer."""


def digital_root_iterative(n: int) -> int:
    """
    Calculate the digital root of a non-negative integer iteratively.

    The digital root is obtained by repeatedly summing the digits of a
    number until only a single digit remains.

    For example:

        38 -> 3 + 8 -> 11 -> 1 + 1 -> 2

    The algorithm uses two loops.

    The outer loop is responsible for repeatedly calculating the digit
    sum until the result contains only one digit.

    The inner loop extracts each digit from the current number. The
    modulo operator (%) obtains the rightmost digit, while integer
    division (//) removes that digit.

    For example, given 1234:

        1234 % 10 = 4
        1234 // 10 = 123

        123 % 10 = 3
        123 // 10 = 12

        12 % 10 = 2
        12 // 10 = 1

        1 % 10 = 1
        1 // 10 = 0

    Therefore, the digit sum is:

        4 + 3 + 2 + 1 = 10

    The process then repeats:

        10 -> 1 + 0 -> 1

    No list or other growing data structure is required. The digits are
    accumulated directly into digit_sum, which keeps the auxiliary space
    constant.

    Args:
        n: A non-negative integer whose digital root should be calculated.

    Returns:
        The single digit obtained after repeatedly summing the digits of n.

    Raises:
        ValueError: If n is not an integer or if n is negative.

    Complexity:
        Time: O(d), where d is the number of digits in n. Each digit is
            processed during the digit summation.
        Space: O(1), because only a fixed number of integer variables are
            used regardless of the size of n.
    """
    if type(n) is not int or n < 0:
        raise ValueError(
            "The input must be a non-negative integer."
        )

    # A single-digit number is already its own digital root.
    if n < 10:
        return n

    current: int = n

    # Continue until the current value contains only one digit.
    while current >= 10:
        digits_sum: int = 0

        # Extract and add every digit from the current number.
        while current > 0:
            digits_sum += current % 10
            current //= 10

        # Use the digit sum as the number for the next iteration.
        current = digits_sum

    return current


def digital_root_mathematical(n: int) -> int:
    """
    Calculate the digital root using the modulo 9 mathematical property.

    A positive integer and the sum of its digits have the same remainder
    when divided by 9.

    For example:

        38 % 9 = 2

    The digit sum of 38 is:

        3 + 8 = 11

    And:

        11 % 9 = 2

    Continuing the digit reduction:

        11 -> 1 + 1 -> 2

    Therefore, the remainder modulo 9 gives the digital root for numbers
    that are not divisible by 9.

    There is one important exception. A positive number that is divisible
    by 9 has a digital root of 9, not 0.

    For example:

        18 % 9 = 0
        18 -> 1 + 8 -> 9

    Therefore:

        n == 0       -> 0
        n % 9 == 0   -> 9
        otherwise    -> n % 9

    This approach does not need to repeatedly extract digits, so the
    running time and auxiliary space are both constant.

    Args:
        n: A non-negative integer whose digital root should be calculated.

    Returns:
        The digital root of n.

    Raises:
        ValueError: If n is not an integer or if n is negative.

    Complexity:
        Time: O(1), because only a constant number of arithmetic
            operations are performed.
        Space: O(1), because only a fixed number of variables are used.
    """
    if type(n) is not int or n < 0:
        raise ValueError(
            "The input must be a non-negative integer."
        )

    # Zero is a special case because 0 has a digital root of 0.
    if n == 0:
        return 0

    remainder: int = n % 9

    # A positive multiple of 9 has a digital root of 9 rather than 0.
    if remainder == 0:
        return 9

    return remainder


if __name__ == "__main__":
    test_cases: list[int] = [
        0,
        7,
        10,
        38,
        1234,
        9999,
    ]

    for number in test_cases:
        iterative_result: int = digital_root_iterative(number)
        mathematical_result: int = digital_root_mathematical(number)

        print(
            f"{number}: "
            f"iterative={iterative_result}, "
            f"mathematical={mathematical_result}"
        )