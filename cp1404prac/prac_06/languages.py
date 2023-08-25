"""
Author: FENG YUAN
Time: 20 minutes

Pseudocode:
1. Import the ProgrammingLanguage class.
2. Define the main function.
    a. Create three instances of the ProgrammingLanguage class, namely python, ruby, and visual_basic.
    b. Display the python instance to verify the string representation (__str__ method).
    c. Create a list 'languages' to store the three programming language instances.
    d. Print out the names of languages that are dynamically typed.
        i. Iterate over the 'languages' list.
        ii. For each language, if it's dynamically typed, display its name.
3. Call the main function to run the program.
"""

from programming_language import ProgrammingLanguage


def main():
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    print(python)

    languages = [python, ruby, visual_basic]

    print("\nThe dynamically typed languages are:")
    for language in languages:
        if language.is_dynamic():
            print(language.name)


main()
