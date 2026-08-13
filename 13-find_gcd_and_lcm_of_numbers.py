#!/usr/bin/env python3
"""Find the GCD and LCM of two numbers."""

from sys import argv

def find_gcd_and_lcm_two_number(num1: int, num2:int) -> tuple[int, int]:
    """
    Finds the GCD and LCM of two numbers.
    Args:
        num1: The first number
        num2: The second number
    Return:
        tuple(gcd, lcm)
    """
    # Ensure the values are integers
    if not isinstance(num1, int) or not isinstance(num2, int):
        raise TypeError("The values must be integers. Please try again.")

    # Check if both or either value is 0
    if num1 == 0 or num2 == 0:
        return (0, 0)

    # Check if the numbers are negative
    if num1 < 0 or num2 < 0:
        num1 = abs(num1)
        num2 = abs(num2)

    # Check if the numbers are equal
    if num1 == num2:
        return (num1, num1)

    small_value: int = num1 if num1 < num2 else num2
    big_value: int = num1 if num1 > num2 else num2

    # Check if the min value is a divisor of the max value
    if big_value % small_value == 0:
        return (small_value, big_value)

    def _find_gcd(min_value: int, max_value: int) -> int:
        """Find the GCD of the two values"""
        i: int = 2
        gcd_factors: list = []
        current_min: int = min_value

        while i < current_min:

            while min_value % i == 0 and max_value % i == 0:
                min_value //= i
                max_value //= i

                print(f"GCD round {i}: Min value {min_value} and max_value {max_value}")

                # Append i to the factor value list
                gcd_factors.append(i)

            # Break out of the loop if the min value gets to 1
            if min_value == 1:
                break

            # Increment i
            i += 1

        gcd: int = gcd_factors[0] if gcd_factors else 0

        for idx in range(1, len(gcd_factors)):
            gcd *= gcd_factors[idx]

        return gcd if gcd else 0


    def _find_lcm(min_value: int, max_value: int) -> int:
        """Find the LCM of the two values"""
        i: int = 2
        lcm_factors: list = []
        current_min: int = min_value

        while i < current_min:
            if min_value % i == 0 or max_value % i == 0:
                if min_value % i == 0:
                    min_value //= i

                if max_value % i == 0:
                    max_value //= i

                lcm_factors.append(i)
                continue

            if min_value == 1 or max_value == 1:
                if min_value == 1:
                    lcm_factors.append(max_value)
                    break

                if max_value == 1:
                    lcm_factors.append(min_value)
                    break

            i += 1

        lcm: int = lcm_factors[0] if lcm_factors else 0
        length: int = len(lcm_factors)
            
        for idx in range(1, length):
            lcm *= lcm_factors[idx]

        return lcm

    return (_find_gcd(small_value, big_value), _find_lcm(small_value, big_value))


if __name__ == "__main__":
    try:
        first_number, second_number = 12, 18
        gcd_value, lcm_value = find_gcd_and_lcm_two_number(first_number, second_number)

        print(f"GCD: {gcd_value}")
        print(f"LCM: {lcm_value}")

    except IndexError:
        print("Error in the arguments passed. Please check and try again.")