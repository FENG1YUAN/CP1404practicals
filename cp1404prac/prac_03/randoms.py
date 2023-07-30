"""
CP1404/CP5632 - Practical
FENG YUAN


Import the random module

Define function main:
    Print the statement "Generate a random integer between 5 and 20"
    Generate a random integer between 5 and 20 using random.randint function, and store the result in val1
    Print the generated value val1

    Print the statement "Generate a random integer from range 3 to 10 (step=2)"
    Generate a random integer from 3 to 10 with step size of 2 using random.randrange function, and store the result in
    val2
    Print the generated value val2

    Print the statement "Generate a random floating point number between 2.5 and 5.5"
    Generate a random floating point number between 2.5 and 5.5 using random uniform function, and store the result in
    val3
    Print the generated value val3

    Print the statement "Generate a random integer between 1 and 100 inclusive"
    Generate a random integer between 1 and 100 using random.randint function, and store the result in val4
    Print the generated value val4

Check if the script is running directly (i.e., not being imported)
    If true, call function main

End Program

"""

import random


def main():
    """
    Main function that drives the program.
    """

    print("\nGenerate a random integer between 5 and 20")
    val1 = random.randint(5, 20)  # Smallest number could be 5, largest could be 20
    print("Generated value:", val1)

    print("\nGenerate a random integer from range 3 to 10 (step=2)")
    val2 = random.randrange(3, 10, 2)  # Smallest number could be 3, largest could be 9. It can't produce 4 because
    # step=2
    print("Generated value:", val2)

    print("\nGenerate a random floating point number between 2.5 and 5.5")
    val3 = random.uniform(2.5, 5.5)  # Smallest number could be 2.5, largest could be 5.5
    print("Generated value:", val3)

    print("\nGenerate a random integer between 1 and 100 inclusive")
    val4 = random.randint(1, 100)
    print("Generated value:", val4)


if __name__ == "__main__":
    main()
