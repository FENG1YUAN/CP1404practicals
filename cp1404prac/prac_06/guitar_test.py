"""
Author: FENG YUAN
Time: 10 minutes

Pseudocode for Guitar Test:
1. Import the Guitar class.
2. Define the main function.
    a. Create two Guitar objects: guitar1 and guitar2.
    b. Test the get_age() method for both guitars and print the expected and actual results.
    c. Test the is_vintage() method for both guitars and print the expected and actual results.
3. Execute the main function.
"""

from guitar import Guitar


def main():
    guitar1 = Guitar("Gibson L-5 CES", 1922, 16035.40)
    guitar2 = Guitar("Another Guitar", 2013, 825.5)

    print(f"{guitar1.name} get_age() - Expected 100. Got {guitar1.get_age()}")
    print(f"{guitar2.name} get_age() - Expected 9. Got {guitar2.get_age()}")

    print(f"{guitar1.name} is_vintage() - Expected True. Got {guitar1.is_vintage()}")
    print(f"{guitar2.name} is_vintage() - Expected False. Got {guitar2.is_vintage()}")


main()
