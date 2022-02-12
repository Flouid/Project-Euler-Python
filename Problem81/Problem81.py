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
from turtle import back


def ingest_data(filename='matrix.txt'):
    """Ingest the matrix from disk and split it into a nested list.
    Each element is a list representing a row in the matrix."""
    with open(filename) as f:
        # read rows
        data = f.read().split('\n')
        # split rows into individual lists of integers
        data = [list(map(int, line.split(','))) for line in data if line != '']
    return data


def get_sum(r, c):
    """A recursive function to calculate the minimum cost to get to
    the end from a given coordinate position."""
    cost = matrix[r][c]

    # if at the end, just return the cost of the cell
    if (r, c) == (r_end, c_end):
        return cost
    # if in the bottom row, traverse left
    elif r == r_end:
        return cost + get_sum(r, c+1)
    # if in the rightmost column, traverse down
    elif c == c_end:
        return cost + get_sum(r+1, c)
    # otherwise, explore both paths and return the minimum
    else:
        return cost + min(get_sum(r+1, c), get_sum(r, c+1))
    

if __name__ == '__main__':
    start = time()
    matrix = ingest_data()
    r_end, c_end = len(matrix)-1, len(matrix[0])-1
    print(get_sum(65, 65))
    print('\nFINISHED IN %s SECONDS' % round(time() - start, 4))