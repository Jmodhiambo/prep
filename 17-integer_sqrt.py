#!/usr/bin/env python3
"""This module finds the square root of a number"""

def integer_sqrt(n: int) -> int:
    """
    Takes in a number and returns the square root of the number
    Arg:
        n: the number
    Return:
        the square root of the number or the number closes to the squareroot is the number is not a perfect square
    """
    # Outright return for 0 and 1
    if n <= 1:
        return n

    # Declare variables to use
    start: int = 1
    end: int = n
    mid: int = (start + end) // 2
    sqr: int = 0
    answer: int = mid

    while start <= end:
        sqr = mid * mid

        if sqr > n:
            end = mid - 1
        else:
            start = mid + 1
            answer = mid   # Number is the highest viable square root

        mid = (start + end) // 2

    return answer


if __name__ == "__main__":
    print(integer_sqrt(10))


# AI detailed version
#!/usr/bin/env python3
"""This module implements an integer square root using binary search."""


def integer_sqrt(n: int) -> int:
    """
    Return the integer square root of a non-negative integer.

    The integer square root is the largest integer `x` such that:

        x² <= n

    For perfect squares, this returns the exact square root. For numbers
    that are not perfect squares, it returns the floor of the square root.

    Examples:
        integer_sqrt(0)  -> 0
        integer_sqrt(1)  -> 1
        integer_sqrt(4)  -> 2
        integer_sqrt(8)  -> 2
        integer_sqrt(15) -> 3
        integer_sqrt(16) -> 4
        integer_sqrt(24) -> 4
        integer_sqrt(25) -> 5

    Approach:
        A straightforward solution would start at 1 and keep increasing
        the candidate until its square becomes greater than `n`. However,
        that approach can require O(n) iterations in the worst case.

        Instead, binary search is used because the possible answers are
        ordered.

        For a candidate `mid`:

            mid² <= n
                `mid` is a valid answer, but a larger valid answer may
                still exist. Save `mid` and search the right half.

            mid² > n
                `mid` is too large to be the answer. Search the left half.

        The `answer` variable stores the largest valid candidate found so
        far. This is necessary because when a valid `mid` is found, we
        continue searching to the right for a potentially larger valid
        value.

        When the search finishes, there are no unexplored candidates left,
        so `answer` must be the largest integer whose square is less than
        or equal to `n`.

    Why `left = mid + 1`:
        When `mid² <= n`, `mid` has already been saved as a valid candidate.
        We no longer need to consider `mid`, so the next search starts at
        `mid + 1`.

    Why `right = mid - 1`:
        When `mid² > n`, `mid` cannot be the answer, and neither can any
        value greater than `mid`. Therefore, the next search ends at
        `mid - 1`.

    Why `answer` starts at 0:
        The input is guaranteed to be non-negative, and 0 is always a
        valid integer square root candidate because 0² <= n.

    Why `left <= right`:
        The search continues while there is at least one candidate left
        to examine. Once `left` becomes greater than `right`, the entire
        search space has been eliminated.

    Complexity:
        Time: O(log n)
            Binary search eliminates approximately half of the remaining
            candidates on every iteration.

        Space: O(1)
            Only a fixed number of integer variables are used regardless
            of the size of `n`.

    Note:
        Python integers do not have the same fixed-width overflow behavior
        as integer types in languages such as C, C++, or Java. In those
        languages, calculating `mid * mid` may require additional care to
        avoid integer overflow.
    """
    if n <= 1:
        return n

    left: int = 1
    right: int = n
    answer: int = 0

    while left <= right:
        mid: int = (left + right) // 2

        if mid * mid <= n:
            answer = mid
            left = mid + 1
        else:
            right = mid - 1

    return answer


if __name__ == "__main__":
    print(integer_sqrt(2147395600))