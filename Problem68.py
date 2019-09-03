import time
import sys

'''
Consider the following "magic" 3-gon ring, filled with the numbers 1 to 6, and each line adding to nine.

Working clockwise, and starting from the group of three with the numerically lowest external node 
(4,3,2 in this example), each solution can be described uniquely. For example, 
the above solution can be described by the set: 4,3,2; 6,2,1; 5,1,3.

It is possible to complete the ring with four different totals: 9, 10, 11, and 12. There are eight solutions in total.

Total	Solution Set
9	4,2,3; 5,3,1; 6,1,2
9	4,3,2; 6,2,1; 5,1,3
10	2,3,5; 4,5,1; 6,1,3
10	2,5,3; 6,3,1; 4,1,5
11	1,4,6; 3,6,2; 5,2,4
11	1,6,4; 5,4,2; 3,2,6
12	1,5,6; 2,6,4; 3,4,5
12	1,6,5; 3,5,4; 2,4,6
By concatenating each group it is possible to form 9-digit strings; the maximum string for a 3-gon ring is 432621513.

Using the numbers 1 to 10, and depending on arrangements, it is possible to form 16- and 17-digit strings. 
What is the maximum 16-digit string for a "magic" 5-gon ring?

Louis Keith
5-24-19
'''


class Problem68:

    solutions = []

    @staticmethod
    # iterates through the solution list and returns the one with the largest numerical value
    def find_largest_solution():
        largest = -sys.maxsize - 1
        for solution in Problem68.solutions:
            if int(solution) > largest:
                largest = int(solution)
        return largest

    @staticmethod
    # a method for printing solutions for debugging purposes
    def print_solutions():
        for solution in Problem68.solutions:
            print(solution)

    @staticmethod
    # takes the three solutions and orders them to be clockwise starting from the one with the smallest outer node
    # returns a string with the result and only works for the magic 3-gon
    def order_solutions_three_gon(s1, s2, s3):
        solution = ""

        # finding the smallest out node
        smallest_out = s1[0]
        if s2[0] < smallest_out:
            smallest_out = s2[0]
        if s3[0] < smallest_out:
            smallest_out = s3[0]

        # ordering
        if s1[0] == smallest_out:
            for n in s1:
                solution += str(n)
            for n in s2:
                solution += str(n)
            for n in s3:
                solution += str(n)
        elif s2[0] == smallest_out:
            for n in s2:
                solution += str(n)
            for n in s3:
                solution += str(n)
            for n in s1:
                solution += str(n)
        else:
            for n in s3:
                solution += str(n)
            for n in s1:
                solution += str(n)
            for n in s2:
                solution += str(n)

        return solution

    @staticmethod
    # actually generates all of the unique solutions related to a magic 3-gon ring
    def three_gon():
        valid_numbers = range(1, 7)
        used_numbers = [0, 0, 0, 0, 0, 0]
        for s1_base in valid_numbers:
            used_numbers[0] = s1_base
            for s2_base in valid_numbers:
                if s2_base in used_numbers:
                    continue
                used_numbers[1] = s2_base
                for s3_base in valid_numbers:
                    if s3_base in used_numbers:
                        continue
                    used_numbers[2] = s3_base
                    for s1_out in valid_numbers:
                        if s1_out in used_numbers:
                            continue
                        used_numbers[3] = s1_out
                        s1 = [s1_out, s1_base, s2_base]
                        target_sum = s1_out + s1_base + s2_base
                        for s2_out in valid_numbers:
                            if s2_out in used_numbers:
                                continue
                            used_numbers[4] = s2_out
                            s2 = [s2_out, s2_base, s3_base]
                            s2_sum = s2_out + s2_base + s3_base
                            if s2_sum != target_sum:
                                used_numbers[4] = 0
                                continue
                            for s3_out in valid_numbers:
                                if s3_out in used_numbers:
                                    continue
                                used_numbers[5] = s3_out
                                s3 = [s3_out, s3_base, s1_base]
                                s3_sum = s3_out + s3_base + s1_base
                                if s3_sum != target_sum:
                                    used_numbers[5] = 0
                                    continue

                                solution = Problem68.order_solutions_three_gon(s1, s2, s3)
                                if solution not in Problem68.solutions:
                                    Problem68.solutions.append(solution)

                                used_numbers[5] = 0
                            used_numbers[4] = 0
                        used_numbers[3] = 0
                    used_numbers[2] = 0
                used_numbers[1] = 0
            used_numbers[0] = 0

    @staticmethod
    # order solutions method for the more complicated magic 5-gon
    def order_solutions_five_gon(s1, s2, s3, s4, s5):
        solution = ""

        # finding the smallest out node
        nodes = [s1[0], s2[0], s3[0], s4[0], s5[0]]
        smallest_out = sys.maxsize
        for node in nodes:
            if node < smallest_out:
                smallest_out = node

        # ordering
        if s1[0] == smallest_out:
            for n in s1:
                solution += str(n)
            for n in s2:
                solution += str(n)
            for n in s3:
                solution += str(n)
            for n in s4:
                solution += str(n)
            for n in s5:
                solution += str(n)
        elif s2[0] == smallest_out:
            for n in s2:
                solution += str(n)
            for n in s3:
                solution += str(n)
            for n in s4:
                solution += str(n)
            for n in s5:
                solution += str(n)
            for n in s1:
                solution += str(n)
        elif s3[0] == smallest_out:
            for n in s3:
                solution += str(n)
            for n in s4:
                solution += str(n)
            for n in s5:
                solution += str(n)
            for n in s1:
                solution += str(n)
            for n in s2:
                solution += str(n)
        elif s4[0] == smallest_out:
            for n in s4:
                solution += str(n)
            for n in s5:
                solution += str(n)
            for n in s1:
                solution += str(n)
            for n in s2:
                solution += str(n)
            for n in s3:
                solution += str(n)
        else:
            for n in s5:
                solution += str(n)
            for n in s1:
                solution += str(n)
            for n in s2:
                solution += str(n)
            for n in s3:
                solution += str(n)
            for n in s4:
                solution += str(n)

        if len(solution) == 17:
            return -1
        return solution

    @staticmethod
    # actually generates all of the unique solutions related to a magic 3-gon ring
    def five_gon():
        valid_numbers = range(1, 11)
        # tracks which numbers have been used already for the current solution
        used_numbers = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        # the second and third numbers of the solution set are actually cyclical
        # this generates all possible cyclical 2 number sets in the valid_numbers range
        for s1_base in valid_numbers:
            used_numbers[0] = s1_base
            for s2_base in valid_numbers:
                if s2_base in used_numbers:
                    continue
                used_numbers[1] = s2_base
                for s3_base in valid_numbers:
                    if s3_base in used_numbers:
                        continue
                    used_numbers[2] = s3_base
                    for s4_base in valid_numbers:
                        if s4_base in used_numbers:
                            continue
                        used_numbers[3] = s4_base
                        for s5_base in valid_numbers:
                            if s5_base in used_numbers:
                                continue
                            used_numbers[4] = s5_base

                            # first digit of each solution must be in the valid numbers,
                            # not be in the used numbers, and all must sum equally
                            for s1_out in valid_numbers:
                                if s1_out in used_numbers:
                                    continue
                                used_numbers[5] = s1_out
                                target_sum = s1_out + s1_base + s2_base
                                for s2_out in valid_numbers:
                                    if s2_out in used_numbers:
                                        continue
                                    used_numbers[6] = s2_out
                                    s2_sum = s2_out + s2_base + s3_base
                                    if s2_sum != target_sum:
                                        used_numbers[6] = 0
                                        continue
                                    for s3_out in valid_numbers:
                                        if s3_out in used_numbers:
                                            continue
                                        used_numbers[7] = s3_out
                                        s3_sum = s3_out + s3_base + s4_base
                                        if s3_sum != target_sum:
                                            used_numbers[7] = 0
                                            continue
                                        for s4_out in valid_numbers:
                                            if s4_out in used_numbers:
                                                continue
                                            used_numbers[8] = s4_out
                                            s4_sum = s4_out + s4_base + s5_base
                                            if s4_sum != target_sum:
                                                used_numbers[8] = 0
                                                continue
                                            for s5_out in valid_numbers:
                                                if s5_out in used_numbers:
                                                    continue
                                                used_numbers[9] = s5_out
                                                s5_sum = s5_out + s5_base + s1_base
                                                if s5_sum != target_sum:
                                                    used_numbers[9] = 0
                                                    continue

                                                s1 = [s1_out, s1_base, s2_base]
                                                s2 = [s2_out, s2_base, s3_base]
                                                s3 = [s3_out, s3_base, s4_base]
                                                s4 = [s4_out, s4_base, s5_base]
                                                s5 = [s5_out, s5_base, s1_base]

                                                solution = Problem68.order_solutions_five_gon(s1, s2, s3, s4, s5)
                                                if solution not in Problem68.solutions:
                                                    Problem68.solutions.append(solution)

                                                # every time a loop completes the place it was responsible for checking
                                                # must be reset accordingly
                                                used_numbers[9] = 0
                                            used_numbers[8] = 0
                                        used_numbers[7] = 0
                                    used_numbers[6] = 0
                                used_numbers[5] = 0
                            used_numbers[4] = 0
                        used_numbers[3] = 0
                    used_numbers[2] = 0
                used_numbers[1] = 0
            used_numbers[0] = 0

    @staticmethod
    def main():
        start = time.time()

        Problem68.five_gon()
        print(Problem68.find_largest_solution())

        end = time.time()
        print("found in " + str(end - start) + " seconds")


if __name__ == '__main__':
    Problem68.main()
