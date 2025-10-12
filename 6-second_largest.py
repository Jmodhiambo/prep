#!/usr/bin/env python3
"""Returns the second largest value from list of integers without using sort(ed) functions."""

from sys import argv


def second_largest(numbers: list) -> int:
    """
    Return the second largest item in the list.
    Args:
        -> numbers (list): input list
    Return:
        -> Second largest value in the list or raise ValueError if otherwise
    """
    if not isinstance(numbers, list):
        raise ValueError("The argument passed must be a list.")

    # Convert the list to set to ensure unique integer values
    numbers = set(numbers)

    if len(numbers) < 2:
        raise ValueError("The list must contain at least two unique values.")

    # If only two values return the min value
    if len(numbers) == 2:
        return min(numbers)

    # Find the largest value and remove it from the set
    largest = max(numbers)
    numbers.remove(largest)

    # Find the largest value again but now it will be second largest
    second = max(numbers)

    return second


def second_largest_two(numbers: list) -> int:
    if not isinstance(numbers, list):
        raise ValueError("The argument passed must be a list.")

    # Convert the list to set to ensure unique integer values
    # Covert the set back to list since set is unordered and not indexable
    numbers = list(set(numbers))

    if len(numbers) < 2:
        raise ValueError("The list must contain at least two unique values.")

    largest: int = numbers[0]
    second: int = numbers[1]

    # Ensure that largest bigger than second 
    if largest < second:
        largest, second = second, largest

    for num in numbers[2:]:  # Start from index 2
        if num > largest:
            second = largest
            largest = num
            
        elif num > second:
            second = num

    return second


if __name__ == "__main__":
    try:
        # The list is string so convert to value to integers
        arg = list(map(int, argv[1:]))
    except IndexError:
        arg = []

    print("Function 1:", second_largest(arg))
    print("Function 2:", second_largest_two(arg))


# The first function uses two max() which makes it easy to read and follow but not optimal.
# A single max() call is O(n) so that means to O(n) which is still O(n) though but not effective
# So the second one having a single O(n) makes it more optimal
# No usage of numbers.sort() or sorted(numbers)