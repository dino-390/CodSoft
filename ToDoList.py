#create an array
tasks=[]

#addingtask logic
def addingtask():
    task = input("Enter your Task ToDo: ")
    tasks.append(task)
    print(task, "task has been added succesfully")

#viewtask logic
def viewtask():
    if not tasks:
        print("No tasks are available")
    else:
        print("Available tasks:")
        for index, task in enumerate(tasks):
            print(f"{index}.{task}")

#deletetask logic
def deltask():
    viewtask()
    try:
        tasktodelete = int(input("Enter the task number to delete: "))
        if tasktodelete < len(tasks) and tasktodelete >=0:
            tasks.pop(tasktodelete)
            print("The task has been deleted succesfully")
        else:
            print("The task was not found")
    except:
        print("Invalid input")

#creating main method

print("ToDoList Application")
 #logic of the applicaion
while True:
    print("--------------------")
    print("Select your option:")
    print("1) Add a task")
    print("2) View all tasks")
    print("3) Delete a task")
    print("4) Exit")

    choice = input("Enter your choice: ")
    if(choice == "1"):
        addingtask()
    elif(choice == "2"):
        viewtask()
    elif(choice == "3"):
        deltask()
    elif(choice == "4"):
        break
    else:
        print("The choice is invalid")
        
