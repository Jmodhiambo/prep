#!/usr/bin/env python3
"""This functions counts the number or vowels and consonants in a string"""

from sys import argv


def count_vowels_and_consonants(s: str) -> dict:
    """
    Counts the number of vowels and consonants in a string.
    Args:
        -> s (str): Input string
    Return:
        -> dict: {"Vowels": int, "Consonants": int}
    """
    # Return None for a empty string or if the argument is not a string
    if not s or type(s) is not str:
        return {"Vowels": 0, "Consonants": 0}

    # Convert all characters to lowercase for ease of work
    s = s.lower()

    i: int = 0
    vowel_count: int = 0
    consonant_count: int = 0

    vowels = {"a", "e", "i", "o", "u"} # Set for O(1) lookup

    while i < (len(s)):
        if ord(s[i]) >= ord("a") and ord(s[i]) <= ord("z"):
            if s[i] in vowels:
                vowel_count += 1
            else:
                consonant_count += 1
        i += 1

    if not vowel_count and not consonant_count:
        return {"Vowels": 0, "Consonants": 0}
    else:
        return {"Vowels": vowel_count, "Consonants": consonant_count}


if __name__ == "__main__":
    try:
        arg = argv[1]
    except IndexError:
        arg = ""

    print(count_vowels_and_consonants(arg))


# AI Approach 1
# def count_vowels_and_consonants(s: str) -> dict:
#     if not isinstance(s, str):
#         raise TypeError("Input must be a string")

#     vowels = {"a", "e", "i", "o", "u"}
#     s = s.lower()

#     vowel_count = 0
#     consonant_count = 0

#     for ch in s:
#         if ch.isalpha() and ch.isascii():  # ensures only English letters
#             if ch in vowels:
#                 vowel_count += 1
#             else:
#                 consonant_count += 1

#     return {"Vowels": vowel_count, "Consonants": consonant_count}


# AI Approach 2
# def count_vowels_and_consonants(s: str) -> dict:
#     s = s.lower()
#     vowels = {"a", "e", "i", "o", "u"}

#     letters = [ch for ch in s if ch.isalpha() and ch.isascii()]
#     vowel_count = sum(1 for ch in letters if ch in vowels)
#     consonant_count = len(letters) - vowel_count

#     return {"Vowels": vowel_count, "Consonants": consonant_count}


# AI Approach 3 (Using Regular Expression/Regex)

# import re

# def count_vowels_and_consonants(s: str) -> dict:
#     s = s.lower()
#     vowels = "aeiou"

#     letters = re.findall(r"[a-z]", s)
#     vowel_count = sum(1 for ch in letters if ch in vowels)
#     consonant_count = len(letters) - vowel_count

#     return {"Vowels": vowel_count, "Consonants": consonant_count}
