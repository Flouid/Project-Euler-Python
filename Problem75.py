import time
import math
from Problem73 import Problem73

'''
It turns out that 12 cm is the smallest length of wire that can be bent to form an integer sided right angle triangle
in exactly one way, but there are many more examples.

12 cm: (3,4,5)
24 cm: (6,8,10)
30 cm: (5,12,13)
36 cm: (9,12,15)
40 cm: (8,15,17)
48 cm: (12,16,20)

In contrast, some lengths of wire, like 20 cm, cannot be bent to form an integer sided right angle triangle,
and other lengths allow more than one solution to be found; for example, using 120 cm it is possible to form 
exactly three different integer sided right angle triangles.

120 cm: (30,40,50), (20,48,52), (24,45,51)

Given that L is the length of the wire, for how many values of L ≤ 1,500,000 
can exactly one integer sided right angle triangle be formed?

Louis Keith
5-28-19
'''


class Problem75:

    @staticmethod
    def main():
        start = time.time()

        # so this is another heavy number theory one i believe. The fundamental question is how many c below 1,500,000
        # belong to exactly one pythagorean triple a^2 + b^2 = c^2.
        # from wikipedia, Euclid's formula offers a way of generating pythagorean triples:
        # a = m^2 - n^2; b = 2mn; c = m^2 + n^2 for arbitrary integers m > n > 0
        # furthermore: "Every primitive triple arises (after the exchange of a and b, if a is even) from a unique pair
        # of coprime numbers m, n, one of which is even." This means that we should be able to easily generate all
        # of the primitive triples for c <= 1,500,000 and then the non primitive ones can be easily filled in by
        # stepping through multiples of primitive ones

        limit = 1500000
        # each index on this list represents a wire, each element will contain the number of ways to make a triangle
        triple_sums = [0] * limit
        result = 0
        for m in range(2, int(math.sqrt(limit / 2))):
            for n in range(1, m):
                # if exactly one of them is even and they are relatively prime
                if (m + n) % 2 == 1 and Problem73.gcd(m, n) == 1:
                    # a + b + c as described above, the n^2 terms cancel out
                    triple_sum = 2*m**2 + 2*m*n
                    original_triple_sum = triple_sum
                    # once a sum is found, step through each of its multiples
                    while triple_sum < limit:
                        triple_sums[triple_sum] += 1
                        # if a number can be made into a perfect right triangle, increment the counter
                        if triple_sums[triple_sum] == 1:
                            result += 1
                        # if it was found that there was more than one triangle for this number, decrement the counter
                        # as the statement before this has necessarily triggered once already
                        elif triple_sums[triple_sum] == 2:
                            result -= 1
                        triple_sum += original_triple_sum

        print(result)

        end = time.time()
        print("found in " + str(end - start) + " seconds")


if __name__ == '__main__':
    Problem75.main()
