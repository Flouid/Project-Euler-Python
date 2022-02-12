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
from Problem81 import ingest_data, print_matrix
from Problem82 import write_matrix


def get_sum(cost):
    """A dynamic programming approach that calculates a total cost function for a matrix.
    Transforms the input matrix to a total cost matrix as it goes along, no extra memory required.
    Returns the minimum cost to traverse the entire matrix from top right to bottom left."""
    r_end, c_end = len(cost[0]) - 1, len(cost) - 1

    # populate the first row and first column with their respective costs to reach
    for c in range(1, c_end + 1):
        cost[0][c] += cost[0][c-1]
    for r in range(1, r_end + 1):
        cost[r][0] += cost[r-1][0]

    # populate the rest of the total cost matrix
    for r in range(1, r_end + 1):
        for c in range(1, c_end + 1):
            cost[r][c] += min(cost[r-1][c],
                                    cost[r][c-1])

    return cost[r_end][c_end], cost


def main():
    cost, cost_matrix = get_sum(ingest_data('test_matrix.txt'))
    print(cost)

    if verbose:
        print_matrix(cost_matrix)
        write_matrix(cost_matrix)

    
if __name__ == '__main__':
    if len(sys.argv) == 2 and sys.argv[1] == '-v':
        verbose = True
    else:
        verbose = False

    start = time()
    main()
    print('\nFINISHED IN %s SECONDS' % round(time() - start, 4))