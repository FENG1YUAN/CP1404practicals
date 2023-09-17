"""
Author: Feng Yuan
Time to Complete: 25 minutes
Pseudo-code Repository: https://github.com/FENG1YUAN/CP1404practicals/tree/prac_09_feedback/cp1404prac

Pseudo Code:
1. Import Taxi and SilverServiceTaxi classes.
2. Create a list of available taxis.
3. Initialize total bill to 0.
4. Display a menu to the user for choosing an option.
5. If 'q', quit and show the total cost.
6. If 'c', display the available taxis and let the user choose one.
7. If 'd', check if a taxi has been selected, then drive it.
8. Continue this loop until the user quits.
"""

from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi


def main():
    """Main function to run the taxi simulator."""
    taxis = [
        Taxi("Prius", 100),
        SilverServiceTaxi("Limo", 100, 2),
        SilverServiceTaxi("Hummer", 200, 4)
    ]
    current_taxi = None
    total_bill = 0.0

    print("Let's drive!")

    while True:
        print("q)Quit, c)Choose taxi, d)Drive")
        choice = input(">>> ").lower()

        if choice == 'q':
            print(f"Total trip cost: ${total_bill:.2f}")
            print("Taxis are now:")
            for i, taxi in enumerate(taxis):
                print(f"{i} - {taxi}")
            break

        elif choice == 'c':
            print("Taxis available:")
            for i, taxi in enumerate(taxis):
                print(f"{i} - {taxi}")
            try:
                taxi_choice = int(input("Choose taxi: "))
                current_taxi = taxis[taxi_choice]
            except (ValueError, IndexError):
                print("Invalid taxi choice")

        elif choice == 'd':
            if current_taxi is None:
                print("You need to choose a taxi before you can drive")
                continue
            current_taxi.start_fare()
            distance_to_drive = float(input("Drive how far? "))
            distance_driven = current_taxi.drive(distance_to_drive)
            trip_cost = current_taxi.get_fare()
            print(f"Your {current_taxi.name} trip cost you ${trip_cost:.2f}")
            total_bill += trip_cost

        else:
            print("Invalid option")

        print(f"Bill to date: ${total_bill:.2f}")


if __name__ == '__main__':
    """Run the main function."""
    main()
