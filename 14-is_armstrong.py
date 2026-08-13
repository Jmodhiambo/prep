#!/usr/bin/env python3
"""
Find if a number is an Armstrong number.
An Armstrong number is a number that is equal to the sum of its digits,
where each digit is raised to the power of the number of digits in the number.
i.e. 153 = 1^3 + 5^3 + 3^3
"""


def is_armstrong(n: int) -> bool:
    """
    Determine whether n is an Armstrong number.
    Args:
        n: the number to decide if Armstrong
    Return:
        True if Arstrong and False if otherwise
    """

    # Return false for the negative numbers
    if n < 0:
        return False

    if n == 0:
        return True
    
    # Get the string version on n to have length (power) and allow iteration
    str_n: str = str(n)
    power: int = len(str_n)
    total: int = 0

    for digit in str_n:
        total += pow(int(digit), power)

    return n == total

def is_armstrong_2(n: int) -> bool:
    # Return false for the negative numbers
    if n < 0:
        return False

    power: int =  len(str(n))
    total: int = 0
    current_value: int = n

    while n > 1:
        total += pow(n % 10, power)
        n //= 10

        if n < 10:
            total += pow(n, power)
            break

    return current_value == total

if __name__ == "__main__":
    print(is_armstrong(153))
    print(is_armstrong_2(153))


# AI Version
#!/usr/bin/env python3
"""
Determine whether a number is an Armstrong number.
"""


def is_armstrong(n: int) -> bool:
    """
    Determine whether n is an Armstrong number.

    Args:
        n: The number to check.

    Returns:
        True if n is an Armstrong number, otherwise False.
    """
    if n < 0:
        return False

    if n == 0:
        return True

    power = 0
    current = n

    while current > 0:
        power += 1
        current //= 10

    total = 0
    current = n

    while current > 0:
        digit = current % 10
        total += digit ** power
        current //= 10

    return total == n