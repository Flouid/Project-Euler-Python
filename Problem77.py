import time
from Problem69 import Problem69

'''
It is possible to write ten as the sum of primes in exactly five different ways:

7 + 3
5 + 5
5 + 3 + 2
3 + 3 + 2 + 2
2 + 2 + 2 + 2 + 2

What is the first value which can be written as the sum of primes in over five thousand different ways?

Louis Keith
8-3-19
'''


class Problem77:

    # this is a much harder variation of the problem before it. If i had to guess the version before was probably
    # susceptible to brute force in a way this is not. luckily the dynamic programming method from before will not
    # be affected much by the change from integers to primes.

    @staticmethod
    def main():
        start = time.time()

        target = 5000
        prime_upper_bound = 500
        print(Problem77.solve(target, prime_upper_bound))

        end = time.time()
        print("found in " + str(end - start) + " seconds")

    @staticmethod
    # this function will probably be useful later anyway, uses a sieve I wrote earlier to populate a list
    def get_primes_list(bound):
        primes = []
        for i in range(2, bound):
            if Problem69.is_prime(i):
                primes.append(i)
        return primes

    @staticmethod
    # finds the first value which can be written in at least n ways as a sum of primes up to a bound
    # this needed to be its own function because I wanted to escape the loop with a return as soon as it's found
    def solve(n, prime_bound):
        primes = Problem77.get_primes_list(prime_bound)
        ways = [0 for i in range(n + 1)]
        ways[0] = 1

        # works the same as in problem 76 but iterating through a list of primes instead of just all integers
        # the bound for the primes was chosen somewhat arbitrarily and then adjusted to be near-ish the ideal value
        for i in range(len(primes)):
            if ways[i] > n:
                return i
            j = primes[i]
            while j <= prime_bound:
                ways[j] += ways[j - primes[i]]
                j += 1


if __name__ == '__main__':
    Problem77.main()
