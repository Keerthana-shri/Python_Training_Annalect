#QUESTION: CREATE A LIST WITH DICTIONARY AS ELEMENTS AND CREATE A MENU WITH FUNCTIONS:
#ADD TASK, UPDATE TASK, REMOVE TASK, PRINT ALL TASK AND EXIT

all_task=[]

def add_task(taskid,status):
    task={"taskid": taskid, "status": status}
    all_task.append(task)
    return f"Task{taskid} is added"

def update_task(taskid,new_status):
        for task in all_task:
            if task["taskid"] == taskid:
                task["status"] = new_status
                return(f"Task {taskid} is updated to {new_status}")
        return (f"Task {taskid} is not found")

def remove_task(taskid):
    for task in all_task:
        if task["taskid"] == taskid:
            all_task.remove(task)
            print(f"Task {taskid} is removed")
            return
    return (f"Task {taskid} is not found")

def print_all_tasks(): 
    #print(all_task)       
    if all_task:
        return all_task
    else:
        return ("No tasks available.")

def start():
    while True:
        print("\nChoose an option:")
        print("1. Add Task")
        print("2. Update Task")
        print("3. Remove Task")
        print("4. Print All Tasks")
        print("5. Exit")
        
        choice = input("Enter choice (1-5): ")
        if choice == "1":
            taskid = input("Enter task ID: ")
            status = input("Enter task status: ")
            a = add_task(taskid, status)
            print(a)
        
        elif choice == "2":
            taskid = input("Enter task ID to update: ")
            new_status = input("Enter new status: ")
            b= update_task(taskid, new_status)
            print(b)
        
        elif choice == "3":
            taskid = input("Enter task ID to remove: ")
            c= remove_task(taskid)
            print(c)
        
        elif choice == "4":
            d=print_all_tasks()
            for task in d:
                print(f"taskId: {task['taskid']} , status: {task['status']}")
        
        elif choice == "5":
            print("Exiting program.")
            break
        
        else:
            print("Invalid choice, please try again.")

start()