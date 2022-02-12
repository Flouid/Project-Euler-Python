"""
The minimal path sum in the 5 by 5 matrix below, by starting in any cell in the left column and 
finishing in any cell in the right column, and only moving up, down, and right, is indicated in 
red and bold; the sum is equal to 994.

/   131   673 ->234 ->103  ->18   \ 
| ->201  ->96 ->342   965   150   | 
|   630   803   746   422   111   | 
|   537   699   497   121   956   | 
\   805   732   524    37   331   / 

Find the minimal path sum from the left column to the right column in matrix.txt 
(right click and "Save Link/Target As..."), a 31K text file containing an 80 by 80 matrix.

Louis Keith
2-11-22
"""


from time import time
import sys
from copy import deepcopy
from Problem81 import ingest_data, print_matrix


def find_path(matrix):
    """A dynamic programming approach that calculates the total cost function 
    from each place in the leftmost column of the input matrix. For each start,
    the minimum cost is the smallest value in the rightmost column. The answer 
    is the lowest minimum cost seen."""
    r_end, c_end = len(matrix[0]) - 1, len(matrix) - 1
    min_cost = sys.maxsize - 1

    # for each starting row in the first column, get the total cost matrix
    for r_start in range(r_end + 1):
        cost, cost_matrix = get_cost(matrix, r_start, r_end, c_end)
        # track the lowest cost that has been calculated
        if cost < min_cost:
            min_cost = cost
            min_cost_matrix = deepcopy(cost_matrix)
        if verbose:
            print('CHECKING:', r_start, cost)

    return min_cost, min_cost_matrix


def get_cost(matrix, r_start, r_end, c_end):
    """Find the minimum cost to any cell in the right column 
    from a given start row in the input matrix."""
    # create a deep copy of the input matrix to edit
    total_cost = deepcopy(matrix)

    # populate the left-most column of the cost matrix
    for r in range(r_start + 1, r_end + 1):
        total_cost[r][0] += total_cost[r-1][0]
    for r in reversed(range(0, r_start)):
        total_cost[r][0] += total_cost[r+1][0]

    # populate the rest of the cost matrix
    for c in range(1, c_end + 1):
        # calculate the start row and everything beneath it
        for r in range(r_start, r_end + 1):
            # don't consider costs that haven't been calculated yet
            if r == r_start:
                total_cost[r][c] += total_cost[r][c-1]
            else:
                total_cost[r][c] += min(total_cost[r][c-1],
                                        total_cost[r-1][c])
        # calculate everything above the start row
        for r in reversed(range(0, r_start)):
            # special case for when the start row is the bottom row
            total_cost[r][c] += min(total_cost[r][c-1],
                                    total_cost[r+1][c])
    
    # find the minimum of the rightmost column and return
    return min([row[-1] for row in total_cost]), total_cost


def write_matrix(matrix):
    """Write a matrix to an output file in the same format as the input matrix."""
    with open('out.txt', 'w') as f:
        for r in range(len(matrix)):
            for c in range(len(matrix[r])):
                f.write(str(matrix[r][c]))
                if c != len(matrix[r]) - 1:
                    f.write(',')
            f.write('\n')
    

def main():
    cost, cost_matrix = find_path(ingest_data('test_matrix.txt'))
    print(cost)

    if verbose:
        write_matrix(cost_matrix)

    
if __name__ == '__main__':
    if len(sys.argv) == 2 and sys.argv[1] == '-v':
        verbose = True
    else:
        verbose = False

    start = time()
    main()
    print('\nFINISHED IN %s SECONDS' % round(time() - start, 4))