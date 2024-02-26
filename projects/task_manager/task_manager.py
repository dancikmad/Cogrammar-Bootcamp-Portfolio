# Notes:
# 1. Use the following username and password to access the admin rights
# username: admin
# password: password

import settings
from utils import (
    reg_user,
    add_task,
    view_all,
    view_mine,
    generate_reports,
    display_statistics,
)


DATETIME_STRING_FORMAT = "%Y-%m-%d"


def main():
    # Initilaise Users
    username_password = settings.load_users("user.txt")

    # Initialise Tasks
    task_list = settings.load_tasks("tasks.txt", DATETIME_STRING_FORMAT)

    # Initialise Authorization into Task Manager
    curr_user = settings.sign_in(username_password)

    while True:
        print()
        user_choice = input(settings.display_menu(curr_user)).strip().lower()

        if user_choice == "r":
            reg_user(username_password, "user.txt")

        elif user_choice == "a":
            add_task(username_password, task_list, DATETIME_STRING_FORMAT, "tasks.txt")

        elif user_choice == "va":
            view_all(task_list, DATETIME_STRING_FORMAT)

        elif user_choice == "vm":
            view_mine(task_list, curr_user, DATETIME_STRING_FORMAT)

        elif user_choice == "ds" and curr_user == "admin":
            display_statistics(task_list, username_password)

        elif user_choice == "gr":
            generate_reports(task_list, username_password)

        elif user_choice == "e":
            print("Goodbye!!!")
            exit()

        else:
            print("You have made a wrong choice, Please Try again")


if __name__ == "__main__":
    main()
