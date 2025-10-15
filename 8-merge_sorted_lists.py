#!/usr/bin/env python3
"""Merge two sorted lists into a single list sorted in ascending order"""


def merge_sorted_lists(list1: list, list2: list) -> list:
    """
    Merge two sorted list into one in ascending order.
    Args:
        - list1 (list): Input list 1
        - list2 (list): Input list 2
    Return:
        - Merged list1 and list2
    """
    if not isinstance(list1, list) and not isinstance(list2, list):
        raise ValueError("Both inputs need to be lists.")
    
    # Return a present list if the other input is not a list
    if not list1:
        return list2
    if not list2:
        return list1
    
    len1, len2, i, j = len(list1) - 1, len(list2) - 1, 0, 0
    new_list = []

    while i <= len1 or j <= len2:
        if list1[i] < list2[j]:
            new_list.append(list1[i])
            i += 1
        else:
            new_list.append(list2[j])
            j += 1

        # Minus 1 from i and j since we had incremented them above
        if (i - 1) == len1 and (j - 1) < len2:
            new_list += list2[j:]
            break

        if (j - 1) == len2 and (i - 1) < len1:
            new_list += list1[i:]
            break

    return new_list


if __name__ == "__main__":
    list1 = [1, 2, 4]
    list2 = [1, 3, 4]

    print(merge_sorted_lists(list1, list2))


# AI Approach

def merge_sorted_lists(list1: list, list2: list) -> list:
    if not isinstance(list1, list) or not isinstance(list2, list): # Assume both inputs are lists
        raise ValueError("Both inputs must be lists.")

    i = j = 0
    merged = []

    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            merged.append(list1[i])
            i += 1
        else:
            merged.append(list2[j])
            j += 1

    # Append remaining elements (if any)
    merged.extend(list1[i:])
    merged.extend(list2[j:])
    return merged
