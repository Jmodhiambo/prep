#!/usr/bin/env python 3
"""Returns a list of Prime Numbers upto n."""

from math import isqrt


def list_prime_numbers(n: int) -> list:
    """
    Returns a list of prime numbers upto nth value.
    Args:
        - n (int): Input value
    Return:
        - list: All prime numbers upto nth value.
    """
    if n < 2:
        return []
    if n == 2:
        return [2]
    else:
        possible_primes = [2] # Create a list with 2 if n is greater than 2
    
    possible_primes.extend([num for num in range(3, n + 1) if num % 2 != 0])

    def is_prime(num: int) -> bool:
        """Return True if num is prime and False if not."""
        for i in range(3, isqrt(num) + 1, 2):
            if num % i == 0:
                return False
        return True
    
    prime_numbers = [num for num in possible_primes if is_prime(num)]

    return prime_numbers


if __name__ == "__main__":
    from sys import argv
    if len(argv) < 2:
        print("Usage: ./12-list_prime_nmbers <positive integer>")
    else:
        n = int(argv[1])
        print(list_prime_numbers(n))


# My optimized version
def list_prime_numbers(n: int) -> list:
    if n < 2:
        return []
    
    primes = [2]
    for num in range(3, n + 1, 2):  # directly skip evens
        for i in range(3, isqrt(num) + 1, 2):
            if num % i == 0:
                break
        else:
            primes.append(num)
    return primes


# AI Approach 1 - Use only previous primes as the divisors
def optimized_trial_division(n: int) -> list[int]:
    if n < 2:
        return []
    primes = [2]
    for num in range(3, n + 1, 2):
        is_prime = True
        for p in primes:
            if p * p > num:
                break
            if num % p == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes

# AI Approach 2 - Use the Sieve of Eratosthenes (Best Impact)
