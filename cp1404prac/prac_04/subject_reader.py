"""
CP1404/CP5632 - Practical
FENG YUAN
Pseudocode:

The code uses a main function to drive the program,
then retrieves data from a file and displays the subject details.

The function get_data reads data from a file formatted like: subject,lecturer,number of students,
and returns a list of lists with the subject, lecturer, and number of students.

The function display_subject_details takes in the data retrieved and
displays the subject details in the format: "{subject} is taught by {lecturer} and has {number} students".
"""


FILENAME = "subject_data.txt"


def main():
    """
    Main function that drives the program.
    It retrieves data from the file and displays the subject details.
    """
    data = get_data()
    display_subject_details(data)


def get_data():
    """
    Reads data from file formatted like: subject,lecturer,number of students,
    and returns a list of lists with the subject, lecturer, and number of students.
    """
    data = []
    with open(FILENAME) as input_file:
        for line in input_file:
            line = line.strip()
            parts = line.split(',')
            parts[2] = int(parts[2])
            data.append(parts)
    return data


def display_subject_details(data):
    """
    Displays subject details.
    """
    for subject_data in data:
        print(f"{subject_data[0]} is taught by {subject_data[1]} and has {subject_data[2]} students")


if __name__ == '__main__':
    main()
