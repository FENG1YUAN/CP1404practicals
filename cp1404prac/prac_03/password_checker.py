"""
CP1404/CP5632 - Practical
FENG YUAN

Start Program

Declare constants MIN_LENGTH, MAX_LENGTH, SPECIAL_CHARS_REQUIRED, SPECIAL_CHARACTERS

Define a function named main:
    Display a prompt for the user to enter a valid password with specific requirements
    Read the password input by the user
    While password is not valid as determined by the function is_valid_password
        Display an error message about the invalid password
        Read the password input by the user again
    Display a success message that shows the password is valid

Define a function named is_valid_password with an argument password:
    If the length of password is less than MIN_LENGTH or greater than MAX_LENGTH
        Return False

    Initialize counters for lowercase letters, uppercase letters, digits, and special characters
    For each character in password:
        If the character is a digit, increment the digit counter
        If the character is a lowercase letter, increment the lowercase letter counter
        If the character is an uppercase letter, increment the uppercase letter counter
        If the character is a special character, increment the special character counter

    If any of the counters for lowercase letters, uppercase letters, or digits is zero
        Return False

    If special characters are required and the special character counter is zero
        Return False

    Return True

Call the main function

End Program

"""

MIN_LENGTH = 2
MAX_LENGTH = 6
SPECIAL_CHARS_REQUIRED = False
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"


def main():
    """Program to get and check a user's password."""
    print("Please enter a valid password")
    print("Your password must be between", MIN_LENGTH, "and", MAX_LENGTH,
          "characters, and contain:")
    print("\t1 or more uppercase characters")
    print("\t1 or more lowercase characters")
    print("\t1 or more numbers")
    if SPECIAL_CHARS_REQUIRED:
        print("\tand 1 or more special characters: ", SPECIAL_CHARACTERS)
    password = input("> ")
    while not is_valid_password(password):
        print("Invalid password!")
        password = input("> ")
    print(f"Your {len(password)}-character password is valid: {password}")


def is_valid_password(password):
    """Determine if the provided password is valid."""
    if len(password) < MIN_LENGTH or len(password) > MAX_LENGTH:
        return False

    count_lower = 0
    count_upper = 0
    count_digit = 0
    count_special = 0
    for char in password:
        if char.isdigit():
            count_digit += 1
        elif char.islower():
            count_lower += 1
        elif char.isupper():
            count_upper += 1
        elif char in SPECIAL_CHARACTERS:
            count_special += 1

    if count_lower == 0 or count_upper == 0 or count_digit == 0:
        return False

    if SPECIAL_CHARS_REQUIRED and count_special == 0:
        return False

    return True


main()
