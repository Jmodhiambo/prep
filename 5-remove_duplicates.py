#!/usr/bin/env python3
"""This function removes duplicates from a list."""

from collections import Counter
from sys import argv


def remove_duplicates(lst: list) -> list:
    """
    Removes duplicates value in a list while maintaining the order of items
    Args:
        -> lst: input list
    """
    if not isinstance(lst, list):  # Handles both non-list and empty list
        raise ValueError("The argument must be a list.")

    unique_list = []

    # Returns {3: 2, 5: 2, 2: 2, 7: 1} i.e. item and item count in the list
    lst_count = Counter(lst)

    for k in lst_count.keys():
        unique_list.append(k)

    return unique_list


if __name__ == "__main__":
    try:
        lst = argv[1:]
    except IndexError:
        lst = []

    print(remove_duplicates(lst))


# AI Approach (Counter approach wokrs in pyton 3.7+ and might might cause error in lower versions so below is the best approach)
def remove_duplicates(lst: list) -> list:
    if not isinstance(lst, list):
        raise ValueError("The argument must be a list.")

    seen = set()
    unique = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            unique.append(item)
    return unique