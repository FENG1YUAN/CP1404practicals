"""
Author: FENG YUAN
Time: 15 minutes

Pseudocode for Guitar Class:
1. Define the Guitar class.
    a. Initialize the guitar with a name, year, and cost.
    b. String representation of the Guitar: [name] ([year]) : [$cost]
    c. Method to get the age of the guitar:
        i. Calculate the age as the difference between current year (2022) and the guitar's year.
    d. Method to check if the guitar is vintage:
        i. A guitar is vintage if its age is 50 or more years.
"""


class Guitar:
    """Represent a Guitar object."""

    def __init__(self, name="", year=0, cost=0):
        """Initialise a Guitar instance with name, year, and cost."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):
        """Return the age of the guitar based on the current year."""
        current_year = 2022  # In this example, I'm using 2022. You might want to dynamically get the current year.
        return current_year - self.year

    def is_vintage(self):
        """Return True if the guitar is 50 or more years old, False otherwise."""
        return self.get_age() >= 50
