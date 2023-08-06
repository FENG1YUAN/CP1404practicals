"""
CP1404/CP5632 Practical
FENG YUAN

Main function:
1. Initialize an empty list called 'numbers'.
2. For a range of 5 times:
   2.1. Prompt the user to enter a number and convert it to a float.
   2.2. Append this number to the 'numbers' list.
3. Print the first number in the 'numbers' list.
4. Print the last number in the 'numbers' list.
5. Print the smallest number in the 'numbers' list.
6. Print the largest number in the 'numbers' list.
7. Print the average of the numbers in the 'numbers' list.
8. Define a list of accepted usernames.
9. Prompt the user to enter their username.
10. If the entered username is in the list of accepted usernames:
    10.1. Print "Access granted".
11. If the entered username is not in the list of accepted usernames:
    11.1. Print "Access denied".
"""


def main():
    """
    The main function of the program, which includes two parts:
    1. Asks the user to input 5 numbers and performs operations on these numbers.
    2. Performs a security check by asking for a username and checking if it exists in a pre-defined list.
    """
    numbers = []
    for i in range(5):
        number = float(input("Number: "))
        numbers.append(number)

    print("The first number is", numbers[0])
    print("The last number is", numbers[-1])
    print("The smallest number is", min(numbers))
    print("The largest number is", max(numbers))
    print("The average of the numbers is", sum(numbers) / len(numbers))

    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45',
                 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState',
                 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

    entered_username = input("Please enter your username: ")

    if entered_username in usernames:
        print("Access granted")
    else:
        print("Access denied")


if __name__ == '__main__':
    main()
