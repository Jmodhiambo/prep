#!/usr/bin/env python3
"""Checks if two strings are anagrams of each other."""
from collections import Counter
from sys import argv


def are_anagrams(str1: str, str2: str) -> bool:
    """
    Checks if the two strings are anagrams of each other.
    Args:
        - str1 (str): Input string 1
        - str2 (str): Input string 2
    Return:
        - Boolean: True is anagrams and False if otherwise
    """
    if not isinstance(str1, str) or not isinstance(str2, str):
        raise ValueError("Both arguments must be strings.")

    # Remove spaces and make the string a dict using counter
    # The keys are the chars and the value are chars count
    str1 = Counter(str1.replace(" ", "").lower())
    str2 = Counter(str2.replace(" ", "").lower())

    # Iterate over the two dicts and check if a similar key exists in both and have the same value
    for k in str1.keys():
        if k in str2.keys():
            if str1[k] == str2[k]:
                continue
            else:
                return False
        else:
            return False
        
    return True


if __name__ == "__main__":
    if len(argv) < 3:
        print("Usage: ./10-anagrams <string1> <string2>")
    else:
        print(are_anagrams(argv[1], argv[2]))


# AI Approach
def are_anagrams(str1: str, str2: str) -> bool:
    if not isinstance(str1, str) or not isinstance(str2, str):
        raise ValueError("Both arguments must be strings.")
    
    str1 = Counter(str1.replace(" ", "").lower())
    str2 = Counter(str2.replace(" ", "").lower())
    
    return str1 == str2


# Approach 1: Using Sorting
def are_anagrams_sorting(str1: str, str2: str) -> bool:
  str1 = str1.replace(" ", "").lower()
  str2 = str2.replace(" ", "").lower()
  return sorted(str1) == sorted(str2)

# Simple, elegant, and often the first solution candidates give in interviews.


# Approach 2: Using a Manual Dictionary (Count Map)
def are_anagrams_dict(str1: str, str2: str) -> bool:
  str1 = str1.replace(" ", "").lower()
  str2 = str2.replace(" ", "").lower()

  if len(str1) != len(str2):
    return False

  count = {}

  for ch in str1:
    count[ch] = count.get(ch, 0) + 1

  for ch in str2:
    if ch in count:
      count[ch] -= 1
    else:
      return False

  # Ensure all counts return to zero
  return all(v == 0 for v in count.values())

# This version is ideal for demonstrating logic and understanding of hashing.


# Approach 3: Using Character Arrays (for limited alphabets)
def are_anagrams_array(str1: str, str2: str) -> bool:
  str1 = str1.replace(" ", "").lower()
  str2 = str2.replace(" ", "").lower()

  if len(str1) != len(str2):
    return False

  counts = [0] * 26  # One slot per letter (a–z)

  for ch in str1:
    counts[ord(ch) - ord('a')] += 1

  for ch in str2:
    counts[ord(ch) - ord('a')] -= 1

  return all(c == 0 for c in counts)

# This version often impresses interviewers who want to see low-level optimization thinking.