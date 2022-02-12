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
from Problem81 import ingest_data, print_matrix


def generate_cost(cost):
    """Uses a dynamic programming approach to calculate the minimum cost to traverse
    the matrix from left to right. It works by going column by column and at each step
    calculating the cost of moving forward and then checking if traversing up or down
    from another row would be cheaper. The rightmost column of the resulting cost matrix
    is the minium cost to reach each cell in that column."""
    n_rows, n_cols = len(cost), len(cost[0])

    # for every column except the first, get the minimum cost to each cell
    for c in range(1, n_cols):
        # generate forward partial path sums
        partial = [row[c] for row in cost]
        for r in range(n_rows):
            partial[r] += cost[r][c-1]
        # generate downward partial path sums
        for r in range(n_rows):
            # explore moving down the column as much as possible
            traverse = 0
            for e in range(1, n_rows-r):
                traverse += cost[r+e][c]
                # the cost of moving down is now greater than starting elsewhere
                if traverse > partial[r+e]:
                    break
                partial[r+e] = min(partial[r+e], partial[r] + traverse)
        # generate upward partial path sums
        for r in reversed(range(n_rows)):
            # explore moving up the column as much as possible
            traverse = 0
            for e in range(1, r):
                traverse += cost[r-e][c]
                # the cost of moving up is now greater than starting elsewhere
                if traverse > partial[r-e]:
                    break
                partial[r-e] = min(partial[r-e], partial[r] + traverse)
        # replace the current column of the cost matrix with the partial path sums
        for r in range(n_rows):
            cost[r][c] = partial[r]

    return min([row[-1] for row in cost]), cost


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
    cost, cost_matrix = generate_cost(ingest_data('matrix.txt'))
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