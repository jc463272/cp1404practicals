"""
CP1404 - William Hunter
Taxi simulator using Taxi and SilverServiceTaxi classes.
Estimate:
Actual:
"""

from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"

def main():
    """Main menu to drive program"""
    current_taxi = None
    total_bill = 0
    taxis = [Taxi("Prius", 100),
             SilverServiceTaxi("Limo", 100, 2),
             SilverServiceTaxi("Hummer", 200, 4)]
    print("---Let's drive---")
    print(MENU)
    choice = input(">>>").lower()
    while choice != "q":
        if choice == "c":
            print("The following taxis are available:")
            display_taxis(taxis)
            taxi_choice = int(input("Please choose taxi: "))
            try:
                current_taxi = taxis[taxi_choice]
            except IndexError:
                print("Invalid choice")
        elif choice == "d":
            if current_taxi:
                current_taxi.start_fare()
                distance_driven = float(input("Please enter distance in kilometers: "))
                current_taxi.drive(distance_driven)
                trip_cost = current_taxi.get_fare()
                print(f"Your {current_taxi.name} trip cost you ${trip_cost:.2f}")
                total_bill += trip_cost
            else:
                print("You must choose a taxi first")
        else:
            print("Invalid option")
        print(f"Up-to-date bill: ${total_bill:.2f}")
        print(MENU)
        choice = input(">>>").lower()

    print(f"Total trip cost: {total_bill:.2f}")
    print("Taxis are now:")
    display_taxis(taxis)

def display_taxis(taxis):
    """Displays index list of taxis."""
    for i,taxi in enumerate(taxis):
        print(f"{i} - {taxi}")

main()
