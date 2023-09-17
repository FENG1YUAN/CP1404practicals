"""
Author: Feng Yuan
Time to Complete: 10 minutes
Pseudo-code Repository: https://github.com/FENG1YUAN/CP1404practicals/tree/prac_09_feedback/cp1404prac

Pseudo Code:
1. Import the UnreliableCar class from the corresponding module.
2. Define the main function.
3. Inside the main function:
    - Create an UnreliableCar object named 'my_unreliable_car' with 50% reliability and 100 units of fuel.
    - Attempt to drive the car 30 km using its drive method.
    - Get the actual distance driven (this may be less than the requested distance due to the car's unreliability).
    - Display the car's name and the distance it actually drove.

"""

from cp1404prac.prac_09.unreliable_car import UnreliableCar


def main():
    """Main function to test the UnreliableCar class."""
    my_unreliable_car = UnreliableCar("Unreliable1", 100, 50.0)

    distance = my_unreliable_car.drive(30)

    print(f"{my_unreliable_car.name} drove {distance}km.")


if __name__ == "__main__":
    main()
