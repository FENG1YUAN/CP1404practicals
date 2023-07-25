"""
CP1404/CP5632 - Practical
FENG YUAN
Pseudocode:

This code uses a main function to control the program and uses a menu system.
The user can choose to get a valid score, print the result of the score,
show as many stars as the score, or quit the program.
"""


def main():
    """
    Main function that drives the program.
    It displays a menu to the user and handles the user's choice.
    """
    score = get_valid_score()
    menu = """(G)Get a valid score
(P)print result
(S)show stars
(Q)quit"""
    print(menu)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            print(get_score_status(score))
        elif choice == "S":
            print_stars(score)
        else:
            print("Invalid option")
        print(menu)
        choice = input(">>> ").upper()
    print("Farewell. Thank you for using the Score Status Program.")


def get_valid_score():
    """
    Function to get a valid score from the user.
    """
    score = float(input("Enter a valid score (0-100 inclusive): "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = float(input("Enter a valid score (0-100 inclusive): "))
    return score


def get_score_status(score):
    """
    Function to determine the status of the score.
    """
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


def print_stars(score):
    """
    Function to print as many stars as the score.
    """
    print("*" * int(score))


main()
