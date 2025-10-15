#!/usr/bin/env python3
"""Find unique intersection of two lists"""


def unique_intersection_of_two_lists(list1: list, list2: list) -> list:
    """
    Find the unique intersection of two list.
    Args:
        - list1 (list): Input list 1
        - list2 (list): Input list 2
    Return:
        - New list of unique intersections
    """
    if not isinstance(list1, list) or not isinstance(list2, list):
        raise ValueError("Both inputs must be lists.")
    
    if len(list1) <= len(list2):
        short, long = list(set(list1)), set(list2)
    else:
        short, long = list(set(list2)), set(list1)

    unique = []

    for i in range(len(short)):
        if short[i] in long:
            unique.append(short[i])

    return unique


if __name__ == "__main__":
    list1 = [1, 2, 2, 3, 4]
    list2 = [2, 2, 3, 5]

    print(unique_intersection_of_two_lists(list1, list2))


# AI Approach

def unique_intersection_of_two_lists(list1: list, list2: list) -> list:
    """
    Find the unique intersection of two lists.
    Args:
        - list1 (list): Input list 1
        - list2 (list): Input list 2
    Return:
        - New list of unique intersections
    """
    if not isinstance(list1, list) or not isinstance(list2, list):
        raise ValueError("Both inputs must be lists.")

    short, long = (set(list1), set(list2)) if len(list1) <= len(list2) else (set(list2), set(list1))
    return [x for x in short if x in long]
