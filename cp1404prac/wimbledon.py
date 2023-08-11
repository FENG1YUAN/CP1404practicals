"""
CP1404/CP5632 - Practical
FENG YUAN

Wimbledon Champions Analysis
Estimate: 40 minutes
Actual: 29 minutes
Pseudo-code:

The program begins by defining a set of functions to read, process, and display Wimbledon champions data from a CSV
 file.

The read_data function:
Opens the provided CSV file.
For each line in the file, it strips away any trailing whitespace, splits the line by comma, and appends the resulting
 list to the data list.
The function returns the populated data list.

The process_data function:
Initializes a dictionary to keep track of the number of times each champion has won and a set to store the unique
 countries of the champions.
For each row in the data, the function checks if the champion is already in the dictionary.
If the champion is present, their count is incremented.
If not, they are added to the dictionary with a count of 1.
The country of the champion is also added to the set.
The function then returns the champions dictionary and the countries set.

The display_data function:
Prints out all the champions along with the number of times they have won in descending order.
It also prints out the number of unique countries and displays them in alphabetical order.

The main function orchestrates the operations:
It calls read_data to get the data from the CSV file.
It then processes the data using the process_data function.
Finally, it displays the data using the display_data function.

Execution of the program begins in the main function if the script is run as the main module.
"""


def read_data(filename):
    """Read the data from the CSV file and return a list of lists."""
    data = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        for line in in_file:
            row = line.strip().split(",")
            data.append(row)
    return data


def process_data(data):
    """Process the data and return the champions with their win counts and a set of countries of the champions."""
    champions = {}
    countries = set()

    for row in data:
        champion = row[2]
        country = row[1]

        if champion in champions:
            champions[champion] += 1
        else:
            champions[champion] = 1

        countries.add(country)

    return champions, countries


def display_data(champions, countries):
    """Display the processed data."""
    print("Wimbledon Champions: ")
    for champion, wins in sorted(champions.items(), key=lambda x: x[1], reverse=True):
        print(f"{champion} {wins}")

    print("\nThese {} countries have won Wimbledon: ".format(len(countries)))
    print(", ".join(sorted(countries)))


def main():
    """Main function to tie all operations together."""
    data = read_data("wimbledon.csv")
    champions, countries = process_data(data)
    display_data(champions, countries)


if __name__ == "__main__":
    main()
