import time
import math

'''
It is well known that if the square root of a natural number is not an integer, then it is irrational. 
The decimal expansion of such square roots is infinite without any repeating pattern at all.

The square root of two is 1.41421356237309504880..., and the digital sum of the first one hundred decimal digits is 475.

For the first one hundred natural numbers, find the total of the digital sums of the first 
one hundred decimal digits for all the irrational square roots.

Louis Keith
8-5-19
'''


class Problem79:

    # so it seems the essence of this problem is to efficiently calculate square roots digit by digit if i understand
    # this correctly. Looking up methods of computing square roots wikipedia offers several algorithms for calculating
    # digit by digit square roots. The one that stood out to me (as actually understandable) was an altered form of
    # long division.

    #############################################################################################################

    # well that was a pretty easy implement and it works but nothing is ever that easy, the remainder grows far too fast
    # and in a way that im not sure how to compress or optimize because its precise value is needed for each successive
    # calculation, time to look for another method

    @staticmethod
    def main():
        start = time.time()

        print(math.e**(0.5 * math.log(2)))
        '''
        limit = 100
        n = 2
        x = int(n**(1/2))
        remainder = n - x**2
        p = x
        digital_sum = 0
        for i in range(limit):
            upper_bound = remainder * 100
            for j in range(1, 9):
                if ((20 * p) + (j + 1)) * (j + 1) > upper_bound:
                    remainder = upper_bound - ((20 * p) + j) * j
                    x = j
                    p = (10 * p) + x
                    digital_sum += x
                    print(x, remainder, p)
                    break
        print()
        print(digital_sum)
        '''

        end = time.time()
        print("found in " + str(end - start) + " seconds")


if __name__ == '__main__':
    Problem79.main()
