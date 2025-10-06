#!/usr/bin/env python3
"""This function reverses a string."""


def reverse_string(s) -> str:
    """The function takes in a string and reverses it."""
    if not s:
        return s  # An empty string is valid and is returned as it is.

    if type(s) is not str:
        raise ValueError("Invalid data type")

    new_string = ""
    i: int = len(s) - 1

    while i >= 0:
        new_string += s[i]
        i -= 1

    return new_string


if __name__ == "__main__":
    print(reverse_string("hello"))
