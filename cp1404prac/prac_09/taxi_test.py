"""
Author: Feng Yuan
Time to Complete: 15 minutes
Pseudo-code Repository: https://github.com/FENG1YUAN/CP1404practicals/tree/prac_09_feedback/cp1404prac

Pseudo Code:
1. Import the Taxi class from cp1404prac.prac_09.taxi.
2. Define a main function.
3. Create a Taxi instance named "Prius 1" with 100 units of fuel.
4. Drive the Taxi for 40 km.
5. Print the Taxi's details and the current fare.
6. Start a new fare.
7. Drive the Taxi for 100 km.
8. Print the Taxi's details and the current fare.
"""

from cp1404prac.prac_09.taxi import Taxi


def main():
    """Main function to run the Taxi test."""

    my_taxi = Taxi("Prius 1", 100)
    """Create a Taxi instance."""

    my_taxi.drive(40)
    """Drive the Taxi for 40 km."""

    print(my_taxi)
    """Print Taxi details."""

    print(f"Current fare: ${my_taxi.get_fare():.2f}")
    """Print current fare."""

    my_taxi.start_fare()
    """Start a new fare."""

    my_taxi.drive(100)
    """Drive the Taxi for 100 km."""

    print(my_taxi)
    """Print Taxi details."""

    print(f"Current fare: ${my_taxi.get_fare():.2f}")
    """Print current fare."""


if __name__ == "__main__":
    """Run the main function."""
    main()
