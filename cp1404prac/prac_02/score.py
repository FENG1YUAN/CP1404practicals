"""
CP1404/CP5632 - Practical
FENG YUAN
Pseudocode:

The code uses a main function to ask the user for their score,
then print the result.
A new function get_score_status(score) takes in the user's score as a parameter
and returns the result to be printed.
"""

import random


def main():
    """
    Main function that drives the program.
    It asks for the user's score, prints the result,
    generates a random score and prints the result.
    """
    print("Welcome to the Score Status Program.")
    score = float(input("Enter score: "))
    print(get_score_status(score))

    random_score = random.randint(0, 100)
    print(f"Random Score: {random_score}, Result: {get_score_status(random_score)}")


def get_score_status(score):
    """
    Function to determine the status of the score.
    """
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
