"""
CP1404/CP5632 - Practical
FENG YUAN

State Codes and Names
Estimate: 30 minutes
Actual: 24 minutes
Pseudo-code:

The code maintains a dictionary of Australian state abbreviations as keys and their full names as values.

Initially, it prints the entire dictionary to show all state codes with their respective full names.

Then, using a for loop, the code prints out each state abbreviation along with its full name neatly.

After displaying all the states, the code prompts the user to enter an abbreviation. The program converts
the input to uppercase to ensure case insensitivity and tries to fetch the full name of the state using the
given abbreviation.

If the abbreviation isn't found in the dictionary, the program raises a KeyError and informs the user about
the invalid input.

The code continues to prompt the user for state abbreviations until an empty string is provided.
"""

CODE_TO_NAME = {
    "QLD": "Queensland",
    "NSW": "New South Wales",
    "NT": "Northern Territory",
    "WA": "Western Australia",
    "ACT": "Australian Capital Territory",
    "VIC": "Victoria",
    "TAS": "Tasmania"
}
print(CODE_TO_NAME)

# Printing all the states and their names neatly
for code, name in CODE_TO_NAME.items():
    print(f"{code} is {name}")

state_code = input("Enter short state: ").upper()
while state_code != "":
    try:
        print(state_code, "is", CODE_TO_NAME[state_code])
    except KeyError:
        print("Invalid short state")
    state_code = input("Enter short state: ").upper()
