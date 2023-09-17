"""
Author: Feng Yuan
Time to Complete: 10 minutes
Pseudo-code Repository: https://github.com/FENG1YUAN/CP1404practicals/tree/prac_09_feedback/cp1404prac

Pseudo Code:
1. Define Band class.
2. Initialize Band with a name and empty Musicians list.
3. Implement string representation for Band.
4. Add a musician to the Band.
5. Simulate each musician playing their instrument.

"""


class Band:
    """Band class represents a musical band."""

    def __init__(self, name=""):
        """Construct a Band with a name and an empty Musicians collection."""
        self.name = name
        self.musicians = []

    def __str__(self):
        """Return a string representation of a Band."""
        return f"{self.name} ({', '.join(map(str, self.musicians))})"

    def add(self, musician):
        """Add a musician to the Band's collection."""
        self.musicians.append(musician)

    def play(self):
        """Simulate each musician in the Band playing their first (or no) instrument."""
        return '\n'.join(musician.play() for musician in self.musicians)
