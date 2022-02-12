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
from Problem81 import ingest_data, print_matrix
from Problem82 import write_matrix


def main():
    matrix = ingest_data('test_matrix.txt')
    print(matrix[-1][-1])


if __name__ == '__main__':
    start = time()
    main()
    print('\nFINISHED IN %s SECONDS' % round(time() - start, 4))