"""
CP1404/CP5632 - Practical
FENG YUAN
Pseudocode:

The code uses a main function to drive the program.
The user is asked for the number of months for which income data is to be entered.
The program then asks the user to input the income for each month and stores it in a list.

Once all the income data has been entered, the function print_report is called,
which takes the number of months and the list of incomes as arguments,
and prints a formatted income report.
"""


def main():
    """
    Main function that drives the program.
    It collects income data over a number of months and prints an income report.
    """
    incomes = []
    number_of_months = int(input("How many months? "))

    for month in range(1, number_of_months + 1):
        income = float(input(f"Enter income for month {month}: "))
        incomes.append(income)

    print_report(number_of_months, incomes)


def print_report(number_of_months, incomes):
    """
    Function to print income report given the number of months and the respective incomes.
    """
    print("\nIncome Report\n-------------")
    total = 0
    for month in range(1, number_of_months + 1):
        income = incomes[month - 1]
        total += income
        print(f"Month {month:2} - Income: ${income:10.2f} Total: ${total:10.2f}")


if __name__ == '__main__':
    main()
