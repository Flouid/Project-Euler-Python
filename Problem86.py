"""
A spider, S, sits in one corner of a cuboid room, measuring 6 by 5 by 3, and a fly, F, 
sits in the opposite corner. By travelling on the surfaces of the room the shortest 
"straight line" distance from S to F is 10 and the path is shown on the diagram.

However, there are up to three "shortest" path candidates for any given cuboid and the 
shortest route doesn't always have integer length.

It can be shown that there are exactly 2060 distinct cuboids, ignoring rotations, 
with integer dimensions, up to a maximum size of M by M by M, for which the shortest 
route has integer length when M = 100. This is the least value of M for which the number 
of solutions first exceeds two thousand; the number of solutions when M = 99 is 1975.

Find the least value of M such that the number of solutions first exceeds one million.

Louis Keith
2-14-22
"""


from time import time
import sys
import math


def get_next_m(limit, paths):
    """Use the assumption that limit will always be the largest side of the cubiod and that the sum
    of the other two sides can be dealt with independantly to get the number of cubiods for the next value of m."""
    for xy in range(2, limit * 2):
        if math.sqrt(xy**2 + limit**2).is_integer():
            paths += num_combinations(xy, limit)
    return paths


def num_combinations(xy, m):
    """Find how many integers x and y can be found such that 1 <= x <= y <= m and x + y == xy.
    This represents how many cubiods can be created from the sum xy."""
    # initialize x and y to be half of their sum, if xy is odd then y gets the extra 1
    x = int(xy / 2)
    y = x + (xy & 1)

    # return the shortest distance from the respective bounds of x and y
    return min(m - y + 1, x)


def main():
    m = 100
    paths = 2060
    threshold = 1000000
    while paths < threshold:
        m += 1
        paths = get_next_m(m, paths)
        if verbose:
            print('M: %d has %d solutions' % (m, paths))
    print(m)


if __name__ == '__main__':
    verbose = False
    if len(sys.argv) == 2 and sys.argv[1] == '-v':
        verbose = True

    start = time()
    main()
    print('\nFINISHED IN %s SECONDS' % round(time() - start, 4))