from datetime import datetime, date
from tabulate import tabulate


def reg_user(user_database, file_name):
    """A function to register a user to the user.txt file"""

    while True:
        # - Request input of a new username
        new_username = input("New Username: ")
        if new_username in user_database:
            print("Sorry the username exists. Please enter new username.")
        else:
            break

    # - Request input of a new password
    new_password = input("New Password: ")

    # - Request input of password confirmation.
    confirm_password = input("Confirm Password: ")

    # - Check if the new password and confirmed password are the same.
    if new_password == confirm_password:
        # - If they are the same, add them to the user.txt file
        print("New user added")
        user_database[new_username] = new_password

        with open(file_name, "w") as out_file:
            user_data = []
            for k in user_database:
                user_data.append(f"{k};{user_database[k]}")
            out_file.write("\n".join(user_data))

    # - Otherwise your present a relevant message.
    else:
        print("Passwords do not match")


def add_task(user_database, task_database, date_format, file_name):
    """
    A function that allows user to add a new task to task.txt file
        Prompts the user for the following:
        - A username of the person whom the task is assigned to,
        - A title of a task,
        - A description of the task and the due date of the task.
    """
    while True:
        username_task = input("Name of person assigned to task: ")
        if username_task not in user_database.keys():
            print("User does not exist. Please enter a valid username.")
        else:
            break

    task_title = input("Title of Task: ")
    task_description = input("Description of Task: ")

    while True:
        try:
            task_due_date = input("Due date of task (YYYY-MM-DD): ")
            due_date_time = datetime.strptime(task_due_date, date_format)
            break

        except ValueError:
            print("Invalid datetime format. Please use the format specified.")

    # Then get the current date.
    curr_date = date.today()
    """ Add the data to the file task.txt and 
        Include 'No' to indicate if the task is complete."""
    new_task = {
        "username": username_task,
        "title": task_title,
        "description": task_description,
        "due_date": due_date_time,
        "assigned_date": curr_date,
        "completed": False,
    }

    task_database.append(new_task)
    with open(file_name, "w") as task_file:
        task_list_to_write = []
        for t in task_database:
            str_attrs = [
                t["username"],
                t["title"],
                t["description"],
                t["due_date"].strftime(date_format),
                t["assigned_date"].strftime(date_format),
                "Yes" if t["completed"] else "No",
            ]
            task_list_to_write.append(";".join(str_attrs))
        task_file.write("\n".join(task_list_to_write))
    print("Task succesfully added.")


def view_all(task_database, date_format):
    """
    A function that is called when users type 'va' to view all the tasks listed
    in tasks.txt.
    Reads the task from txt.file and prints to the console in the format of
    Output 2 presented in the task pdf (i.e. includes spacing and labelling)
    """

    for t in task_database:
        disp_str = f"Task: \t\t {t['title']}\n"
        disp_str += f"Assigned to: \t {t['username']}\n"
        disp_str += f"Date Assigned: \t {t['assigned_date'].strftime(date_format)}\n"
        disp_str += f"Due Date: \t {t['due_date'].strftime(date_format)}\n"
        disp_str += f"Task Description: \n {t['description']}\n"
        print(disp_str)


