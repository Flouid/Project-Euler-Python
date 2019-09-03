import time

'''
Consider the fraction, n/d, where n and d are positive integers. If n<d and HCF(n,d)=1, 
it is called a reduced proper fraction.

If we list the set of reduced proper fractions for d ≤ 8 in ascending order of size, we get:

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that there are 21 elements in this set.

How many elements would be contained in the set of reduced proper fractions for d ≤ 1,000,000?

Louis Keith
5-26-19
'''


class Problem72:

    @staticmethod
    def main():
        start = time.time()

        # let's look at very small d to see what is going on. d = 1 has no fractions
        # d = 2; 1/2
        # d = 3; 1/2, 1/3, 2/3 or d = 2 + [1/3, 2/3]
        # d = 4; d = 3 + [1/4, 3/4]
        # d = 5; d = 4 + [1/5, 2/5, 3/5, 4/5]
        # d = 6; d = 5 + [1/6 + 5/6]
        # notice what is going on here, for each d the list of fractions grows by the number of numbers less than
        # the new d that are relatively prime to it. From earlier problems this is another way of describing the totient
        # so the goal here is to get the totient sum of all totient values for n from 2 to 1,000,000

        # the approach here is to take a list of every number from 0 to the l,000,000 and apply a sieve of eratosthenes
        # instead of removing multiples of primes we come across, we instead multiply them by (1 - 1/p) where p is the
        # prime they were found to be a multiple of. For primes this will occur once and evaluate to (p - 1)
        # for composites, they should be hit by a pass for every prime they are divisible by, and thus get converted
        # ultimately to nΠ(1-1/p): the totient. From there it is a simple matter of summing the list from 2

        limit = 1000000
        totient = []
        for i in range(limit + 1):
            totient.append(i)
        totient_sum = 0
        for i in range(2, limit + 1):
            if totient[i] == i:
                j = i
                while j <= limit:
                    totient[j] = (totient[j] / i) * (i - 1)
                    j += i
            totient_sum = int(totient_sum + totient[i])
        print(totient_sum)

        end = time.time()
        print("found in " + str(end - start) + " seconds")


if __name__ == '__main__':
    Problem72.main()
