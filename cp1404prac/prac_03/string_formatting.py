"""
CP1404/CP5632 - Practical
FENG YUAN


Pseudocode:

Function main()
    Define guitar information
    Print different formatting methods
    Print guitar information using f-string formatting
    Print a sequence of right-aligned numbers

Function print_formatting_examples(name, year, cost)
    Print examples of different formatting methods

Function print_guitar_info(name, year, cost)
    Print guitar information using f-string formatting

Function print_right_aligned_numbers()
    Print a sequence of right-aligned numbers

Call function main()
"""


def main():
    """
    Main function.
    """
    name = "Gibson L-5 CES"
    year = 1922
    cost = 16035.4

    print_formatting_examples(name, year, cost)
    print_guitar_info(name, year, cost)
    print_right_aligned_numbers()


def print_formatting_examples(name, year, cost):
    """
    Print examples of different formatting methods.
    """
    print("My guitar: " + name + ", first made in " + str(year))
    print("My guitar: {}, first made in {}".format(name, year))
    print(f"My {name} was first made in {year} (that's right, {year}!)")
    print("My {} would cost ${:,.2f}".format(name, cost))
    print(f"My {name} would cost ${cost:,.2f}")

    numbers = [1, 19, 123, 456, -25]
    for i, number in enumerate(numbers, 1):
        print(f"Number {i} is {number:5}")


def print_guitar_info(name, year, cost):
    """
    Print guitar information using f-string formatting.
    """
    print(f"{year} {name} for about ${cost:,.0f}!")


def print_right_aligned_numbers():
    """
    Print a sequence of right-aligned numbers.
    """
    for i in range(0, 200, 50):
        print(f"{i:>3}")


if __name__ == "__main__":
    main()
