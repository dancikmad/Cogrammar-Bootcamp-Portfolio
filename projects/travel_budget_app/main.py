import random
from utils import get_destination, get_days, create_invoice, get_date
from datetime import datetime


def hotel_cost(num: int) -> int:
    """
    This function initializes a variable to store the standard price for a hotel night.
    It employs a logical sequence where the price changes based on the number
    of nights the hotel is booked.
    The function takes the number of nights as a parameter,
    applies the specified logic, and returns an integer representing
    the total cost at the hotel (calculated as the number of nights
    multiplied by the adjusted price for the standard night).
    """
    # Standard price
    hotel_cost_per_night = 100

    # If the booking duration falls within the range of 7 to 14 days,
    # the standard price decreases based on a generated random number
    if 7 <= num <= 14:
        hotel_cost_per_night -= random.randint(5, 15)

    # If the booking duration falls within the range of 15 to 21 days,
    # the standard price increases based on a generated random number
    elif 14 < num <= 21:
        hotel_cost_per_night += random.randint(15, 20)

    # For any other days the standard price decreases based on a generated number
    else:
        hotel_cost_per_night -= random.randint(20, 25)

    total_cost = hotel_cost_per_night * num

    return total_cost


def plane_cost(destination: str) -> int:
    """
    This function identifies the current month and stores it in a variable.
    The pricing logic takes into consideration factors such as the current season,
    destination, and the level of peak season activity. Prices are then adjusted,
    either increasing or decreasing, based on these parameters.
    """
    # Set prices depending on Peak Season:
    peak = 1.2  # Peak: 20% increase
    non_peak = 0.15  # Non-Peak: 20% discount

    # Set a sample ticket price
    ticket_price = 100

    # Get the current date and time
    current_datetime = datetime.now()

    # Format the date to get the month as a string
    current_month_str = current_datetime.strftime("%B")

    if current_month_str in ["December", "January", "February", "March"]:
        if destination in ["London", "New York", "Paris"]:
            determine_peak = random.choice(["Peak", "Non-Peak"])
            if determine_peak == "Peak":
                ticket_price = round((peak * ticket_price), 2)
            else:
                ticket_price = round((non_peak * ticket_price), 2)

    elif current_month_str in ["June", "July", "August"]:
        if destination in ["Mallorca", "Tenerife", "Madrid"]:
            ticket_price *= 2
        else:
            ticket_price /= 2

    return ticket_price


def car_rental(num: int) -> int:
    """
    This function initializes a variable to store the standard price for car day rent.
    It employs a logical sequence where the price changes based on the number of days to rent a car.
    The function takes the number of days as a parameter, applies the specified logic,
    and returns an integer representing the total cost for renting the car for num - days
    (calculated as the num - days multiplied by the adjusted price for the standard day rent).
    """
    car_rental_per_day = 50

    if 7 < num <= 14:
        car_rental_per_day -= random.randint(5, 15)
    elif 14 < num <= 21:
        car_rental_per_day -= random.randint(15, 20)
    else:
        car_rental_per_day -= random.randint(20, 25)

    total_cost = car_rental_per_day * num

    return total_cost


def holiday_cost(fn1, fn2, fn3):
    def inner_funct(num_nights, rental_days, city_flight):
        total = fn1(num_nights) + fn2(rental_days) + fn3(city_flight)
        return total

    return inner_funct


def main():
    cities = ["New York", "London", "Madrid", "Paris", "Tenerife", "Mallorca"]

    print("Welcome to Booking - ASAP! \n")
    date = get_date()
    city_flight = get_destination(cities)
    num_nights, rental_days = get_days()
    total_cost = holiday_cost(hotel_cost, car_rental, plane_cost)
    total_holiday_cost = total_cost(num_nights, rental_days, city_flight)

    data = [
        date,
        city_flight,
        plane_cost(city_flight),
        num_nights,
        hotel_cost(num_nights),
        rental_days,
        car_rental(rental_days),
        total_holiday_cost,
    ]

    create_invoice(data)


if __name__ == "__main__":
    main()
