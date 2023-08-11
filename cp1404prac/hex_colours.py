"""
CP1404/CP5632 - Practical
FENG YUAN

Colour Code Lookup
Estimate: 20 minutes
Actual: 20 minutes
Pseudo-code:

The program begins with a predefined dictionary COLOUR_CODES,
mapping colour names to their hexadecimal codes.

The main function displays "Colour Code Lookup" and enters an infinite loop, which:
    1. Prompts the user for a colour name.
    2. If the user input is empty, the loop exits.
    3. For a given colour name, it searches the dictionary for the corresponding hexadecimal code.
    4. If found, it prints the colour and its hexadecimal code.
    5. If not found, it notifies the user that the entered colour name isn't in the dictionary.

The get_colour_code(colour_name) function takes a colour name and returns the associated hexadecimal code,
or None if not found in the dictionary.
"""

COLOUR_CODES = {
    "Blue (Pantone)": "#0018a8",
    "Blue Bell": "#a2a2d0",
    "Blue Green": "#0d98ba",
    "Blue1": "#0000ff",
    "BlueViolet": "#8a2be2",
    "Bole": "#79443b",
    "Bone": "#e3dac9",
    "Boysenberry": "#873260",
    "Brandeis Blue": "#0070ff",
    "Brick Red": "#cb4154"
}


def get_colour_code(colour_name):
    """Retrieve hexadecimal colour code based on the provided colour name."""
    return COLOUR_CODES.get(colour_name, None)


def main():
    """Interactively look up colour codes."""
    print("Colour Code Lookup")
    while True:
        colour_name = input("Enter a colour name (blank to quit): ").strip().title()
        if not colour_name:
            break
        code = get_colour_code(colour_name)
        if code:
            print(f"{colour_name} -> {code}")
        else:
            print(f"Sorry, {colour_name} not found!")


if __name__ == "__main__":
    main()
