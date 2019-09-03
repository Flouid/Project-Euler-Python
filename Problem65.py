import time
from fractions import Fraction

'''
The square root of 2 can be written as an infinite continued fraction.

2–√=1+1/2+1/2+1/2+1/2+...
The infinite continued fraction can be written, 2–√=[1;(2)], (2) indicates that 2 repeats ad infinitum. 
In a similar way, 23−−√=[4;(1,3,1,8)].

It turns out that the sequence of partial values of continued fractions for square roots provide the best 
rational approximations. Let us consider the convergents for 2–√.

1+1/2=3/2
1+1/2+1/2=7/5
1+1/2+1/2+1/2=17/12
1+1/2+1/2+1/2+1/2=41/29
Hence the sequence of the first ten convergents for 2–√ are:

1,3/2,7/5,17/12,41/29,99/70,239/169,577/408,1393/985,3363/2378,...
What is most surprising is that the important mathematical constant,
e=[2;1,2,1,1,4,1,1,6,1,...,1,2k,1,...].

The first ten terms in the sequence of convergents for e are:

2,3,8/3,11/4,19/7,87/32,106/39,193/71,1264/465,1457/536,...
The sum of digits in the numerator of the 10th convergent is 1+4+5+7=17.

Find the sum of digits in the numerator of the 100th convergent of the continued fraction for e.

Louis Keith
5-21-19
'''


class Problem65:

    @staticmethod
    # evaluates the nth convergent of e using its continued fraction representation and returns it as a fraction
    def approximate_e(n):
        seq = Problem65.generate_e_sequence(n)
        if n == 1:
            return 2
        fraction = Fraction(1, seq[n - 2])
        for i in reversed(range(n - 2)):
            fraction = Fraction(1, seq[i] + fraction)
        return 2 + fraction

    @staticmethod
    # generates the sequence for e's period according to [1, 2, 1, 1, 4, 1, 1... 2k, 1, 1, 2(k + 1)...]
    # terminates after n digits of the sequence have been generated
    def generate_e_sequence(n):
        seq = [1]
        count = 2
        k = 2
        for i in range(0, n):
            if count == 2:
                seq.append(k)
                k += 2
                count = 0
            else:
                seq.append(1)
                count += 1
        return seq

    @staticmethod
    def main():
        start = time.time()

        # generates the numerator and creates a sum of the digits
        numerator = str(Problem65.approximate_e(100).numerator)
        count = 0
        for i in range(0, len(numerator)):
            count += int(numerator[i])
        print(count)

        end = time.time()
        print("found in " + str(end - start) + " seconds")


if __name__ == '__main__':
    Problem65.main()
