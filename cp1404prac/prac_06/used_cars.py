"""
Author: FENG YUAN
Time: 15 minutes

Pseudocode:

1. Import the Car class.
2. Define the main function to showcase the usage of the Car class.

   Within the main function:
   a . Initialize an object named "my_car" with name "MyCar" and fuel 180.
   b . Drive the "my_car" object for a distance of 30.
   c . Display the remaining fuel in "my_car".
   d . Print the string representation of "my_car".

   e . Create another object named "limo" with name "Limo" and fuel 100.
   f . Add 20 units of fuel to "limo".
   g . Display the fuel amount in "limo".
   h . Drive the "limo" object for a distance of 115.
   i . Print the string representation of "limo".

3. Execute the main function to run the demonstration.
"""

from car import Car


def main():
    """Demo test code to show how to use car class."""

    my_car = Car("MyCar", 180)
    my_car.drive(30)
    print(f"{my_car.name} has fuel: {my_car.fuel}")
    print(my_car)

    limo = Car("Limo", 100)
    limo.add_fuel(20)
    print(f"{limo.name} has fuel: {limo.fuel}")
    limo.drive(115)
    print(limo)


main()
