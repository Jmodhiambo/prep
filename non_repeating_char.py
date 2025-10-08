#!/usr/bin/env python3
"""
The function takes in a string and returns the first non repeating character
"""

from typing import Optional
from sys import argv


def first_non_repeating_char(s: str) -> Optional[str]:
    """
    Takes in a string and returns the first non-repeating character if there else None.
    Args:
        -> s (str): input string
    Return:
        -> str: The first non-repeating character or None if otherwise
    """
    if not s:
        return None  # Returns None is the string is empty
    
    length: int = len(s) - 1

    if length == 0:
        return s  # Returns the string if it has only one character
    
    if length == 1:
        if s[0] == s[1]:
            return None  # Returns None for a two character string with the same characters.
        return s[0]  # Return the first character is different characters
    
    if s[0] != s[1] and s[0] not in s:
        return s[0]  # Returns the first character for strings with more that 2 chars with the first being different from the second.
    
    left: int = 0
    mid: int = 1
    right: int = 2
    
    while mid < length:  # Loops over to find the first non repeating character
        if right == length and s[mid] != s[right]:
            return s[right]

        if s[left] != s[mid] and s[mid] != s[right] and s[mid] not in s:
            return s[mid]
        
        left += 1
        mid += 1
        right += 1

    return None
    

if __name__ == "__main__":
    try:
        arg = argv[1]
    except:
        arg = ""

    print(first_non_repeating_char(arg))


# AI Solution 1 (Based on mine) Difference because mine was focusing on subsequent character while 
# non-repeating meant no similar character in the whole string.
# #!/usr/bin/env python3
# """
# The function takes in a string and returns the first non-repeating character.
# """

# from typing import Optional
# from collections import OrderedDict
# from sys import argv


# def first_non_repeating_char(s: str) -> Optional[str]:
#     """
#     Takes in a string and returns the first non-repeating character if there else None.
#     Args:
#         -> s (str): input string
#     Return:
#         -> str: The first non-repeating character or None if otherwise
#     """
#     if not s:
#         return None  # Empty string

#     # Use OrderedDict to preserve order while counting occurrences
#     freq = OrderedDict()

#     for char in s:
#         freq[char] = freq.get(char, 0) + 1

#     # Find first character with frequency 1
#     for char, count in freq.items():
#         if count == 1:
#             return char

#     return None


# if __name__ == "__main__":
#     try:
#         arg = argv[1]
#     except IndexError:
#         arg = ""

#     print(first_non_repeating_char(arg))


# AI Solution 2
# from typing import Optional
# from collections import Counter

# def first_non_repeating_char(s: str) -> Optional[str]:
#     """
#     Returns the first non-repeating character in a string.
#     """
#     if not s:
#         return None

#     freq = Counter(s)

#     for char in s:
#         if freq[char] == 1:
#             return char
#     return None