import time

'''
A common security method used for online banking is to ask the user for three random characters from a passcode. 
For example, if the passcode was 531278, they may ask for the 2nd, 3rd, and 5th characters; the expected reply would be:
317.

The text file, keylog.txt, contains fifty successful login attempts.

Given that the three characters are always asked for in order, analyse the file so as to determine the 
shortest possible secret passcode of unknown length.

Louis Keith
8-5-19
'''


class Problem79:

    # the basic idea i'm getting looking at this is to make a program that will just smart merge these successful login
    # attempts until it has found a passcode matching all of them

    #################################################################################################################

    # that worked surprisingly easily, this code probably isn't comprehensive as i just kept adding rules as I saw
    # scenarios that broke the existing ones until it spit out an answer

    @staticmethod
    def main():
        start = time.time()

        logins = Problem79.get_logins()
        # the goal is merging all of the logins into one passcode
        while len(logins) > 1:
            # if the first digit of the second passcode is in the first
            if logins[1][0] in logins[0]:
                first_index = logins[0].index(logins[1][0])
                # if the second digit of the second passcode is in the first
                if logins[1][1] in logins[0]:
                    second_index = logins[0].index(logins[1][1])
                    if first_index < second_index:
                        # if the third digit of the second passcode is in the first
                        if logins[1][2] in logins[0]:
                            # this login offered no new info this iteration and can be removed
                            logins.remove(logins[1])
                    else:
                        # all the right digits are there they just need to be swapped
                        temp = logins[0][first_index]
                        logins[0][first_index] = logins[0][second_index]
                        logins[0][second_index] = temp
                else:
                    # the first digit was in the passcode but the second wasn't, so put it after the first
                    logins[0] = logins[0][0:first_index + 1] + list(logins[1][1]) + logins[0][first_index + 1:]
            # if the second digit of the second passcode is in the first
            elif logins[1][1] in logins[0]:
                first_index = logins[0].index(logins[1][1])
                # if the third digit of the second passcode is in the first
                if logins[1][2] in logins[0]:
                    second_index = logins[0].index(logins[1][2])
                    if first_index < second_index:
                        # the last two digits were present but the first was not, so it was inserted before the second
                        logins[0] = logins[0][0:first_index] + list(logins[1][0]) + logins[0][first_index:]
            else:
                # no digits matched at all, just throw it on the end
                logins[0] = logins[0] + logins[1]
                logins.remove(logins[1])
        print("".join(logins[0]))

        end = time.time()
        print("found in " + str(end - start) + " seconds")

    @staticmethod
    # opens the keylog file and strips out the '\n' on every line, then returns it as a list of lists of chars
    # also strips unnecessary duplicates out
    def get_logins():
        file = open("p079_keylog.txt", "r")
        raw = file.readlines()
        logins = []
        for i in range(len(raw)):
            raw[i] = raw[i][0:3]
            if raw[i] not in logins:
                logins.append(list(raw[i]))
        file.close()
        return logins


if __name__ == '__main__':
    Problem79.main()
