"""
CP1404/CP5632 - Practical
FENG YUAN


Define function write_name_to_file:
    Prompt the user to enter their name
    Open the file "name.txt" in write mode
    Write the user's name to the file

Define function read_name_from_file:
    Open the file "name.txt" in read mode
    Read the name from the file
    Print "Your name is {name}"

Define function read_and_add_numbers:
    Open the file "numbers.txt" in read mode
    Read the first two numbers from the file
    Add these two numbers together
    Print the result

Define function sum_all_numbers:
    Open the file "numbers.txt" in read mode
    Read all numbers from the file
    Sum up all the numbers
    Print the total

Define function main:
    Call function write_name_to_file
    Call function read_name_from_file
    Call function read_and_add_numbers
    Call function sum_all_numbers

Check if the script is running directly (i.e., not being imported)
    If true, call function main

End Program

"""


def write_name_to_file():
    """
    Function that asks for user's name, writes it to a file "name.txt".
    """
    name = input("Enter your name: ")
    with open("name.txt", 'w') as name_file:
        name_file.write(name)


def read_name_from_file():
    """
    Function that reads a name from "name.txt", then prints "Your name is {name}".
    """
    with open("name.txt", 'r') as name_file:
        name = name_file.read().strip()
        print(f"Your name is {name}")


def read_and_add_numbers():
    """
    Function that opens "numbers.txt", reads only the first two numbers,
    adds them together, and prints the result.
    """
    with open("numbers.txt", 'r') as numbers_file:
        num1 = int(numbers_file.readline())
        num2 = int(numbers_file.readline())
        print(num1 + num2)


def sum_all_numbers():
    """
    Function that opens "numbers.txt" and prints the total for all numbers in the file.
    """
    with open("numbers.txt", 'r') as numbers_file:
        total = sum(int(line) for line in numbers_file)
        print(total)


def main():
    """
    Main function that drives the program.
    Executes all the functions defined above.
    """
    write_name_to_file()
    read_name_from_file()
    read_and_add_numbers()
    sum_all_numbers()


if __name__ == "__main__":
    main()
