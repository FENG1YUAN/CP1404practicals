"""
Author: FENG YUAN
Time: 30 minutes

Pseudocode:

Attributes:
1. name: The name of the car. Defaulted to "Car".
2. fuel: The amount of fuel in the car. One unit of fuel is assumed to drive one kilometre.
3. _odometer: This keeps track of the total distance driven by the car. Initialized as 0 and is private.

Methods:
1. __init__(self, name="Car", fuel=0): Constructor method that initializes a Car object.
2. add_fuel(self, amount): Adds the specified amount to the car's fuel.
3. drive(self, distance): Attempts to drive the car the specified distance. If there's not enough fuel, the car
drives until the fuel runs out.
4. __str__(self): A special method that returns a string representation of the Car object.

When a Car object is initialized, it can be given a name and initial fuel. The drive method simulates driving the car
by reducing the fuel and increasing the odometer. The string representation of the car shows its name, current fuel,
and odometer reading.
"""


class Car:
    """Represent a Car object."""

    def __init__(self, name="Car", fuel=0):
        """Initialise a Car instance.

        Parameters:
        name (str): Name of the car. Default is "Car".
        fuel (float): Initial fuel amount. One unit of fuel drives one kilometre. Default is 0.
        """
        self.name = name
        self.fuel = fuel
        self._odometer = 0

    def add_fuel(self, amount):
        """Add specified amount to the car's fuel.

        Parameters:
        amount (float): Amount of fuel to be added.
        """
        self.fuel += amount

    def drive(self, distance):
        """Drive the car a specified distance.

        If the car has enough fuel, it drives the specified distance.
        Otherwise, it drives until the fuel runs out.
        The odometer updates accordingly.

        Parameters:
        distance (float): Desired driving distance.

        Returns:
        float: Actual distance driven.
        """
        if distance > self.fuel:
            distance = self.fuel
            self.fuel = 0
        else:
            self.fuel -= distance
        self._odometer += distance
        return distance

    def __str__(self):
        """Return a string representation of the Car object.

        Returns:
        str: String containing the name, fuel level, and odometer reading of the car.
        """
        return f"{self.name}, fuel={self.fuel}, odometer={self._odometer}"
