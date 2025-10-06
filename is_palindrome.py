#!/usr/bin/env python3
"""This utility function checks if the string is a palindrome."""

def is_palindrome(s: str) -> bool:
    """
    Checks if the string is Palindrome.
    Args:
        -> s (str): input string
    Return:
        -> boolen: True for palindrome and False if otherwise
    """
    if not s:
        return True  # Assumes the palindrome of a empty string is empty

    if not isinstance(s, str):
        raise ValueError("The passed argument is not a string")

    s = s.lower()  # Lower the string for easy check

    i: int = len(s) - 1
    j: int = 0

    while j < i:
        if s[j] != s[i]:
            return False
        i -= 1
        j += 1
    
    return True


def non_alphanumeric_palindrome(s: str) -> bool:
    if not isinstance(s, str):
        raise ValueError("Input must be a string")

    s = s.lower()
    left, right = 0, len(s) - 1

    while left < right:
        # Skip non-alphanumeric characters
        if not s[left].isalnum(): # If not letters (A–Z, a–z) or digits (0–9)
            left += 1
            continue
        if not s[right].isalnum():
            right -= 1
            continue

        if s[left] != s[right]:
            return False

        left += 1
        right -= 1

    return True


if __name__ == "__main__":
    print(is_palindrome("raceCar"))

# Complexity
# Time: 0(n/2) ~ 0(n)
# Space: 0(1) - No new structures created.
