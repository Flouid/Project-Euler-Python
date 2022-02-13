"""
In the 5 by 5 matrix below, the minimal path sum from the top left to the bottom right, 
by moving left, right, up, and down, is indicated in bold red and is equal to 2297.

/ ->131   673 ->234 ->103  ->18   \ 
| ->201  ->96 ->342   965 ->150   | 
|   630   803   746 ->422 ->111   | 
|   537   699   497 ->121   956   | 
\   805   732   524  ->37 ->331   / 
 
Find the minimal path sum from the top left to the bottom right by moving left, 
right, up, and down in matrix.txt (right click and "Save Link/Target As..."), 
a 31K text file containing an 80 by 80 matrix.

Louis Keith
2-12-22
"""


from time import time
import sys
import numpy as np
from Problem81 import ingest_data, get_sum, print_matrix
from Problem82 import write_matrix


def perform_update(partial, cost, r, c, nrows, ncols):
    """Take a partial cost matrix, the input cost matrix, and a pair of coordinates r and c
    and perform an update on the partial matrix."""
    # do nothing in the top left corner
    if r == 0 and c == 0:
        return partial[-1, -1], partial
    # special case for top right corner
    elif r == 0 and c == ncols-1:
        partial[r, c] = cost[r, c] + min(partial[r, c-1],
                                         partial[r+1, c])
    # special case for bottom left corner
    elif r == nrows-1 and c == 0:
        partial[r, c] = cost[r, c] + min(partial[r, c+1],
                                         partial[r-1, c])
    # special case for bottom right corner
    elif r == nrows-1 and c == ncols-1:
        partial[r, c] = cost[r, c] + min(partial[r, c-1],
                                         partial[r-1, c])
    # special case for top row
    elif r == 0:
        partial[r, c] = cost[r, c] + min(partial[r, c-1],
                                         partial[r, c+1],
                                         partial[r+1, c])
    # special case for bottom row
    elif r == nrows-1:
        partial[r, c] = cost[r, c] + min(partial[r, c-1],
                                         partial[r, c+1],
                                         partial[r-1, c])
    # special case for left column
    elif c == 0:
        partial[r, c] = cost[r, c] + min(partial[r, c+1],
                                         partial[r-1, c],
                                         partial[r+1, c])
    # special case for right column
    elif c == ncols-1:
        partial[r, c] = cost[r, c] + min(partial[r, c-1],
                                         partial[r-1, c],
                                         partial[r+1, c])
    # general case
    else:
        partial[r, c] = cost[r, c] + min(partial[r, c-1],
                                         partial[r, c+1],
                                         partial[r-1, c],
                                         partial[r+1, c])
    return partial[-1, -1], partial


def generate_cost(matrix):
    """Take a cost matrix as input and calculate the shortest possible path from
    the top left corner to the bottom right. Do this by first using the solution
    from Problem 81 to get the sum moving only down and to the right, then iterately
    improving it by checking if any of the total costs can be imroved. This algorithm
    runs until further passes don't improve the result."""
    # use numpy arrays because they have nicer syntax for indexing
    cost = np.array(matrix)
    nrows, ncols = np.shape(cost)

    # get a partial cost matrix resulting from only moving down and to the right
    _, partial = get_sum(matrix)
    partial = np.array(partial)
    result = partial[-1, -1]

    passes = 0
    while True:
        passes += 1
        # one pass of the algorithm updates every cell in the matrix
        for r in range(nrows):
            for c in range(ncols):
                new_result, partial = perform_update(partial, cost, r, c, nrows, ncols)
        # if no improvement was made, the algorithm is finished
        if new_result == result:
            if verbose:
                print('PASSED REQUIRED: %d' % passes)
            return result, partial
        else:
            result = new_result
    

def main():
    cost, cost_matrix = generate_cost(ingest_data('matrix.txt'))
    print(cost)

    if verbose:
        print_matrix(cost_matrix)
        write_matrix(cost_matrix)

    
if __name__ == '__main__':
    verbose = False
    if len(sys.argv) == 2 and sys.argv[1] == '-v':
        verbose = True

    start = time()
    main()
    print('\nFINISHED IN %s SECONDS' % round(time() - start, 4))