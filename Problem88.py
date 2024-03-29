"""
A natural number, N, that can be written as the sum and product of a given set of at 
least two natural numbers, {a1, a2, ... , ak} is called a product-sum number: 
N = a1 + a2 + ... + ak = a1 x a2 x ... x ak.

For example, 6 = 1 + 2 + 3 = 1 x 2 x 3.

For a given set of size, k, we shall call the smallest N with this property a minimal product-sum 
number. The minimal product-sum numbers for sets of size, k = 2, 3, 4, 5, and 6 are as follows.

k=2: 4 = 2 x 2 = 2 + 2
k=3: 6 = 1 x 2 x 3 = 1 + 2 + 3
k=4: 8 = 1 x 1 x 2 x 4 = 1 + 1 + 2 + 4
k=5: 8 = 1 x 1 x 2 x 2 x 2 = 1 + 1 + 2 + 2 + 2
k=6: 12 = 1 x 1 x 1 x 1 x 2 x 6 = 1 + 1 + 1 + 1 + 2 + 6

Hence for 2≤k≤6, the sum of all the minimal product-sum numbers is 4+6+8+12 = 30; 
note that 8 is only counted once in the sum.

In fact, as the complete set of minimal product-sum numbers for 2≤k≤12 is 
{4, 6, 8, 12, 15, 16}, the sum is 61.

What is the sum of all the minimal product-sum numbers for 2≤k≤12000?

Louis Keith
2-17-22
"""


from time import time
import sys
from math import prod
from copy import deepcopy

    
def get_min_nps(k):
    # only try to calculate for valid cases
    assert(k>=2)

    # initialize with a decent guess, the following is true for all k
    # (1 ** (k-2)) * 2 * k = 2k = (1 * (k-2)) + 2 + k
    elems = [1] * k
    elems[-1] = k
    elems[-2] = 2
    s, p = sum(elems), prod(elems)

    return s, elems
    
    

def main():
    sols = set()
    if verbose:
        print('k:\tnps\telems\n--------------------------------')
    for k in range(2, 11):
        min_npms, min_elems = get_min_nps(k)
        if verbose:
            print(str(k) + ':\t', min_npms, '\t', min_elems)
        sols.add(min_npms)
    if verbose:
        print('--------------------------------')
    print(sum(sols))


if __name__ == '__main__':
    verbose = False
    if len(sys.argv) == 2 and sys.argv[1] == '-v':
        verbose = True

    start = time()
    main()
    print('\nFINISHED IN %s SECONDS' % round(time() - start, 4))