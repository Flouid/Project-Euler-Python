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


def is_solution(x, y, z):
    """Determines if the shortest path length along a cubiod of dimensions (x, y, z) is an integer."""
    if x == y and x == z:
        d = math.sqrt((x + x)**2 + x**2)
    elif x == y:
        d = min(math.sqrt((x + z)**2 + x**2),
                math.sqrt((x + y)**2 + z**2))
    elif x == z:
        d = min(math.sqrt((x + y)**2 + z**2),
                math.sqrt((x + z)**2 + y**2))
    elif y == z:
        d = min(math.sqrt((x + z)**2 + y**2),
                math.sqrt((y + z)**2 + x**2))
    else:
        d = min(math.sqrt((x + y)**2 + z**2),
                math.sqrt((x + z)**2 + y**2),
                math.sqrt((y + z)**2 + x**2))
    return int(d) == d, d


def num_solutions(limit):
    """Find all solutions with integer pathlength below a given maximum dimension."""
    paths = 0
    for x in range(1, limit + 1):
        for y in range(1, x + 1):
            for z in range(1, y + 1):
                sol, d = is_solution(x, y, z)
                if sol:
                    paths += 1

                    if verbose:
                        print('%dx%dx%d = %d' % (x, y, z, d), end='\t')
                        print('C =', num_combinations(y, z), end='\n')

    return paths


def get_next_m(limit, paths):
    for y in range(1, limit + 1):
        for z in range(1, y + 1):
            sol, _ = is_solution(limit, y, z)
            if sol:
                paths += 1
    return paths


def num_combinations(a, b):
    """Returns the number of unique combinations of integers that add up to the sum of two numbers"""
    return int(abs(a - b) / 2) + 1


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
    # print(num_solutions(100))
    print('\nFINISHED IN %s SECONDS' % round(time() - start, 4))