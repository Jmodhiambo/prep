#!/usr/bin/env python3
"""This function returns the number of trailing zeros in a factorial of a given number."""


def trailing_zeros(n: int) -> int:
    """
    Count the numeber of trailing zeros in the factorial on n
    Arg:
        n: the number to find the factorial and get trailing zeros
    Return:
        the number of zeros in the factorial of n
    """

    if not isinstance(n, int) or n < 0:
        raise ValueError("The input must be a non-negative number.")

    if n == 0:
        return 0

    # Helpler function to get factorial of n
    def get_factorial(num) -> int:
        """Gets the factorial on the number given"""
        if num == 1:
            return 1

        return num * get_factorial(num - 1)

    factorial: int = get_factorial(n)
    zero_count: int = 0

    # Get the count of trailing zero
    while factorial > 0:
        if factorial % 10 == 0:
            zero_count += 1
        else:
            break

        factorial //= 10

    return zero_count


#AI detailed version
#!/usr/bin/env python3
"""Count trailing zeros in the factorial of a number."""


def trailing_zeros(n: int) -> int:
    """
    Return the number of trailing zeros in n!.

    A trailing zero is produced by a factor of 10, and:

        10 = 2 * 5

    Therefore, every trailing zero requires one pair of factors
    consisting of a 2 and a 5.

    In a factorial, there are always more factors of 2 than
    factors of 5. Therefore, the number of trailing zeros is
    determined by the number of factors of 5.

    Multiples of 5 contribute at least one factor of 5:

        5   = 5
        10  = 2 * 5
        15  = 3 * 5

    However, some numbers contain more than one factor of 5:

        25  = 5 * 5
        125 = 5 * 5 * 5
        625 = 5 * 5 * 5 * 5

    Therefore, we count:

        n // 5
        n // 25
        n // 125
        n // 625
        ...

    Each division counts how many multiples of that power of 5
    exist between 1 and n.

    For example, for n = 100:

        100 // 5  = 20
        100 // 25 = 4

    Therefore:

        20 + 4 = 24

    So 100! contains 24 trailing zeros.

    We do not calculate n! itself because factorial values become
    extremely large. Instead, we count the factors of 5 directly.

    Args:
        n: A non-negative integer.

    Returns:
        The number of trailing zeros in n!.

    Raises:
        ValueError: If n is not a non-negative integer.
    """
    if not isinstance(n, int) or n < 0:
        raise ValueError("The input must be a non-negative integer.")

    zero_count = 0
    divisor = 5

    while divisor <= n:
        zero_count += n // divisor
        divisor *= 5

    return zero_count


if __name__ == "__main__":
    print(trailing_zeros(0))      # 0
    print(trailing_zeros(5))      # 1
    print(trailing_zeros(10))     # 2
    print(trailing_zeros(20))     # 4
    print(trailing_zeros(25))     # 6
    print(trailing_zeros(100))    # 24
    print(trailing_zeros(3125))    # 31