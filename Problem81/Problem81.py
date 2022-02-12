"""
In the 5 by 5 matrix below, the minimal path sum from the top left to the bottom right, 
by only moving to the right and down, is indicated in bold red and is equal to 2427.

/   131   673   234   103    18   \ 
|   201    96   342   965   150   | 
|   630   803   746   422   111   | 
|   537   699   497   121   956   | 
\   805   732   524    37   331   / 

Find the minimal path sum from the top left to the bottom right by only moving right and down in
matrix.txt (right click and "Save Link/Target As..."), a 31K text file containing an 80 by 80 matrix.

Louis Keith
2-11-22
"""

from time import time


def ingest_data(filename='matrix.txt'):
    """Ingest the matrix from disk and split it into a nested list.
    Each element is a list representing a row in the matrix."""
    with open(filename) as f:
        # one-liners are fun
        return [list(map(int, line.split(','))) for line in f.read().split('\n') if line != '']


def get_sum(total_cost):
    """A dynamic programming approach that calculates a total cost function for a matrix.
    Transforms the input matrix to a total cost matrix as it goes along, no extra memory required.
    Returns the minimum cost to traverse the entire matrix from top right to bottom left."""
    r_end, c_end = len(total_cost[0]) - 1, len(total_cost) - 1

    # populate the first row and first column with their respective costs to reach
    for c in range(1, c_end + 1):
        total_cost[0][c] += total_cost[0][c-1]
    for r in range(1, r_end + 1):
        total_cost[r][0] += total_cost[r-1][0]

    # populate the rest of the total cost matrix
    for r in range(1, r_end + 1):
        for c in range(1, c_end + 1):
            total_cost[r][c] += min(total_cost[r-1][c],
                                    total_cost[r][c-1])

    return total_cost[r_end][c_end]


def main():
    print(get_sum(ingest_data()))
    

if __name__ == '__main__':
    start = time()
    main()
    print('\nFINISHED IN %s SECONDS' % round(time() - start, 4))