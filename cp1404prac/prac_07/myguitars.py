"""
CP1404/CP5632 Practical
Author: FENG YUAN
Time: 30 minutes
"""


from guitar import Guitar


def main():
    guitars = load_guitars()

    for guitar in guitars:
        print(guitar)

    guitars.sort()

    print("\nGuitars sorted by year:")
    for guitar in guitars:
        print(guitar)

    add_new_guitars(guitars)
    save_guitars(guitars)


def load_guitars():
    guitars = []
    with open("guitars.csv", "r") as file:
        for line in file:
            parts = line.strip().split(",")
            guitars.append(Guitar(parts[0], int(parts[1]), float(parts[2])))
    return guitars


def add_new_guitars(guitars):
    while True:
        name = input("Enter the guitar's name: ")
        if not name:
            break

        year = int(input("Enter the year the guitar was made: "))
        cost = float(input("Enter the cost of the guitar: $"))
        new_guitar = Guitar(name, year, cost)
        guitars.append(new_guitar)
        print(f"{new_guitar} added.\n")


def save_guitars(guitars):
    with open("guitars.csv", "w") as file:
        for guitar in guitars:
            file.write(f"{guitar.name},{guitar.year},{guitar.cost}\n")
    print("Guitars saved to guitars.csv.")


if __name__ == "__main__":
    main()
