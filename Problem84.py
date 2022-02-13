"""
In the game, Monopoly, the standard board is set up in the following way:

A player starts on the GO square and adds the scores on two 6-sided dice to determine 
the number of squares they advance in a clockwise direction. Without any further rules 
we would expect to visit each square with equal probability: 2.5%. However, 
landing on G2J (Go To Jail), CC (community chest), and CH (chance) changes this distribution.

In addition to G2J, and one card from each of CC and CH, that orders the player to go 
directly to jail, if a player rolls three consecutive doubles, they do not advance the 
result of their 3rd roll. Instead they proceed directly to jail.

At the beginning of the game, the CC and CH cards are shuffled. 
When a player lands on CC or CH they take a card from the top of the respective pile and, 
after following the instructions, it is returned to the bottom of the pile. 
There are sixteen cards in each pile, but for the purpose of this problem we are only 
concerned with cards that order a movement; any instruction not concerned with movement 
will be ignored and the player will remain on the CC/CH square.

Community Chest (2/16 cards):
1. Advance to GO
2. Go to JAIL
Chance (10/16 cards):
1.  Advance to GO
2.  Go to JAIL
3.  Go to C1
4.  Go to E3
5.  Go to H2
6.  Go to R1
7.  Go to next R (railway company)
8.  Go to next R
9.  Go to next U (utility company)
10. Go back 3 squares.

The heart of this problem concerns the likelihood of visiting a particular square. 
That is, the probability of finishing at that square after a roll. For this reason 
it should be clear that, with the exception of G2J for which the probability of 
finishing on it is zero, the CH squares will have the lowest probabilities, as 
5/8 request a movement to another square, and it is the final square that the player 
finishes at on each roll that we are interested in. We shall make no distinction between 
"Just Visiting" and being sent to JAIL, and we shall also ignore the rule about requiring 
a double to "get out of jail", assuming that they pay to get out on their next turn.

By starting at GO and numbering the squares sequentially from 00 to 39 we can concatenate 
these two-digit numbers to produce strings that correspond with sets of squares.

Statistically it can be shown that the three most popular squares, in order, 
are JAIL (6.24%) = Square 10, E3 (3.18%) = Square 24, and GO (3.09%) = Square 00. 
So these three most popular squares can be listed with the six-digit modal string: 102400.

If, instead of using two 6-sided dice, two 4-sided dice are used, find the six-digit modal string.

Louis Keith
2-12-22
"""


from time import time
import random


def generate_board():
    """Generates the game board encoded as a list of strings from '00' to '39'"""
    board = []
    for tens in range(4):
        for ones in range(10):
            board.append(str(tens) + str(ones))
    return board


def generate_chest():
    """Generates the community chest pile encoded as a list.
    Empty strings represent irrelevant cards and integers encode a space to move to.
    Shuffles the list upon reterning to represent the pile being shuffled at the start of the game."""
    chest = [0, 10] + [''] * 14
    random.shuffle(chest)
    return chest


def generate_chance():
    """Generates the chance pile encoded as a list.
    Empty strings represent irrelevant cards and integers encode a space to move to.
    The exceptions of this are 'R', 'U', and 'B' which represent special move logic. 
    Shuffles the list upon reterning to represent the pile being shuffled at the start of the game."""
    chance = [0, 10, 11, 24, 39, 5, 'R', 'R', 'U', 'B'] + [''] * 6
    random.shuffle(chance)
    return chance


def generate_roll(sides):
    """Generate a random roll of two dice with a given amount of sides."""
    return random.randint(1, sides) + random.randint(1, sides)


def simulate_game(rolls, sides):
    """Simulate the game for a given amount of rolls and return a histogram of the most commonly
    encountered spaces. Position on the board is encoded as a simple index."""
    board = generate_board()
    chest = generate_chest()
    chance = generate_chance()
    pos = 0
    pos_chest = 0
    pos_chance = 0
    histogram = [0] * 40

    for _ in range(rolls):
        pos = (pos + generate_roll(sides)) % 40
        # roll landed on chance pile
        if pos == 7 or pos == 22 or pos == 36:
            # draw a card and rollover if all cards have been drawn
            card = chance[pos_chance % 16]
            # move backward 3
            if card == 'B':
                pos = (pos - 3) % 40
            # move to the next railroad
            elif card == 'R':
                # if on the first chest, move to R2
                if pos == 7:
                    pos = 15
                # if on the second chest, move to R3
                elif pos == 22:
                    pos = 25
                # if on the third chest, move to R1
                else:
                    pos = 5
            # move to the next utility
            elif card == 'U':
                # if on the first or third chest, move to U1
                if pos == 7 or pos == 36:
                    pos = 12
                # if on the second chest, move to U2
                else:
                    pos = 28
            # if the card encodes a position, move there
            elif card != '':
                pos = card
            pos_chance += 1
        # roll landed on community chest
        elif pos == 2 or pos == 17 or pos == 33: 
            # draw a card and rollover if all cards have been drawn
            card = chest[pos_chest % 16]
            # if the card is relevant then move to the place it encodes
            if card != '':
                pos = card
            pos_chest += 1
        # go to jail space
        if pos == 30:
            pos = 10
        # record the roll in the frequency histogram
        histogram[pos] += 1

    # find the top 3 elements in the historgram and store their indices
    i1, i2, i3 = -1, -1, -1
    f, s, t = -1, -1, 1
    for i in range(40):
        n = histogram[i]
        if n > f:
            f, s, t = n, f, s
            i1, i2, i3 = i, i1, i2
        elif n > s:
            s, t = n, s
            i2, i3 = i, i2
        elif n > t:
            t = n
            i3 = i

    # print the model string
    print(board[i1] + board[i2] + board[i3])


def main():
    simulate_game(100000, 4)
    

if __name__ == '__main__':
    start = time()
    main()
    print('\nFINISHED IN %s SECONDS' % round(time() - start, 4))