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


def get_path_sum(matrix):
    r, c = 0, 0
    r_end, c_end = len(matrix)-1, len(matrix[0])-1
    path_sum = matrix[r][c]

    while (r, c) != (r_end, c_end):
        # check if on bottom row, if so then move right
        if r == r_end:
            c += 1
        # check if on right wall, if so then move down
        elif c == c_end:
            r += 1
        # check if number beneath is less than number to right, if so then move down
        elif matrix[r+1][c] < matrix[r][c+1]:
            r += 1
        # otherwise then move right
        else:
            c += 1
        path_sum += matrix[r][c]
        print('FORWARD: ', matrix[r][c], path_sum)

    return path_sum



def get_backward_sum(matrix):
    r, c = len(matrix)-1, len(matrix[0])-1
    r_end, c_end = 0, 0
    path_sum = matrix[r][c]

    while (r, c) != (r_end, c_end):
        # check if on top row, if so then move left
        if r == r_end:
            c -= 1
        # check if on left wall, if so then move up
        elif c == c_end:
            r -= 1
        # check if number above is less than number to left, if so then move up
        elif matrix[r-1][c] < matrix[r][c-1]:
            r -= 1
        # otherwise then move left
        else:
            c -= 1
        path_sum += matrix[r][c]
        print('BACKWARD: ', matrix[r][c], path_sum)

    return path_sum



def main():
    matrix = ingest_data('test_matrix.txt')
    forward_sum = get_path_sum(matrix)
    print()
    backward_sum = get_backward_sum(matrix)

    print(min(forward_sum, backward_sum))
    


if __name__ == '__main__':
    start = time()
    main()
    print('\nFINISHED IN %s SECONDS' % round(time() - start, 4))