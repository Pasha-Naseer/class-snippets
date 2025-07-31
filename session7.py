# while loop
while True:
    print("Hello")
    break

# print hello x3 (while loop)
counter = 0
while True:
    print("Hello")
    # counter = counter + 1
    counter += 1
    if counter == 3:
        break

# Now it is time for nested while loops
# declare two empty lists
# making relation between todos and their times using indexes
# storing todos
todo_list = []
# storing todo time
todo_time_list = []
# The great while loop
# storing user input for todo name, todo time, and resuming input
while True:
    todo = str(input("Enter todo: "))
    # Not great while loop
    # making sure user doesn't provide invalid data
    while True:
        try:
            todo_hour = int(input("Enter todo hour: "))
        except ValueError:
            print("Invalid Input!")
        else:
            if todo_hour in range(0, 24):
                break
            else:
                print("Invalid Hour!")
    while True:
        try:
            todo_minute = int(input("Enter todo minute: "))
        except ValueError:
            print("Invalid Input")
        else:
            if todo_minute in range(0, 60):
                break
            else:
                print("Invalid Minute!")
    # providing sufficient format with the two variables
    todo_time = f"{todo_hour} : {todo_minute}"

    todo_list.append(todo)
    todo_time_list.append(todo_time)

    resume = str(input("Do you wish to continue(yes/no)? "))
    if resume.lower().strip() == 'no':
        break

# starting the digital clock
# i for hours & j for minutes
for i in range(0, 24):
    for j in range(0, 60):
        # providing sufficient format for the two variables
        time = f"{i} : {j}"
        if time in todo_time_list:
            print(time)
            # ask the users if they want to attend to their todo
            while True:
                flag = "False"
                if i == 23 and j in range(50, 60):
                    check_todo = str(input(f"Do You want to check your todo(yes/no)?"
                                           f"\n({todo_list[todo_time_list.index(time)]}): ")).strip().lower()
                    flag = "True"
                else:
                    check_todo = str(input(f"Do You want to check your todo(yes/no/snooze)?"
                                           f"\n({todo_list[todo_time_list.index(time)]}): ")).strip().lower()
                    flag = "False"
                if check_todo == "yes":
                    break
                if check_todo == "no":
                    break
                elif check_todo == 'snooze':
                    if flag == "False":
                        break
                    else:
                        print("Invalid Input")
                else:
                    print("Invalid Input!")

            if check_todo == "yes":
                print(time, todo_list[todo_time_list.index(time)], 'Done!')
            elif check_todo == "no":
                print(time, todo_list[todo_time_list.index(time)], 'Skipped!')
            elif check_todo == 'snooze':
                # asking the user if he/she wants to snooze manually or 10 minutes by default
                while True:
                    try:
                        check_method = int(input("If you want to snooze for 10 minutes '1'\n"
                                                 "If you want to manually select the new time press '2': "))
                    except ValueError:
                        print("Invalid Input")
                    else:
                        if check_method == 1:
                            break
                        elif check_method == 2:
                            break
                        else:
                            print("Invalid Input")
                if check_method == 2:
                    while True:
                        try:
                            new_todo_hour = int(input("Enter new todo hour: "))
                        except ValueError:
                            print("Invalid Input")
                        else:
                            if new_todo_hour in range(0, 24):
                                if new_todo_hour >= i:
                                    break
                                else:
                                    print("Invalid Input")
                            else:
                                print("Invalid Input")

                    while True:
                        try:
                            new_todo_minute = int(input("Enter new todo minute: "))

                        except ValueError:
                            print('Invalid Input')
                        else:
                            if new_todo_hour == i:
                                if new_todo_minute > j:
                                    break
                            else:
                                if new_todo_minute in range(0, 60):
                                    break

                    new_todo_time = f"{new_todo_hour} : {new_todo_minute}"
                    todo_time_list.append(new_todo_time)
                    todo_list.append(todo_list[todo_time_list.index(time)])

                elif check_method == 1:
                    # emergency variables
                    e = 10
                    z = 1
                    # if 10 minutes snooze will be still in the range of the current hour
                    if j < 50:
                        # add 10 minutes to j (the current minute)
                        e += j
                        new_todo_time = f"{i} : {e}"
                    # if 10 minutes snooze will take us to a new hour
                    elif j >= 50:
                        # ex 22 : 55
                        z += i  # 23
                        e += j  # 65
                        new_j = e - 60
                        new_todo_time = f"{z} : {new_j}"
                    todo_time_list.append(new_todo_time)
                    todo_list.append(todo_list[todo_time_list.index(time)])
        else:
            print(time)