def view_mine(task_database, current_user, date_format):
    """
    A function that displays all the tasks that have been assigned to user.
    Reads the task from task.txt and prints to the console in the format of
    Output 2 presented in the task pdf (i.e. includes spacing and labelling)
    """

    for i, t in enumerate(task_database):
        if t["username"] == current_user:
            headers = [f"Task Number: {i}", "INFORMATION"]
            table = [
                ["Task ", t["title"]],
                [
                    "User Assigned",
                    t["username"],
                ],
                ["Date Assigned", t["assigned_date"].strftime(date_format)],
                ["Due Date", t["due_date"].strftime(date_format)],
                ["Task Description", f"--- Enter '{i}' to view description ---"],
            ]
            print(tabulate(table, headers, tablefmt="rounded_grid"))

    while True:
        view_menu = "If you require additional details about the task, "
        view_menu += "please input a number corresponding to the Task Number.\n"
        view_menu += "If you want to return to menu please select '-1'\n: "

        task_choice = input(view_menu).strip()

        if task_choice == "-1":
            break
        else:
            try:
                task_choice = int(task_choice)
                if 0 <= task_choice < len(task_database):
                    selected_task = task_database[task_choice]
                    task_info = f"Title: \t{task_database[task_choice]['title']}\n\n"
                    task_info += f"Task Description: \n*** {task_database[task_choice]['description']}"
                    print(task_info)

                    # Provide options to mark task as complete or edit task
                    edit_menu = "\nSelect an option:\n"
                    edit_menu += "1. Mark task as complete\n"
                    edit_menu += "2. Edit task\n"
                    edit_menu += "3. Return to menu\n: "

                    edit_choice = input(edit_menu).strip()

                    if edit_choice == "1":
                        if not selected_task["completed"]:
                            selected_task["completed"] = True
                            print("Task marked as complete.")
                        else:
                            print("Task is already marked as complete.")

                    elif edit_choice == "2":
                        if not selected_task["completed"]:
                            new_username = input(
                                "Enter new username for the task: "
                            ).strip()
                            new_due_date = input(
                                "Enter new date for the task ()"
                            ).strip()

                            # Update task details if they are provided
                            if new_username:
                                selected_task["username"] = new_username
                            if new_due_date:
                                try:
                                    selected_task["due_date"] = datetime.strptime(
                                        new_due_date, date_format
                                    )
                                except ValueError:
                                    print(
                                        "Invalid datetime format. Task due date not updated."
                                    )
                            print("Task edited succesfully")
                        else:
                            print(
                                "Task cannot be edited as it already marked as complete."
                            )
                    elif edit_choice == "3":
                        print("Returning to the menu.")
                        break
                    else:
                        print("Invalid option. Please select a valid option.")
                else:
                    print("Invalid task number. Please enter a valid Task Number!")
            except ValueError:
                print("Invalid input. Please enter a valid Task Number!")


def generate_reports(task_database, user_database):
    """
    A function that generates reports for task_overview and user_overview and write
    the information to a file.
    """
    menu_reports = "\nPlease choose one of the options to generate reports for - \n"
    menu_reports += "Enter '1' for tasks\n"
    menu_reports += "Enter '2' for users\n"
    menu_reports += "Enter 'q' if you wish to quit\n: "

    while True:
        user_choice = input(menu_reports).strip()
        if user_choice == "q":
            break

        elif user_choice == "1":
            generate_task_report(
                task_database,
            )

        elif user_choice == "2":
            generate_user_report(user_database, task_database)

        else:
            print("Error! Wrong option. Redirecting back to the menu ...\n")


def generate_task_report(task_database):
    task_report = {
        "total_tasks": 0,
        "total_completed": 0,
        "total_uncompleted": 0,
        "total_uncompleted_due_date": 0,
        "percentage_of_incomplete": 0,
        "percentage_of_overdue": 0,
    }

    for task in task_database:
        task_report["total_tasks"] += 1
        if task["completed"]:
            task_report["total_completed"] += 1
        else:
            task_report["total_uncompleted"] += 1

        if task["due_date"].date() < date.today() and not task["completed"]:
            task_report["total_uncompleted_due_date"] += 1

    task_report["percentage_of_incomplete"] = (
        task_report["total_uncompleted"] / task_report["total_tasks"]
    ) * 100
    task_report["percentage_of_overdue"] = (
        task_report["total_uncompleted_due_date"] / task_report["total_tasks"]
    ) * 100

    headers = ["Tasks", "Numbers"]
    table = [
        ["Total", task_report["total_tasks"]],
        ["Completed", task_report["total_completed"]],
        ["Uncompleted", task_report["total_uncompleted"]],
        ["Overdue", task_report["total_uncompleted_due_date"]],
        ["Incomplete (%)", task_report["percentage_of_incomplete"]],
        ["Overdue (%)", task_report["percentage_of_overdue"]],
    ]

    with open("task_overview.txt", "w") as task_overview:
        print("Generating Tasks Report ...\n")
        print(
            'Your generated report file is ready. It was saved as "task_overview.txt"\n'
        )
        task_overview.write(tabulate(table, headers, tablefmt="rounded_grid"))


