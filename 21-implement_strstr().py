#!/usr/bin/env python3
"""
Implement strStr().
Return the index of the first occurrence of needle in haystack,
or -1 if needle is not part of haystack and 0 if needle is empty.
"""


def str_str(haystack: str, needle: str) -> int:
    """
    Find the first occurrence of a substring within a string.

    The function searches for `needle` inside `haystack` without using
    Python's built in substring searching methods such as `find()` or
    the `in` operator.

    The algorithm uses a brute force approach. The outer loop treats
    each valid position in `haystack` as a possible starting position
    for `needle`. For every starting position, the inner loop compares
    the characters of `needle` with the corresponding characters in
    `haystack`.

    Two indexes are used for different purposes:

        i: The possible starting position of `needle` in `haystack`.
        j: The current character being checked in `needle`.

    When comparing characters, `haystack[i + j]` is used because `i`
    represents where the potential match starts and `j` represents
    how far into `needle` we have progressed.

    If a mismatch occurs, the inner loop stops and the outer loop
    tries the next possible starting position. If `j` reaches the
    length of `needle`, every character matched and `i` is returned.

    Args:
        haystack: The string in which to search.
        needle: The substring to search for.

    Returns:
        The starting index of the first occurrence of `needle`.
        Returns 0 if `needle` is empty.
        Returns -1 if `needle` cannot be found in `haystack`.

    Time Complexity:
        O(n * m), where n is the length of `haystack` and m is the
        length of `needle`.

    Space Complexity:
        O(1), because only a constant amount of additional memory
        is used.
    """

    # An empty needle is considered to be found at index 0.
    if not needle:
        return 0

    # If the needle is longer than the haystack, it cannot possibly
    # occur inside the haystack.
    if len(needle) > len(haystack):
        return -1

    # Try every position where the complete needle could potentially
    # fit inside the haystack.
    #
    # Example:
    # haystack = "hello"  (length 5)
    # needle = "ll"      (length 2)
    #
    # Possible starting positions are 0, 1, 2, and 3.
    for i in range(len(haystack) - len(needle) + 1):

        # j represents how many characters of the needle we have
        # successfully matched so far.
        j = 0

        # Compare the needle with the portion of the haystack that
        # starts at position i.
        while j < len(needle):

            # i is the potential starting position and j is the
            # current position inside the needle.
            #
            # Therefore, i + j gives us the corresponding position
            # in the haystack.
            if haystack[i + j] != needle[j]:
                # A mismatch means this starting position cannot
                # contain the complete needle.
                break

            # The current characters matched, so move to the next
            # character in the needle.
            j += 1

        # If j reached the length of the needle, every character
        # matched successfully. Therefore, i is the first position
        # where the needle occurs.
        if j == len(needle):
            return i

    # None of the possible starting positions contained the needle.
    return -1


if __name__ == "__main__":
    print(str_str("sadbutsad", "sad"))      # 0
    print(str_str("leetcode", "leeto"))    # -1
    print(str_str("hello", "ll"))          # 2
    print(str_str("aaaaa", "bba"))         # -1
    print(str_str("", "le"))               # -1
    print(str_str("leetcode", ""))         # 0
    print(str_str("mississippi", "issip")) # 4



#!/usr/bin/env python3
"""
Implement strStr() using the Knuth Morris Pratt algorithm.
"""


def str_str(haystack: str, needle: str) -> int:
    """
    Find the first occurrence of `needle` inside `haystack` using KMP.

    The Knuth Morris Pratt (KMP) algorithm improves on the brute force
    substring search by avoiding unnecessary comparisons.

    The key idea is to preprocess `needle` and build an LPS array.

    LPS stands for "Longest Prefix which is also a Suffix".

    For every position in `needle`, lps[i] stores the length of the
    longest proper prefix of needle[0:i + 1] that is also a suffix.

    This information tells us how far we can move `needle` after a
    mismatch without starting the comparison from the beginning.

    During the search:

        i: position currently being examined in haystack.
        j: position currently being examined in needle.

    If haystack[i] matches needle[j], both indexes move forward.

    If they do not match and j > 0, we use lps[j - 1] to determine
    where to continue in needle. Importantly, i does not move backward
    because we already know that the characters before i have been
    examined.

    If j == 0 during a mismatch, there is no previously matched prefix
    to reuse, so we simply move i forward.

    Args:
        haystack: The string in which to search.
        needle: The substring to search for.

    Returns:
        The starting index of the first occurrence of `needle`.
        Returns 0 if `needle` is empty.
        Returns -1 if `needle` is not found.

    Time Complexity:
        O(n + m), where n is the length of `haystack` and m is the
        length of `needle`.

        Building the LPS array takes O(m), and searching the haystack
        takes O(n).

    Space Complexity:
        O(m), because the LPS array stores information about `needle`.
    """

    # An empty needle is considered to be found at index 0.
    if not needle:
        return 0

    # If the needle is longer than the haystack, it cannot occur.
    if len(needle) > len(haystack):
        return -1

    # ---------------------------------------------------------------
    # STEP 1: Build the LPS (Longest Prefix Suffix) array.
    # ---------------------------------------------------------------

    # lps[i] stores the length of the longest proper prefix of
    # needle[0:i + 1] that is also a suffix.
    lps = [0] * len(needle)

    # i represents the current position we are calculating in lps.
    i = 1

    # length represents the length of the prefix that currently
    # matches the suffix.
    length = 0

    while i < len(needle):

        if needle[i] == needle[length]:
            # The current character extends the matching prefix.
            length += 1
            lps[i] = length
            i += 1

        elif length > 0:
            # We found a mismatch, but we may still have a smaller
            # prefix that can match.
            #
            # We do NOT move i because needle[i] still needs to be
            # compared with the shorter prefix.
            length = lps[length - 1]

        else:
            # There is no prefix to fall back to.
            lps[i] = 0
            i += 1

    # ---------------------------------------------------------------
    # STEP 2: Search for needle inside haystack.
    # ---------------------------------------------------------------

    # i is the current position in haystack.
    i = 0

    # j is the current position in needle.
    j = 0

    while i < len(haystack):

        if haystack[i] == needle[j]:
            # The current characters match, so move forward in both
            # strings.
            i += 1
            j += 1

            # We have matched every character in needle.
            if j == len(needle):
                # i points immediately after the match, so subtract
                # the length of needle to get the starting position.
                return i - len(needle)

        elif j > 0:
            # A mismatch occurred after matching some characters.
            #
            # Instead of restarting needle from position 0, use the
            # LPS array to find the next possible matching position.
            #
            # Notice that i does NOT move backward.
            j = lps[j - 1]

        else:
            # The first character of needle did not match.
            # There is nothing to fall back to, so move forward in
            # haystack.
            i += 1

    # The complete needle was never found.
    return -1