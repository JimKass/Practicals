"""

"""

from prac_08.taxi import Taxi
from prac_08.silver_service_taxi import SilverServiceTaxi

TAXIS = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 100, 4)]

MENU = """Q - Quit
C - Choose Taxi
D - Drive"""


def main():
    print(MENU)
    action = input(">>> ").lower()

    while action != "q":
        if action == "c":
            my_taxi = choose_taxi()
        elif action == "d":
            drive_taxi(my_taxi)
        else:
            print("Invalid Input. Please enter a valid input")
        try:
            print("Bill to date: ${}".format(my_taxi.get_fare()))
        except UnboundLocalError:
            pass
        print(MENU)
        action = input(">>> ").lower()
    print("Total trip cost: ${}".format(calculate_total_cost(TAXIS)))
    print("Taxis are now:")
    display_taxis(TAXIS)


def drive_taxi(my_taxi):
    try:
        distance = int(input("Drive how far? "))
        my_taxi.drive(distance)
    except UnboundLocalError:
        print("Please select a taxi.")
    except ValueError:
        print("Invalid Input. Input must be a number")


def choose_taxi():
    is_valid = False
    while not is_valid:
        display_taxis(TAXIS)
        try:
            my_taxi_number = int(input("Choose taxi: "))
            my_taxi = TAXIS[my_taxi_number]
            is_valid = True
        except (ValueError, IndexError):
            print("Invalid Taxi Number")
    return my_taxi


def display_taxis(taxis):
    for i, taxi in enumerate(taxis):
        print("{} - {}".format(i, taxi))


def calculate_total_cost(taxis):
    cost = 0
    for taxi in taxis:
        cost += taxi.get_fare()
    return cost

main()
