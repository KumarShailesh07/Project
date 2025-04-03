def task():
    tasks = [] #empty list
    print("-------WELCOME TO TASK MANAGEMENT APP-------")

    total_task = int(input("Enter how many task you want to add:")) #such as 3
    for i in range(1,total_task+1):
        tasks_name = input(f"Enter task {i}:").lower() #Enter task 1:
        tasks.append(tasks_name) #task name added in list
    print(f"Today's tasks are:{tasks}")

    while True :
        operation = int(input("Enter:\n1-Add\n2-Update\n3-Delete\n4-view\n5-Exit/stop/"))
        if operation == 1:
            add = input("Enter the task you want to add:").lower() #to add new task
            tasks.append(add) #task added to the list
            print(f"Task {add} has been added successfully...")

        elif operation == 2:
            update_val = input("Enter the task you want to update:").lower()
            if update_val in tasks:
                up = input("Enter the task:") #new task to update with old task
                ind = tasks.index(update_val) #to get index of old task
                tasks[ind] = up #replace old task with new one at that particular index
                print(f"The updated task are {up} ")

        elif operation == 3:
            delete_val = input("Enter the task you want to delete:").lower() #to get value you want to delete
            if delete_val in tasks:
                ind = tasks.index(delete_val) #to get index of the delete_val task
                del tasks[ind] #delete the task successfully
                print(f"Task {delete_val} has been deleted successfully...")
                
        elif operation == 4:
            print(f"Today's tasks are:{tasks}")

        elif operation == 5:
            print("Closing the program...")
            break

        else:
            print("Invalid input")

task()