def generate_user_report(user_database, task_database):
    headers = ["", "Numbers"]
    table = [
        ["Total Number of Users", len(user_database)],
        ["Total Number of Tasks", len(task_database)],
    ]

    headers_2 = ["User Number", "User Login"]
    table_2 = []
    for i, key in enumerate(user_database.keys()):
        table_2.append([i, key])

    print("\nGenerating Users Report ...\n")
    print("You generated report file is ready. It was saved as 'users_overview.txt'")

    with open("users_overview.txt", "w") as users_overview_report:
        users_overview_report.write(tabulate(table, headers, tablefmt="rounded_grid"))
        users_overview_report.write("\n" + "=" * 30 + "\n")
        users_overview_report.write(
            tabulate(table_2, headers_2, tablefmt="rounded_grid")
        )

    print("\n----------------------------\n")
    print(tabulate(table_2, headers_2, tablefmt="rounded_grid"))

    select_menu = "\nEnter a user id number from the table to generate a report\n"
    select_menu += "Enter 'q' if you want to quit\n: "

    while True:
        select_user = input(select_menu)

        if select_user == "q":
            break

        else:
            parse_user_data = {
                "number_of_tasks": 0,
                "completed_tasks": 0,
                "uncompleted_tasks": 0,
                "overdue_tasks": 0,
                "percentage_of_total_tasks": 0,
                "percentage_completed_tasks": 0,
                "percentage_tasks_to_complete": 0,
                "percentage_overdue_tasks": 0,
            }

            for i, key in enumerate(user_database.keys()):
                if int(select_user) == i:
                    filtered_dicts = [
                        d for d in task_database if d.get("username") == key
                    ]
                    for data in filtered_dicts:
                        parse_user_data["number_of_tasks"] += 1
                        if data["completed"]:
                            parse_user_data["completed_tasks"] += 1
                        else:
                            parse_user_data["uncompleted_tasks"] += 1

                        if (
                            data["due_date"].date() < date.today()
                            and not data["completed"]
                        ):
                            parse_user_data["overdue_tasks"] += 1
                        parse_user_data["percentage_tasks_to_complete"] = (
                            100 - parse_user_data["percentage_completed_tasks"]
                        )

                    try:
                        parse_user_data["percentage_of_total_tasks"] = (
                            parse_user_data["number_of_tasks"] / len(task_database)
                        ) * 100
                        parse_user_data["percentage_completed_tasks"] = (
                            100 / parse_user_data["number_of_tasks"]
                        )
                        parse_user_data["percentage_overdue_tasks"] = (
                            parse_user_data["overdue_tasks"]
                            / parse_user_data["number_of_tasks"]
                        ) * 100

                    except ZeroDivisionError:
                        continue

                    headers_user = ["Tasks", "Numbers"]
                    table_user = [
                        ["Total", parse_user_data["number_of_tasks"]],
                        ["Completed", parse_user_data["completed_tasks"]],
                        ["Uncompleted ", parse_user_data["uncompleted_tasks"]],
                        ["Overdue", parse_user_data["overdue_tasks"]],
                        ["Assigned (%)", parse_user_data["percentage_of_total_tasks"]],
                        [
                            "Completed (%)",
                            parse_user_data["percentage_completed_tasks"],
                        ],
                        [
                            "To Complete (%)",
                            parse_user_data["percentage_tasks_to_complete"],
                        ],
                        ["Overdue (%)", parse_user_data["percentage_overdue_tasks"]],
                    ]

                    with open(f"{key}_overview.txt", "w") as user_overview_stats:
                        print(f"\nGenerating Tasks Report for {key}\n")
                        print(f'Your generated report file was saved as "{key}.txt"')
                        user_overview_stats.write(
                            tabulate(table_user, headers_user, tablefmt="rounded_grid")
                        )


def display_statistics(task_database, user_database):
    """A function that takes in two parameters for parsing the data and displaying
    statistics on the screen in a user-friendly manner."""
    num_users = len(user_database.keys())
    num_tasks = len(task_database)

    print("-----------------------------------")
    print(f"Number of users: \t\t {num_users}")
    print(f"Number of tasks: \t\t {num_tasks}")
    print("-----------------------------------")
