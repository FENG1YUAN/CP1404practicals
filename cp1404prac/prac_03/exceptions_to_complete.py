"""
CP1404/CP5632 - Practical
FENG YUAN

This code asks the user for a valid integer input. It keeps requesting until a valid integer is given,
catching any ValueError that is thrown when trying to convert the input into an integer.
"""


def main():
    """
    Main function that drives the program.
    It repeatedly requests the user for a valid integer and handles any ValueError until a valid integer is given.
    """
    is_finished = False
    while not is_finished:
        try:
            result = int(input("Enter a valid integer: "))
            is_finished = True
        except ValueError:
            print("Please enter a valid integer.")
    print("Valid result is:", result)


if __name__ == "__main__":
    main()
