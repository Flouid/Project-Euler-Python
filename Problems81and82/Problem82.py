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
from Problem81 import ingest_data, print_matrix


def find_path(matrix):
    return 0


def main():
    print_matrix(ingest_data('test_matrix.txt'))
    

if __name__ == '__main__':
    start = time()
    main()
    print('\nFINISHED IN %s SECONDS' % round(time() - start, 4))