"""
Author: Feng Yuan
Time to Complete: 15 minutes
Pseudo-code Repository: https://github.com/FENG1YUAN/CP1404practicals/tree/prac_09_feedback/cp1404prac

Pseudo Code:
1. Import the random library and Car class from the specified module.
2. Define an UnreliableCar class, which inherits from Car.
3. Inside the UnreliableCar class:
    - Implement the constructor (__init__) to initialize the name, fuel, and a new property called reliability.
    - Implement a drive method that overrides the parent Car's drive method.
        - Generate a random number between 0 and 100.
        - Compare the random number with the car's reliability.
        - If the random number is less than the reliability, call the parent's drive method.
        - Otherwise, the car doesn't move, so return 0.

"""

import random
from cp1404prac.prac_09.car import Car


class UnreliableCar(Car):
    """UnreliableCar class inherits from Car and adds a reliability factor."""

    def __init__(self, name, fuel, reliability):
        """Initialize UnreliableCar attributes including a new attribute reliability."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive the car based on its reliability."""
        random_chance = random.uniform(0, 100)

        if random_chance < self.reliability:
            return super().drive(distance)
        else:
            return 0
