lst = []

while True:

    print("To Do List")
    print("1. To add task")
    print("2. To update task")
    print("3. To view all task")
    print("4. To exit")
    to_do = int(input("Enter the task number you want to perform: "))
    if to_do == 1:
        add = input("Enter a task: ")
        lst.append(add)
    elif to_do == 2:

        choice = int(input("Enter \n 6. To remove a task \n 7. to add task: \n " ))
        if choice == 6:
            rem = input("Enter the task you want to remove: ")
            if rem in lst :
                lst.remove(rem)
                print("removing the task")
        elif choice == 7:
            ad = input("Enter a task: ")
            lst.append(ad)
    elif to_do == 3:
        print(lst)
    elif to_do == 4:
        print("Exiting the To Do List ")
        break
    else:
        print("Enter a valid option!!")
