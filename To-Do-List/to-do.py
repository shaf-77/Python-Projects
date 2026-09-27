tasks = [] #this list holds all the tasks we add (each task will be dictionary with 2 keys->task description, status)

#this will display the options for the user every time they run the program
def show_menu():
    print("\n--- TO-DO LIST ---")
    print("1. Add Task")
    print("2. View Task")
    print("3. Mark Task as Done ")
    print("4. Delete Task")
    print("5. Exit")

def add_task():
    task = input("Enter task:")
    tasks.append({"task":task, "done":False})        #this is used to add/store new task at the end of the list
    print(f"Task '{task}' added!")   #this is the confirmation message to the user

def view_task():
    if not tasks:
        print("No tasks yet!")
        return
    print("\nYour Tasks:")
    for index, task in enumerate(tasks, start=1):
        status="✅" if task["done"] else "❌"
        print(f"{index}. {task['task']} [{status}]")

def mark_done():
    view_task()     #so the user could decide which has to be marked as done instead of guessing the index
    if not tasks:
        return
    try:
        index=int(input("Enter task number to mark done:"))-1  #-1 shifts the user's task number into the correct Python index
        if 0 <= index < len(tasks): #index entered by the user shouldn't be -ve or larger than the no. of tasks
            tasks[index]["done"]=True
            print("Marked as done!")
        else:
            print("Invalid number!")
    except ValueError: #it shows a message when user enters string or enters nothing at all
        print("Please enter a valid number.")

def delete_task():
    view_task()
    if not tasks:
        return
    try:
        index=int(input("Enter task number to delete:"))-1
        if 0<= index < len(tasks):
            removed=tasks.pop(index)
            print(f"Deleted task: {removed['task']}")
        else:
            print("Invalid number!")
    except ValueError:
        print("Please enter a valid number.")

while True:   #we want this loop to run forever or atleast until the user wants to exit
    show_menu()
    choice=input("Choose a number (1-5):")

    if choice == '1':
        add_task()
    elif choice == '2':
        view_task()
    elif choice == '3':
        mark_done()
    elif choice == '4':
        delete_task()
    elif choice == '5':
        print("Goodbye!")
        break  #this ends the while loop
    else:
        print("Invalid choice. Try again!")
