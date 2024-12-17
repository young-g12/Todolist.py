# Create a to-do list program that lets the user add, remove, and view tasks they need to complete.
task_list = []

while True:
    display_options.lower() = ["add task", "remove task", "view task", "exit"]
    print(display_options)
    choose_task = input("Which choice would you like to make?: ")
    if choose_task == display_options[0]:
        print("add task")
        input_task = input("enter task: ")
        task_list.append(input_task)
        print(input_task)
    elif choose_task == display_options[1]:
        task_list.remove(input(f"Which task would you like to remove?: "))
        print("Task removed")
    elif choose_task == display_options[2]:
        print(task_list)
    elif choose_task == display_options[3]:
        break
    else:
        print("Invalid option, please choose another choice")
    
