"""
CP1404/CP5632 - Practical
FENG YUAN
Pseudocode:

function main()
    print welcome message
    prompt for password from user
    create star representation for the password
    print password in star format

function get_password()
    get password input from user
    return password length

Initialize function print_stars(password_length)
    create star representation for the password
    print password in star format

call function main()

"""


def main():
    """
    Main function that drives the program.
    It calls get_password function to get password length from user and
    print_stars function to print the password in star format.
    """
    print("Welcome to the password star representation program.")
    password_length = get_password()
    print_stars(password_length)


def get_password():
    """
    This function prompts the user for password input and
    returns the length of the password.
    """
    password = input("Enter your password: ")
    return len(password)


def print_stars(password_length):
    """
    This function takes password length as input,
    creates a star representation for the password,
    and prints the password in star format.
    """
    password_stars = '*' * password_length
    print("Your password in stars is: ", password_stars)


main()
