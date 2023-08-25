"""
Author: FENG YUAN
Time: 25 minutes

Pseudocode:

1. Initialize the ProgrammingLanguage class.
   a . Accept attributes - name, typing, reflection, and year during initialization.
   b . Store these attributes in instance variables.

2. Define a method 'is_dynamic':
   a . Check if the typing attribute of the instance is 'Dynamic'.
   b . Return True if it is, else return False.

3. Define a string representation for the class (__str__ method):
   a . Return a formatted string with all the attributes displayed.

4. End of the class definition.
"""


class ProgrammingLanguage:
    """Represent a Programming Language object."""

    def __init__(self, name, typing, reflection, year):
        """Initialise a ProgrammingLanguage instance."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Determine if the language is dynamically typed."""
        return self.typing == "Dynamic"

    def __str__(self):
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"
