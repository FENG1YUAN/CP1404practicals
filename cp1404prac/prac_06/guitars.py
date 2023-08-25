"""
Author: FENG YUAN
Time: 12 minutes

Pseudocode for Guitars:
1. Import the Guitar class.
2. Define the main function.
    a. Initialize an empty list called guitars.
    b. Print "My guitars!".
    c. Skip user input for guitar details.
    d. Append hard-coded guitar objects for testing.
    e. Print a separator "... snip ...".
    f. Print "These are my guitars:".
    g. Enumerate through the guitars list and print each guitar's details with its vintage status if applicable.
3. If this script is the main module, execute the main function.
"""

from guitar import Guitar


def main():
    guitars = []
    print("My guitars!")

    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))
    guitars.append(Guitar("Fender Stratocaster", 2014, 765.4))

    print("\n... snip ...\n")
    print("These are my guitars:")

    for i, guitar in enumerate(guitars, 1):
        vintage_string = " (vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")


if __name__ == "__main__":
    main()