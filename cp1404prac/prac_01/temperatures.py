"""
CP1404/CP5632 - Practical
FENG YUAN
Pseudocode for temperature conversion

print MENU
get choice

choice = to_uppercase(choice)
while choice is not 'Q'
    if choice is 'C'
        get Celsius
        Fahrenheit = Celsius * 9.0 / 5 + 32
        print Fahrenheit result
    else if choice is 'F'
        get Fahrenheit
        Celsius = 5 / 9 * (Fahrenheit - 32)
        print Celsius result
    else
        print invalid option
    print MENU
    get choice

    choice = to_uppercase(choice)
print thank you

"""

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
print(MENU)
choice = input(">>> ").upper()
while choice != "Q":
    if choice == "C":
        celsius = float(input("Celsius: "))
        fahrenheit = celsius * 9.0 / 5 + 32
        print(f"Result: {fahrenheit:.2f} F")
    elif choice == "F":
        fahrenheit = float(input("Fahrenheit: "))
        celsius = 5 / 9 * (fahrenheit - 32)
        print(f"Result: {celsius:.2f} C")
    else:
        print("Invalid option")
    print(MENU)
    choice = input(">>> ").upper()
print("Thank you.")
