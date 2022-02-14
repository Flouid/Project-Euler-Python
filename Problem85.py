"""
By counting carefully it can be seen that a rectangular grid measuring 3 by 2 contains eighteen rectangles:

Although there exists no rectangular grid that contains exactly two million rectangles, 
find the area of the grid with the nearest solution.

Louis Keith
2-13-22
"""


from time import time
import sys


def find_best_area(target=2000000):
    """Search the solution space within some bounds to keep it as quick as possible."""
    best_area = 0
    smallest_dist = target
    limit = 100
    margin = 1.02

    for c in range(2, limit):
        for r in range(2, limit):
            # calculate the number of rectangles for the current dimension using an analytical formula
            num = (r * c * (r+1) * (c+1)) / 4
            # calculate the distance from the target number
            dist = abs(target - num)
            # store the result if it's better than any previous solution
            if dist < smallest_dist:
                best_area = c * r
                smallest_dist = dist
                if verbose:
                    print('%dx%d produced %d rectangles and an area of %d' % (c, r, num, best_area))
            # if the number has grown too far past the target, stop increasing the row size and look again
            elif num > target * margin:
                break
    
    return best_area
    

def main():
    print(find_best_area())


if __name__ == '__main__':
    verbose = False
    if len(sys.argv) == 2 and sys.argv[1] == '-v':
        verbose = True

    start = time()
    main()
    print('\nFINISHED IN %s SECONDS' % round(time() - start, 4))