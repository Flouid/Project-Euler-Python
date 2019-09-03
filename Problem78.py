import time

'''
Let p(n) represent the number of different ways in which n coins can be separated into piles. 
For example, five coins can be separated into piles in exactly seven different ways, so p(5)=7.

OOOOO
OOOO   O
OOO   OO
OOO   O   O
OO   OO   O
OO   O   O   O
O   O   O   O   O
Find the least value of n for which p(n) is divisible by one million.

Louis Keith
8-5-19
'''


class Problem78:

    # this is proper partitioning, at first i thought the dynamic programming approach would work but i don't think so.
    # i found a recursive formula for seeing how many ways a number n can be divided into k parts, as follows:
    # pk(n) = pk−1(n−1) + pk(n − k)
    # it makes sense that the base cases would be pk(n) = 1 when k = 1 and pk(n) = 0 when k > n, representing
    # dividing something into one part (one solution) and dividing it into more parts than it contains (no solution)
    # it follows that summing the the function for all reasonable values of k for a given integer will give the
    # total number of partitions

    #############################################################################################################

    # that solution is totally valid and works but is too slow to be practical, i was thinking of ways to optimize
    # and arrived back at some form of dynamic programming, it needs to be building a list of solutions to refer too

    #############################################################################################################

    # well big oof, that new solution is much much better than the old one (reasonably can do up to n = 10000) instead
    # of the old crappy (n < 100) of before...
    # too bad the entire approach of using the pk(n) formula and summing the values is too inefficient, i need something
    # better. To that end i looked some more and stumbled across this formula:
    # p(n) = p(n - 1) + p(n - 2) - p(n - 5) - p(n 0 7) + p(n - 12) + p(n - 15) where the the sequence of numbers
    # subtracted from n is the generalized pentagonal sequence, denoted by k. When k exceeds n there is no point in
    # continuing because you'd be dividing into negative partitions.
    # the generalized pentagonal sequence is given by m(3m - 1)/2 for m = 0, 1, -1,  2, -2, 3, -3...

    @staticmethod
    def main():
        start = time.time()

        # approach 1
        '''
        for n in range(1, 1000):
            print(n)
            start1 = time.time()
            result = Problem78.total_partition(n)
            print(result)
            end1 = time.time()
            print("found in " + str(end1 - start1) + " seconds")
            print()
            if result % 1000000 == 0:
                print(n)
                break
        '''

        # approach 2
        '''
        limit = 10000
        partitions = [[0 for j in range(i + 1)] for i in range(limit)]
        print('n', 'Σ', 'partitions')

        for n in range(1, limit):
            for k in range(1, n + 1):
                if k == 1:
                    # as defined above, when k = 1, then pk(n) = 1
                    partitions[n][k] = 1
                elif k == n:
                    # there's only, one way to divide n into n parts, thus when p == k then pk(n) = 1
                    partitions[n][k] = 1
                elif n - k < k:
                    # if n - k is greater than k than it will attempt to ask a question analogous to:
                    # how many ways can i partition 1 into 2 parts? The question doesn't make sense and would throw an
                    # error, so it can be assumed to be zero and thus left out
                    partitions[n][k] = partitions[n - 1][k - 1]
                else:
                    # this is the recursive formula defined above but instead of calling itself, it can just access
                    # the values it has previously calculated
                    partitions[n][k] = partitions[n - 1][k - 1] + partitions[n - k][k]

            partition_sum = 0
            for k in partitions[n]:
                partition_sum += k
            print(n, partition_sum, partitions[n])

            if partition_sum % 1000000 == 0:
                print(n)
                end = time.time()
                print("found in " + str(end - start) + " seconds")
                return
        '''

        # approach 3
        limit = 60000   # i just incremented this by 10000 until i found the answer
        partitions = [0 for i in range(limit)]
        partitions[0] = 1
        for n in range(1, limit):
            # variable ranging from 0 to 3, representing the 4 states the addition signs cycled through (+, +, -, -)
            sign = 0
            # this is the variable that is used to generate generalized pentagonal numbers
            m = 0
            while True:
                # m needs to take on 0, 1, -1, 2... in precisely that order. This logic accomplishes that albeit badly
                if m == 0:
                    m += 1
                elif m > 0:
                    m = -m
                else:
                    m = -m + 1

                # generates a value of k and checks if it's usable
                k = int(m * (3 * m - 1) / 2)
                if n - k < 0:
                    break

                # either adds or subtracts based on the sign and then changes it's value accordingly
                if sign < 2:
                    partitions[n] += partitions[n - k]
                    sign += 1
                else:
                    partitions[n] -= partitions[n - k]
                    sign = (sign + 1) % 4
            # because the only operations with these numbers are addition and i don't care about any digits past the
            # first seven, i truncate them asap for memory purposes
            partitions[n] %= 1000000
            if partitions[n] == 0:
                print(n)
                break

        end = time.time()
        print("found in " + str(end - start) + " seconds")

    '''
    @staticmethod
    # simple recursive function for partitioning n into k parts, follows formula pk(n) = pk−1(n−1) + pk(n − k)
    def partition(n, k):
        # print("checking n = " + str(n) + " and k = " + str(k))
        if k > n:
            return 0
        elif k == 1:
            return 1
        else:
            return Problem78.partition(n - 1, k - 1) + Problem78.partition(n - k, k)

    @staticmethod
    # gets the total number of ways a number can be partitioned by using the partition formula for all k from 1 to n
    def total_partition(n):
        result = 0
        for k in range(1, n + 1):
            result += Problem78.partition(n, k)
        return result
    '''


if __name__ == '__main__':
    Problem78.main()
