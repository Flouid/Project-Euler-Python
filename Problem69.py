import time
import sys
import math

'''
Euler's Totient function, φ(n) [sometimes called the phi function], is used to determine the number of numbers
 less than n which are relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8, are all less than nine
  and relatively prime to nine, φ(9)=6.

n	Relatively Prime	φ(n)	n/φ(n)
2	1	                1	      2
3	1,2	                2	      1.5
4	1,3	                2	      2
5	1,2,3,4	            4	      1.25
6	1,5	                2	      3
7	1,2,3,4,5,6	        6	      1.1666...
8	1,3,5,7	            4	      2
9	1,2,4,5,7,8	        6	      1.5
10	1,3,7,9	            4	      2.5
It can be seen that n=6 produces a maximum n/φ(n) for n ≤ 10.

Find the value of n ≤ 1,000,000 for which n/φ(n) is a maximum.

Louis Keith
5-25-19
'''


class Problem69:

    @staticmethod
    # determines if a number is prime and returns a boolean
    def is_prime(n):
        if n == 1:
            return False
        elif n == 2:
            return True
        elif n % 2 == 0:
            return False
        else:
            i = 3
            while i * i <= n:
                if n % i == 0:
                    return False
                i += 2
            return True

    @staticmethod
    def main():
        start = time.time()

        # this one is mostly solved through number theory.
        # let p denote any distinct prime factor of n and let Π denote the product of all p
        # from wikipedia, the totient of n/phi(n) is defined as nΠ(1-1/p)
        # thus to maximise n/phi(n) i am maximising 1/ Π(1-1/p) and thus minimizing Π(1-1/p)
        # if that's the case, it follows that the max for n/phi(n) is the highest number less than the
        # limit that is the product of consecutive primes
        limit = 1000000
        i = 1
        n = 1
        while True:
            i += 1
            if Problem69.is_prime(i):
                if n * i < limit:
                    n *= i
                else:
                    break
        print(n)

        end = time.time()
        print("found in " + str(end - start) + " seconds")


if __name__ == '__main__':
    Problem69.main()
