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


# shifting nth root algorithm
def main():
    for num in range(2, 101):
        base = 10  # base of the number system
        n = 2  # degree of the root to be extracted
        x = 0  # radicand processed thus far
        y = 0  # root extracted thus far
        r = 0  # remainder
        alpha = 0  # next n digits of the radicand
        beta = 0  # next digit of the root
        x_prime = 0  # next value of x
        y_prime = 0  # next value of y
        r_prime = 0  # next value of r


if __name__ == '__main__':
    start = time()
    main()
    print('\nFINISHED IN %s SECONDS' % round(time() - start, 4))
