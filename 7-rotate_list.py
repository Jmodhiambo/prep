#!/usr/bin/env python3
"""Rotates a list to the right by given count"""

from sys import argv
from collections import deque


def rotate_list(lst: list, k: int) -> list:
    """
    Rotates a list by k steps. K is a non-negative integer
    Args:
        -> lst (list): Input list
        -> k (int): Steps to ratate the list to the right
    Return:
        -> A rotatated list
    """
    if not isinstance(lst, list):
        raise ValueError("Please ensure the first argument is a list.")

    if k < 0:
        msg = "Please ensure the second argument is a non-negative integer"
        raise ValueError(msg)

    # Return the same list if k is 0 or equal to the list length
    if k == 0 or k == len(lst):
        return lst  # When length == k means list will rotate back to initial

    # If list is more than length the rotation becomes length % k
    if k > len(lst):
        k = k % len(lst)

    # Create a deque instance of the list to allow appending to the left
    lst = deque(lst)

    # Iterate over the list to pop and append
    while k:
        popped_value = lst.pop()  # Pop the last value
        lst.appendleft(popped_value)  # Append the popped value

        k -= 1

    return list(lst)


if __name__ == "__main__":
    try:
        lst = argv[1].split()
        k = int(argv[2]) if len(argv) > 2 else 0
    except IndexError:
        lst = []
        k = 0

    print(rotate_list(lst, k))


# AI Approach 1 (Using Rotate built-in feature in deque)

# def rotate_list(lst: list, k: int) -> list:

#     if not isinstance(lst, list):
#         raise ValueError("First argument must be a list.")
#     if not isinstance(k, int) or k < 0:
#         raise ValueError("Second argument must be a non-negative integer.")

#     n = len(lst)
#     if n == 0 or k == 0 or k == n:
#         return lst

#     k = k % n  # ✅ corrected

#     lst = deque(lst)
#     lst.rotate(k)  # ✅ built-in deque method, O(k) but cleaner
#     return list(lst)



# AI Approach 2 (Using slicing)

# def rotate_list(lst: list, k: int) -> list:

#     if not isinstance(lst, list):
#         raise ValueError("First argument must be a list.")
#     if not isinstance(k, int) or k < 0:
#         raise ValueError("Second argument must be a non-negative integer.")

#     n = len(lst)
#     if n == 0 or k == 0 or k == n:
#         return lst

#     # Adjust k in case it's larger than the list length
#     k = k % n

#     # Slicing does all the work here
#     return lst[-k:] + lst[:-k]
# lst[-k:] → [5, 6, 7] (the last 3 elements)
# lst[:-k] → [1, 2, 3, 4] (the first 4 elements)
# Combine → [5, 6, 7] + [1, 2, 3, 4]


# AI Approach 3 (Rotating in the same list without creating a new one)

# def rotate_list(lst: list, k: int) -> None:
#     """Rotate a list to the right by k steps in-place (O(1) extra space)."""
#     if not isinstance(lst, list):
#         raise ValueError("First argument must be a list.")
#     if not isinstance(k, int) or k < 0:
#         raise ValueError("Second argument must be a non-negative integer.")

#     n = len(lst)
#     if n == 0 or k == 0 or k == n:
#         return

#     k = k % n  # handle cases where k > n

#     def reverse(sublist, start, end):
#         """Helper function to reverse elements in-place."""
#         while start < end:
#             sublist[start], sublist[end] = sublist[end], sublist[start]
#             start += 1
#             end -= 1

#     # 1. Reverse entire list
#     reverse(lst, 0, n - 1)
#     # 2. Reverse first k elements
#     reverse(lst, 0, k - 1)
#     # 3. Reverse remaining n-k elements
#     reverse(lst, k, n - 1)

#     return lst
