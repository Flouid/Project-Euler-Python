import time
from fractions import Fraction

'''
Consider the fraction, n/d, where n and d are positive integers. If n<d and HCF(n,d)=1, 
it is called a reduced proper fraction.

If we list the set of reduced proper fractions for d ≤ 8 in ascending order of size, we get:

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that there are 3 fractions between 1/3 and 1/2.

How many fractions lie between 1/3 and 1/2 in the sorted set of reduced proper fractions for d ≤ 12,000?

Louis Keith
5-26-19
'''


class Problem73:

    @staticmethod
    # gets the greatest common denominator of two numbers using euclid's method
    def gcd(p, q):
        while p != q:
            if p > q:
                p -= q
            else:
                q -= p
        return p

    @staticmethod
    def main():
        start = time.time()

        # given the d is 12,000 this should be an easy solve with brute force
        limit = 12000
        counter = 0
        lower_bound = Fraction(1, 3)
        upper_bound = Fraction(1, 2)
        for d in range(5, limit + 1):
            for n in range(int(d/3 + 1), int((d - 1)/2 + 1)):
                if Problem73.gcd(n, d) == 1:
                    if lower_bound < Fraction(n, d) < upper_bound:
                        counter += 1
        print(counter)
        # note: 'easy' is a relative term and this takes 90+ seconds to run on my computer. I should revisit this

        end = time.time()
        print("found in " + str(end - start) + " seconds")


if __name__ == '__main__':
    Problem73.main()
