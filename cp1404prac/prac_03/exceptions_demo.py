"""
CP1404/CP5632 - Practical
FENG YUAN


1. When does ValueError occur?
   ValueError occurs if the input is not a number.

2. Under what circumstances does a divide by zero error occur?
   A divide by zero error occurs if the denominator is zero

3. Can the code be modified to avoid a divide by zero error?
   Yes, the code can be modified to check if the denominator is zero before performing division
"""


def main():
    """
    Main function that drives the program.
    It asks for the user's score, prints the result,
    generates a random score and prints the result.
    """
    try:
        numerator = int(input("Enter the numerator: "))
        denominator = int(input("Enter the denominator: "))
        if denominator == 0:
            print("Denominator cannot be zero. Please enter a non-zero value.")
        else:
            fraction = numerator / denominator
            print(fraction)
    except ValueError:
        print("Numerator and denominator must be valid numbers!")
    print("Finished.")


if __name__ == "__main__":
    main()
