import time
import math
import sys
from Problem64 import Problem64
from fractions import Fraction

'''
Consider quadratic Diophantine equations of the form:

x^2 – Dy^2 = 1

For example, when D=13, the minimal solution in x is 649^2 – 13×180^2 = 1.

It can be assumed that there are no solutions in positive integers when D is square.

By finding minimal solutions in x for D = {2, 3, 5, 6, 7}, we obtain the following:

3^2 – 2×2^2 = 1
2^2 – 3×1^2 = 1
9^2 – 5×4^2 = 1
5^2 – 6×2^2 = 1
8^2 – 7×3^2 = 1

Hence, by considering minimal solutions in x for D ≤ 7, the largest x is obtained when D=5.

Find the value of D ≤ 1000 in minimal solutions of x for which the largest value of x is obtained.

Louis Keith
5-23-19
'''


class Problem66:

    @staticmethod
    # generates a fraction approximation for the square root of a number d for solving the Pell equation
    def approximate_root_d(d):
        period = Problem64.get_period(d)
        seq = []
        a0 = int(math.sqrt(d))
        # for d with an even period, the period must be modified so that a0 is in front and it truncates just before
        # the end of the second repetition. for d = 14 the period is [1, 2, 1, 6] and becomes [3, 1, 2, 1, 6, 1, 2, 1]
        if len(period) % 2 == 0:
            for i in range(0, len(period)):
                if i == 0:
                    seq.append(Fraction(a0))
                else:
                    seq.append(Fraction(period[i - 1]))
        # if the period is odd, it must be modified so that it truncates at the end of the first period.
        # an for example d = 13 is [1, 1, 1, 1, 6] and becomes [3, 1, 1, 1, 1]
        else:
            for i in range(0, 2 * len(period)):
                if i == 0:
                    seq.append(Fraction(a0))
                else:
                    seq.append(Fraction(period[(i - 1) % len(period)]))
        # evaluates the modified period as a continued fraction and returns it
        temp = 0
        for i in reversed(range(len(seq))):
            temp = 1/(seq[i] + temp)
        return 1/temp

    @staticmethod
    def main():
        start = time.time()

        upper_bound = 1000
        largest_x = -sys.maxsize - 1
        d_with_largest_x = -1
        for d in range(2, upper_bound):
            # d cannot be a perfect square
            if int(math.sqrt(d)) != math.sqrt(d):
                x = Problem66.approximate_root_d(d).numerator
                if x > largest_x:
                    largest_x = x
                    d_with_largest_x = d
        print(str(d_with_largest_x) + " had a minimum x of " + str(largest_x))

        end = time.time()
        print("found in " + str(end - start) + " seconds")


if __name__ == '__main__':
    Problem66.main()
