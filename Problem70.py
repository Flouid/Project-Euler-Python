import time
import sys
import math
from Problem69 import Problem69

'''
Euler's Totient function, φ(n) [sometimes called the phi function], is used to determine the number of positive 
numbers less than or equal to n which are relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8, 
are all less than nine and relatively prime to nine, φ(9)=6.

The number 1 is considered to be relatively prime to every positive number, so φ(1)=1.

Interestingly, φ(87109)=79180, and it can be seen that 87109 is a permutation of 79180.

Find the value of n, 1 < n < 10^7, for which φ(n) is a permutation of n and the ratio n/φ(n) produces a minimum.

Louis Keith
5-25-19
'''


class Problem70:

    @staticmethod
    # determines if p and q are permutations of one another and returns a boolean
    def is_permutation(p, q):
        # this method deals with p and q as strings but can handle being passed numbers
        p = str(p)
        q = str(q)

        # straight up equality check to save some calculations if they are the same
        if p.__eq__(q):
            return True

        # if they aren't the same length they can't be permutations of one another
        if len(p) != len(q):
            return False

        # converting the two numbers to lists of digits
        tokens_p = []
        tokens_q = []
        for i in range(len(p)):
            tokens_p.append(p[i])
        for i in range(len(q)):
            tokens_q.append(q[i])

        # every token in p must be somewhere in q, after each check the token is removed in order to handle duplicates
        for token in tokens_p:
            if token in tokens_q:
                tokens_q.remove(token)
            else:
                return False
        return True

    @staticmethod
    # method title may be obtuse but that's exactly what this does given a limit to search up to. returns n
    def find_n_with_min_ratio_and_permuting_totient(limit):
        n_with_min_ratio = -1
        min_ratio = sys.maxsize
        # the starting p is an optimization choice; the higher the limit is, the closer it can be to the square root
        for p in reversed(range(int(1.2 * math.sqrt(limit)))):      # 1.2 was found to be optimal for this problem
            if Problem69.is_prime(p):
                for q in range(p):
                    n = p * q
                    # if the q gets high enough n goes over the limit then just go to the next p
                    if n > limit:
                        break
                    if Problem69.is_prime(q):
                        totient = int(n * (1 - 1 / p) * (1 - 1 / q))
                        if Problem70.is_permutation(n, totient):
                            # print(str(p) + " * " + str(q) + ": " + str(n) + " and its totient: " + str(totient))
                            ratio = n / totient
                            if ratio < min_ratio:
                                min_ratio = ratio
                                n_with_min_ratio = n
        return n_with_min_ratio

    @staticmethod
    def main():
        start = time.time()

        # another heavy number theory one
        # from the previous problem: The totient of a number n is defined as nΠ(1-1/p)
        # where p is a distinct prime factor of n and Π is the product of all p
        # the goal is to minimize n/nΠ(1-1/p) => 1/Π(1-1/p). That means we are maximizing it's reciprocal Π(1-1/p).
        # notice how each distinct factor p reduces the end result, so we want as few factors as possible.
        # at the same time, the totient of just a prime (p - 1) cannot be its reciprocal.
        # also notice how each factor is (1-1/p) so higher values for p bring the factor closer to one.
        # all this is to say that the n we are looking for should occur around the square root of the limit, and must
        # be the product of two primes, this greatly simplifies the totient calculation.
        # however it is my experience the answer can occur for p around limit / 2 for much lower limits.

        limit = 10000000
        print(Problem70.find_n_with_min_ratio_and_permuting_totient(limit))

        end = time.time()
        print("found in " + str(end - start) + " seconds")


if __name__ == '__main__':
    Problem70.main()
