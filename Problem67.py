import time

'''
By starting at the top of the triangle below and moving to adjacent numbers on the row below, 
the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom in triangle.txt (right click and 'Save Link/Target As...'), 
a 15K text file containing a triangle with one-hundred rows.

NOTE: This is a much more difficult version of Problem 18. It is not possible to try every route to solve this problem, 
as there are 299 altogether! If you could check one trillion (1012) routes every second it would take over 
twenty billion years to check them all. There is an efficient algorithm to solve it. ;o)

Louis Keith
5-23-19
'''


class Problem67:

    triangle = []

    @staticmethod
    # opens the triangle file and copies it into a 2d list where each element is a list of string elements
    def get_triangle():
        file = open("p067_triangle.txt", "r")
        lines = file.readlines()
        for i in range(len(lines)):
            Problem67.triangle.append(lines[i].split())
        file.close()

    @staticmethod
    # converts all of the string elements in the 2d triangle array to integer ones
    def convert_to_int():
        for r in range(len(Problem67.triangle)):
            for c in range(len(Problem67.triangle[r])):
                Problem67.triangle[r][c] = int(Problem67.triangle[r][c])

    @staticmethod
    # starting from the second row to the bottom, each number adds the largest number it can see directly below it
    # it repeats this process for every row until the number in the top spot is the largest possible sum
    def get_max_sum():
        for r in reversed(range(len(Problem67.triangle) - 1)):
            for c in range(len(Problem67.triangle[r])):
                if Problem67.triangle[r + 1][c] > Problem67.triangle[r + 1][c + 1]:
                    Problem67.triangle[r][c] += Problem67.triangle[r + 1][c]
                else:
                    Problem67.triangle[r][c] += Problem67.triangle[r + 1][c + 1]
        return Problem67.triangle[0][0]

    @staticmethod
    def main():
        start = time.time()

        Problem67.get_triangle()
        Problem67.convert_to_int()
        print(Problem67.get_max_sum())

        end = time.time()
        print("found in " + str(end - start) + " seconds")


if __name__ == '__main__':
    Problem67.main()
