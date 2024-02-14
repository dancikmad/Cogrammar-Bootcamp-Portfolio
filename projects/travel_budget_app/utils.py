from datetime import datetime
from tabulate import tabulate
import time


def get_destination(destinations: list) -> int:
    """
    Requests the user to input a destination city (str). The function checks
    whether the user's input is present in the list argument and returns the input
    if it matches any of the cities in the list.

    Parameters:
    destinations (list) : list that stores cities

    Returns:
    res (str) : a string (City Name) capitalized
    """
    while True:
        res = input("What is your flight destination: ").strip().capitalize()

        if res in destinations:
            return res
        else:
            print(
                "Sorry, destination not available. You can choose one of our destinations: \n"
            )
            for destination in destinations:
                print(destination)


def get_days():
    """
    This function receives two integer inputs, assigning them to the variables
    num_nights (representing the number of nights at the hotel) and rental_days
    (representing the number of days for car rental). It includes error handling
    for non-integer inputs. The logic involves initially obtaining input for
    num_nights, and if successful, proceeding to request input for rental_days.
    The function returns two variables of type integer.
    """
    num_nights = rental_days = 0  # Initialize variables
    while True:
        try:
            num_nights = int(input("Number of nights staying at the hotel: "))

            if num_nights:
                while True:
                    try:
                        rental_days = int(
                            input("Number of days you are renting the car: ")
                        )
                        break
                    except ValueError:
                        print("Please enter a number!")
        except ValueError:
            print("Please enter a number!")
        else:
            break

    return num_nights, rental_days


def create_invoice(*args):
    """A function that prints a user friendly display of the cost for booking a trip"""
    table = [*args]

    headers = [
        "Date",
        "Destination",
        "Flight Cost",
        "Accommodation Nights",
        "Hotel Cost",
        "Car Rental Days",
        "Car Rental Cost",
        "Total Cost",
    ]

    msg = "Thank you for providing your information. "
    msg += "We have received it and are currently generating an invoice based on the provided data."
    msg += "Your prompt cooperation is greatly appreciated!"

    print(msg)
    time.sleep(2)
    print(tabulate(table, headers, tablefmt="simple_grid"))


def get_date():
    """A function that returns the current date-time of making a booking"""

    current_datetime = datetime.now()
    # Adjust the format as needed
    formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M")

    return formatted_datetime
