#!/usr/bin/env python3
"""This function converts a decimal to binary"""

def decimal_to_binary(n: int) -> str:
    """
    Converts a decimal to binary
    Arg:
        n: the value to be converted to binary
    Return:
        a string binary representation of the value given
    """
    # Outright return "0" if the value is 0
    if n == 0:
        return "0"
    
    # Turn to True if the number is negative
    is_negative: bool = False

    if n < 0:
        n = abs(n)
        is_negative = True

    binary: str = ""

    while n > 0:
        if n % 2 == 0:
            binary = "0" + binary
        else:
            binary = "1" + binary

        n //= 2

    return binary if not is_negative else "-" + binary


if __name__ == "__main__":
    print(decimal_to_binary(0))
    print(decimal_to_binary(-1))
    print(decimal_to_binary(11))
    print(decimal_to_binary(-11))


# AI Version
def decimal_to_binary(n: int) -> str:
    """Convert a decimal integer to its binary representation."""
    if n == 0:
        return "0"

    is_negative: bool = n < 0
    n = abs(n)

    bits: list[str] = []

    while n > 0:
        bits.append(str(n % 2))
        n //= 2

    bits.reverse()

    binary: str = "".join(bits)

    return f"-{binary}" if is_negative else binary


# Complexity Notes
# Big O Notation

# Big O describes how an algorithm's time or memory requirements grow as the input size grows.

# It does not simply count the number of loops.

# For time complexity, ask:

# How many operations are performed, and how expensive is each operation?

# For space complexity, ask:

# What data does the algorithm store, and does that storage grow with the input?

# Common Complexities
# Complexity	Meaning	Example
# O(1)	Constant	Accessing an array element
# O(log n)	Problem repeatedly reduced by a factor	Binary search
# O(n)	Process input once	Loop through a list
# O(n log n)	Divide and process	Efficient sorting
# O(n²)	Nested processing	Comparing every pair
# O(2ⁿ)	Exponential growth	Some recursive algorithms
# O(n!)	Factorial growth	Generating permutations
# Important Rule

# The work inside a loop matters.

# For:

# for i in range(n):
#     operation()

# If operation() is O(1):

# n × 1 = O(n)

# If operation() is O(n):

# n × n = O(n²)

# Therefore:

# Loop complexity × cost per iteration = overall complexity

# Logarithmic Complexity

# When a value is repeatedly divided by a constant factor:

# n
# n / 2
# n / 4
# n / 8
# n / 16
# ...

# the number of iterations is:

# O(log n)

# This commonly appears in binary search and binary conversion.

# Space Complexity

# Distinguish between auxiliary space and output space.

# For example:

# result = []

# If the result grows proportionally with the input, it requires additional space.

# For the decimal to binary problem, the number of binary digits is approximately:

# log₂(n)

# Therefore, storing the binary representation requires:

# O(log n)

# space.

# Day 15 Example

# Repeatedly prepending to a Python string:

# binary = "1" + binary

# can cause repeated copying because Python strings are immutable.

# Although the loop runs O(log n) times, the total work can become:

# O((log n)²)

# A better approach is:

# bits.append(str(n % 2))

# followed by:

# bits.reverse()
# binary = "".join(bits)

# This gives:

# Time:  O(log n)
# Space: O(log n)
# Interview Mental Checklist

# Whenever asked for complexity, think:

# 1. How many times does the algorithm run?
# 2. What work happens during each iteration?
# 3. Are any operations secretly expensive?
# 4. What data am I storing?
# 5. Does that data grow with the input?
# 6. Am I counting the output space or only auxiliary space?

# Key takeaway: Do not simply count loops. Analyze the work performed by the loops and the memory consumed by the algorithm.