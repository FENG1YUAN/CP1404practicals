"""
Author: Feng Yuan
Time to Complete: 15 minutes
Pseudo-code Repository: https://github.com/FENG1YUAN/CP1404practicals/tree/prac_09_feedback/cp1404prac

Pseudo Code:
1. Import the SilverServiceTaxi class from the specified module.
2. Define a main function.
3. Inside the main function:
    - Create a SilverServiceTaxi object with name "Hummer", fuel 200, and fanciness 2.
    - Start a new fare using the start_fare method.
    - Drive the SilverServiceTaxi for 18 km.
    - Print the object's state.
    - Print the total fare for the trip.
4. Execute the main function if the script is run as the main module.

"""

from cp1404prac.prac_09.silver_service_taxi import SilverServiceTaxi


def main():
    """Main function to run the SilverServiceTaxi test."""
    fancy_taxi = SilverServiceTaxi("Hummer", 200, 2)

    fancy_taxi.start_fare()

    fancy_taxi.drive(18)

    print(fancy_taxi)
    print(f"Total fare: ${fancy_taxi.get_fare():.2f}")


if __name__ == "__main__":
    main()

