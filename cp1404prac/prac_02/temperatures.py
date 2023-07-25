"""
CP1404/CP5632 - Practical
FENG YUAN
Pseudocode for temperature conversion

The code uses two functions to convert Celsius to Fahrenheit and Fahrenheit to Celsius.
The choice of conversion is made through a menu system.
The program continues until the user quits.
"""

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""


def main():
    """
    Main function that drives the program.
    It shows a menu to the user and performs the appropriate conversion based on user's choice.
    """
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            fahrenheit = celsius_to_fahrenheit(celsius)
            print(f"Result: {fahrenheit:.2f} F")
        elif choice == "F":
            fahrenheit = float(input("Fahrenheit: "))
            celsius = fahrenheit_to_celsius(fahrenheit)
            print(f"Result: {celsius:.2f} C")
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def celsius_to_fahrenheit(celsius):
    """
    Function to convert Celsius to Fahrenheit.
    """
    return celsius * 9.0 / 5 + 32


def fahrenheit_to_celsius(fahrenheit):
    """
    Function to convert Fahrenheit to Celsius.
    """
    return 5 / 9 * (fahrenheit - 32)


main()
