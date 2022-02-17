"""
The smallest number expressible as the sum of a prime square, prime cube, 
and prime fourth power is 28. In fact, there are exactly four numbers below 
fifty that can be expressed in such a way:

28 = 2^2 + 2^3 + 2^4
33 = 3^2 + 2^3 + 2^4
49 = 5^2 + 2^3 + 2^4
47 = 2^2 + 3^3 + 2^4

How many numbers below fifty million can be expressed as the sum of a prime square, 
prime cube, and prime fourth power?

Louis Keith
2-17-21
"""


from time import time
import sys
from utils import is_prime
import numpy as np


def find_primes(threshold):
    """Use the Miller-Rabin algorithm to generate all primes below a threshold."""
    if verbose:
        print('Finding all primes below %d...' % threshold)
    primes = [2]
    for n in range(3, threshold):
        if is_prime(n):
            primes.append(n)
    return primes


def find_num_triples(threshold, primes):
    """Use a dynamic programming approach to populate the entire solution space.
    Returns the number of unique solutions found in that solution space."""
    # save computation time by calculating the primes to each power of interest ahead of time
    power2 = [pow(prime, 2) for prime in primes]
    power3 = [pow(prime, 3) for prime in primes]
    power4 = [pow(prime, 4) for prime in primes]
    len_primes = len(primes)
    # create a 3D matrix where the coordinates of each element represent the combination
    # of primes required to generate that element, initialize it with zeros at first.
    solution_space = np.zeros((len_primes, len_primes, len_primes), dtype=int)

    # populate the matrix
    for k in range(len_primes):
        for j in range(len_primes):
            for i in range(len_primes):
                sum = power2[i] + power3[j] + power4[k]
                if sum < threshold:
                    # debugging statement
                    if verbose:
                        print('%d = %d^2 + %d^3 + %d^4' % (sum, primes[i], primes[j], primes[k]))
                    solution_space[i, j, k] = sum
                # if at any point the sum exceeds the threshold, stop populating along that axis
                else:
                    break
            if power2[0] + power3[j] + power4[k] >= threshold:
                break
        if power2[0] + power3[0] + power4[k] >= threshold:
            break
    # calculating the number of unique elements takes some time
    if verbose:
        print('Counting unique elements of the solution space...')
    # don't consider 0 as a solution, so subtract 1
    return len(np.unique(solution_space)) - 1


def main():
    threshold = 50000000
    primes = find_primes(int(pow(threshold, 0.5)))
    num_triples = find_num_triples(threshold, primes)

    print(num_triples)


if __name__ == '__main__':
    verbose = False
    if len(sys.argv) == 2 and sys.argv[1] == '-v':
        verbose = True

    start = time()
    main()
    print('\nFINISHED IN %s SECONDS' % round(time() - start, 4))