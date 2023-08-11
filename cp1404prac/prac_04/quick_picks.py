"""
CP1404/CP5632 - Practical
FENG YUAN

Emails to Names
Estimate: 15 minutes
Actual: 25 minutes
Pseudo-code:

The code uses a main function to ask the user for the number of quick picks they want,
then generate and print that many quick picks.

Each quick pick is a sorted list of 6 unique random numbers between a defined minimum and maximum.
A loop is used to generate a new unique random number,
check if it's already in the list,
and add it to the list if it's not.
After all 6 numbers for a quick pick are generated,
the list is sorted and printed.

The program continues to ask for the number of quick picks until the user enters a non-negative number.
"""

import random

NUMBERS_PER_LINE = 6
MINIMUM = 1
MAXIMUM = 45


def main():
    """
    The main function of the program.
    It asks the user how many quick picks they want,
    and for each quick pick, it generates a sorted list of 6 random numbers.
    """
    num_quick_picks = int(input("How many quick picks? "))
    while num_quick_picks < 0:
        print("That makes no sense!")
        num_quick_picks = int(input("How many quick picks? "))

    for i in range(num_quick_picks):
        quick_pick = []
        for _ in range(NUMBERS_PER_LINE):
            number = random.randint(MINIMUM, MAXIMUM)
            while number in quick_pick:
                number = random.randint(MINIMUM, MAXIMUM)
            quick_pick.append(number)
        quick_pick.sort()
        print(" ".join("{:2}".format(number) for number in quick_pick))


if __name__ == '__main__':
    main()

