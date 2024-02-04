import math


def display():
    """Function that displays 'investment' or 'bond' options."""
    print(
        "investment - to calculate the amount of interest you'll earn on your investment"
    )
    print("bond       - to calculate the amount you'll have to pay on a home loan")
    print("\nEnter either 'investment' or 'bond' from the menu to proceed: ")


def choice():
    """A function that requests and input from the user and handles error if the
    input is either not 'investment' or 'bond'"""
    while True:
        user_choice = input().lower()

        if user_choice == "investment" or user_choice == "bond":
            break
        else:
            print("Invalid choice. Please enter 'investment' or 'bond'")

    return user_choice


def calculate_investment():
    """A function that calculates the investment using interest formula"""

    # Get the input from the user
    deposit = float(input("How much money you want do deposit: "))
    interest_rate = float(input("Enter the interest rate as a percentage (%): ")) / 100
    years = int(input("Enter the number of years you plan of investing: "))
    interest_type = input("Choose the option 'simple' or 'compund' interest: ").lower()

    if interest_type == "simple":
        amount = deposit * (1 + interest_rate * years)
    elif interest_type == "compound":
        amount = deposit * math.pow((1 + interest_rate), years)
    else:
        # Handle invalid interest type
        print("Invalid interest type. Please enter 'simple' or 'compund'")
        return

    print(f"Your investment will be worth ${amount:.2f} after {years} years. ")


def calculate_bond():
    """A function that calcultes the bond using the bond repayment formula"""
    # Get the input from the user
    current_cost = float(input("Enter the current cost of the house: "))
    interest_rate = float(input("Enter the interest rate: ")) / 100
    months = int(input("Enter the number of months for bond repayment: "))

    # Calculate the monthly interest rate and bond repayment
    monthly_interest_rate = interest_rate / 12
    repayment = (monthly_interest_rate * current_cost) / (
        1 - math.pow((1 + monthly_interest_rate), -months)
    )

    # Display the result
    print(f"You will have to repay ${repayment:.2f} each month for {months} months")


def main():
    display()
    user_choice = choice()

    # Execute the appropriate calculations based on user choice
    if user_choice == "investment":
        calculate_investment()
    elif user_choice == "bond":
        calculate_bond()


if __name__ == "__main__":
    # Run the function when the script is being executed
    main()
