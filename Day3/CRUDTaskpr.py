import CRUDTasklogic

def main():
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
            a = CRUDTasklogic.add_task(taskid, status)
            print(a)
        
        elif choice == "2":
            taskid = input("Enter task ID to update: ")
            new_status = input("Enter new status: ")
            b= CRUDTasklogic.update_task(taskid, new_status)
            print(b)
        
        elif choice == "3":
            taskid = input("Enter task ID to remove: ")
            c= CRUDTasklogic.remove_task(taskid)
            print(c)
        
        elif choice == "4":
            d=CRUDTasklogic.print_all_tasks()
            print(d)
        
        elif choice == "5":
            print("Exiting program.")
            break
        
        else:
            print("Invalid choice, please try again.")

main()