import time

'''
Consider the fraction, n/d, where n and d are positive integers. If n<d and HCF(n,d)=1, 
it is called a reduced proper fraction.

If we list the set of reduced proper fractions for d ≤ 8 in ascending order of size, we get:

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that 2/5 is the fraction immediately to the left of 3/7.

By listing the set of reduced proper fractions for d ≤ 1,000,000 in ascending order of size, 
find the numerator of the fraction immediately to the left of 3/7.

Louis Keith
5-25-19
'''


class Problem71:

    @staticmethod
    def main():
        start = time.time()

        # what's the closest number to 3/7 without being 3/7? How would you generate such a number?
        # well, a good approach would be to try doing ((3*k) - 1)/(7*k), with higher k getting closer and closer
        # with an upper limit of 1,000,000 for the denominator then the most I can multiply by is 1,000,000/7
        k = int(1000000 / 7)
        # the denominator will surely be (3 * k) - 1
        denominator = (3 * k) - 1
        print(denominator)

        end = time.time()
        print("found in " + str(end - start) + " seconds")


if __name__ == '__main__':
    Problem71.main()
