"""A utility library with some useful functions for various problems"""

import random


def rab_exp_mod(b: int, e: int, m: int) -> int:
    """A version of modular exponentiation that incorporates the rabin algorithm.
    Based on the right-to-left binary method."""
    c = 1
    while e > 0:
        if e & 1:
            c = (c * b) % m
        e = e >> 1
        z = (b * b) % m
        # rabin algorithm
        if (z == 1) and (b != 1) and (b != m - 1):
            return 0
        else:
            b = z
    return c


def is_prime(m: int, k=1000) -> bool:
    """Implements the Miller-Rabin algorithm to check if a given number is prime.
    Runs the algorithm k times to ensure accuracy of 1-(1/(2**k))"""
    for _ in range(k):
        a = random.randint(1, m - 1)
        if rab_exp_mod(a, m, m) != a:
            return False
    return True