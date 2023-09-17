"""
Author: Feng Yuan
Time to Complete: 30 minutes
Pseudo-code Repository: https://github.com/FENG1YUAN/CP1404practicals/tree/prac_09_feedback/cp1404prac

Pseudo Code:
1. Import Car class from cp1404prac.prac_09.car.
2. Define Taxi class, inherited from Car.
3. Initialize Taxi instance with a name, fuel, and current fare distance.
4. Implement a custom string representation.
5. Calculate and return the fare for the trip.
6. Reset the fare distance for a new trip.
7. Override the drive method to include fare distance.

"""

from cp1404prac.prac_09.car import Car

class Taxi(Car):
    """Taxi is a specialised version of a Car that includes fare costs."""
    price_per_km = 1.23  # Class variable

    def __init__(self, name, fuel):
        """Initialise a Taxi instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.current_fare_distance = 0

    def __str__(self):
        """Return a string representation of a Taxi, including current fare distance."""
        return f"{super().__str__()}, {self.current_fare_distance}km on current fare, ${self.price_per_km:.2f}/km"

    def get_fare(self):
        """Calculate and return the price for the taxi trip."""
        return self.price_per_km * self.current_fare_distance

    def start_fare(self):
        """Reset the fare distance to zero for a new trip."""
        self.current_fare_distance = 0

    def drive(self, distance):
        """Drive the Taxi for a given distance, updating fare distance."""
        distance_driven = super().drive(distance)
        self.current_fare_distance += distance_driven
        return distance_driven
