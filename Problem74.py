import time
import math
from Problem70 import Problem70

'''
The number 145 is well known for the property that the sum of the factorial of its digits is equal to 145:

1! + 4! + 5! = 1 + 24 + 120 = 145

Perhaps less well known is 169, in that it produces the longest chain of numbers that link back to 169; 
it turns out that there are only three such loops that exist:

169 → 363601 → 1454 → 169
871 → 45361 → 871
872 → 45362 → 872

It is not difficult to prove that EVERY starting number will eventually get stuck in a loop. For example,

69 → 363600 → 1454 → 169 → 363601 (→ 1454)
78 → 45360 → 871 → 45361 (→ 871)
540 → 145 (→ 145)

Starting with 69 produces a chain of five non-repeating terms, 
but the longest non-repeating chain with a starting number below one million is sixty terms.

How many chains, with a starting number below one million, contain exactly sixty non-repeating terms?

Louis Keith
5-28-19
'''


class Problem74:

    @staticmethod
    # checks if the number has 60 terms before it first repeats according to the process described above
    def has_sixty_non_repeating_terms(n):
        factorial_sum = 0
        # after looking, all of the numbers we are looking for have mostly the same 60 terms, they just get on the path
        # from a different number. All permutations of that number will have the same factorial sum and thus lead to
        # the same path. So all we need to do is check if the first factorial sum is a permutation of this number
        check_against = 367954
        for i in range(int(math.log10(n) + 1)):
            digit = n % 10
            n = int(n / 10)
            factorial_sum += Problem74.fast_factorial(digit)
        return Problem70.is_permutation(factorial_sum, check_against)

    @staticmethod
    # faster factorial with hardcoded values for n < 10, takes about 2s off evaluation
    def fast_factorial(n):
        if n == 0:
            return 1
        elif n == 1:
            return 1
        elif n == 2:
            return 2
        elif n == 3:
            return 6
        elif n == 4:
            return 24
        elif n == 5:
            return 120
        elif n == 6:
            return 720
        elif n == 7:
            return 5040
        elif n == 8:
            return 40320
        elif n == 9:
            return 362880

    @staticmethod
    # applies factorial function and returns result, notation for it is !
    def factorial(n):
        factorial = 1
        for i in range(1, n + 1):
            factorial *= i
        return factorial

    @staticmethod
    def main():
        start = time.time()

        lower_bound = 1
        upper_bound = 1000000
        counter = 0
        for i in range(lower_bound, upper_bound):
            if Problem74.has_sixty_non_repeating_terms(i):
                counter += 1
        print(counter)

        end = time.time()
        print("found in " + str(end - start) + " seconds")


if __name__ == '__main__':
    Problem74.main()
