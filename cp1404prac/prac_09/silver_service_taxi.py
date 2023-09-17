"""
Author: Feng Yuan
Time to Complete: 20 minutes
Pseudo-code Repository: https://github.com/FENG1YUAN/CP1404practicals/tree/prac_09_feedback/cp1404prac

Pseudo Code:
1. Import the Taxi class from the specified module.
2. Define a SilverServiceTaxi class that inherits from Taxi.
3. Add an 'initial_charge' class variable.
4. Override the '__init__' method to set 'fanciness' and modify 'price_per_km'.
5. Override 'get_fare' method to include the 'initial_charge'.
6. Override '__str__' method to display the 'initial_charge'.

"""

from cp1404prac.prac_09.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """SilverServiceTaxi is a specialized Taxi that has additional attributes and methods."""
    initial_charge = 4.50  # Class variable for initial charge

    def __init__(self, name, fuel, fanciness):
        """Initialize a SilverServiceTaxi instance."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness

    def get_fare(self):
        """Return the total fare for the taxi trip, including initial_charge."""
        return super().get_fare() + self.initial_charge

    def __str__(self):
        """Return a string representation of a SilverServiceTaxi."""
        return f"{super().__str__()} plus initial_charge of ${self.initial_charge:.2f}"
