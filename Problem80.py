"""
It is well known that if the square root of a natural number is not an integer, then it is irrational.
The decimal expansion of such square roots is infinite without any repeating pattern at all.

The square root of two is 1.41421356237309504880..., and the digital sum of the first one hundred decimal digits is 475.

For the first one hundred natural numbers, find the total of the digital sums of the first
one hundred decimal digits for all the irrational square roots.

Louis Keith
2-11-22
"""

from time import time


base = 10
precision = 100


def get_next_aligned_block(s: str, n: int) -> int:
    """Return the next most significant aligned block of n digits from num."""
    # prepend as many zeros as is necessary to make the length of s a multiple of n
    if s == '':
        return 0, ''
    elif len(s) == n:
        return int(s), ''
    else:
        s = '0' * (n - (len(s) % n)) + s
        return int(s[0:n]), s[n:]


def find_beta(y, r, n, alpha):
    """By the loop invariant of the nth root algorithm, beta is the largest digit that satisfies the following condition."""
    for beta in reversed(range(10)):
        if (base * y + beta) ** n - (base ** n) * (y ** n) <= (base ** n) * r + alpha:
            return beta


def nth_root(num, n):
    """Uses the nth root algorithm to calculate the decimal expansion of a square root up to a certain precision."""
    # initialization
    y = 0
    r = 0 
    s = str(num)
    # main loop
    for _ in range(precision):
        alpha, s = get_next_aligned_block(s, n)
        beta = find_beta(y, r, n, alpha)
        y_prime = base * y + beta
        r = (base ** n) * r + alpha - ((base * y + beta) ** n - (base ** n) * (y ** n))
        y = y_prime
    return y


def main():
    """Uses the shifting nth root algorithm to calculate the digital expansion to 100 places for the first 100 numbers."""
    n = 2
    tot_sum = 0

    for num in range(2, 101):
        if int(num ** 0.5) != num ** 0.5:
            y = nth_root(num, n)
            y_sum = sum([int(c) for c in str(y)])
            tot_sum += y_sum
    
    print(tot_sum)


if __name__ == '__main__':
    start = time()
    main()
    print('\nFINISHED IN %s SECONDS' % round(time() - start, 4))
