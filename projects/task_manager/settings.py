from colorama import Fore
from datetime import datetime
import os


def display_menu(for_user):
    if for_user == "admin":
        menu = "Please select one of the following options: \n"
        menu += "r - Register user\n"
        menu += "a - Add task\n"
        menu += "va - View all tasks\n"
        menu += "vm - View my tasks\n"
        menu += "gr - Generate reports\n"
        menu += "ds - Display statistics\n"
        menu += "e - exit\n"
        menu += ": "

        return Fore.BLUE + menu

    else:
        menu = "Please select one of the following options: \n"
        menu += "r - Register user\n"
        menu += "a - Add task\n"
        menu += "va - View all tasks\n"
        menu += "vm - View my tasks\n"
        menu += "e - exit\n"
        menu += ": "

        return menu


def sign_in(user_database):
    logged_in = False
    while not logged_in:
        print("LOGIN")
        curr_user = input("Username: ")
        curr_pass = input("Password: ")
        if curr_user not in user_database.keys():
            print("User does not exist")
            continue
        elif user_database[curr_user] != curr_pass:
            print("Wrong password")
            continue
        else:
            print("Login Succesfull!")
            logged_in = True

    return curr_user


def load_tasks(filename, date_format):
    # Create tasks.txt if it doesn't exist
    if not os.path.exists(filename):
        with open(filename, "w") as default_file:
            pass

    with open(filename, "r") as task_file:
        task_data = task_file.read().split("\n")
        task_data = [t for t in task_data if t != ""]

    tasks = []
    for t_str in task_data:
        curr_t = {}

        # Split by semicolon and manually add each component
        task_components = t_str.split(";")
        curr_t["username"] = task_components[0]
        curr_t["title"] = task_components[1]
        curr_t["description"] = task_components[2]
        curr_t["due_date"] = datetime.strptime(task_components[3], date_format)
        curr_t["assigned_date"] = datetime.strptime(task_components[4], date_format)
        curr_t["completed"] = True if task_components[5] == "Yes" else False

        tasks.append(curr_t)

    return tasks


def load_users(file_name):
    """
    This function reads usernames and password from the user.txt file
    to allow a user to login.
    """
    # If no 'file_name', write one with a default account
    if not os.path.exists(file_name):
        with open(file_name, "w") as default_file:
            default_file.write("admin;password")

    # Read in user_data
    with open(file_name, "r") as user_file:
        user_data = user_file.read().split("\n")

    # Convert to a dictionary
    username_password = {}
    for user in user_data:
        username, password = user.split(";")
        username_password[username] = password

    return username_password
