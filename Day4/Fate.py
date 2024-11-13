from presentation import presentation
from logic import logic
from task import Task

def fate():

    logic_object=logic()
    # presentation_object=presentation()


    from task import Task
    task_object = [
            Task(1, "Marathon", 1, "running", "cbe"),
            Task(2, "Speedwalk", 6, "walking", "chennai")
        ]

    for Task in task_object:
        a= logic_object.add(Task)
        if a == True:
             print("Added")
        else:
             print("Failed")

    # Logic for Adding only 1 task:    
    # adding_logic_object= logic_object.add(task_object) 
    # adding_logic_object= logic_object.add(task_object)-----> if this statement is added again,
    # the condition will be False, bcoz we have already added the task in line 14, 
    # and now if we agin try to add the same task, the condition become False
    
    b= logic_object.update_task(1, 6, "running", "bglr")
    if b == True:
        print ("Task is updated")
    else:
        print ("Task ID not found")


    c= logic_object.remove_task(2)
    if c == True:
        print("Task is removed")
    else:
        print("TaskID not found")
    
    d= logic_object.view_all()
    print("All tasks are listed below:")
    for i in d:
        print(i)

    e= logic_object.view_on_status("running")
    print("Tasks listed based on status:")
    for i in e:
        print(i)
    
    f= logic_object.view_on_priority(6)
    print("Tasks listed based on priotity:")
    for i in f:
        print(i)

    g= logic_object.view_on_location("bglr")
    print("Tasks listed based on location:")
    for i in g:
        print(i)
    
    
    # using the object we are calling the function
    # presentation_object.f1()
    # logic_object.f2()
    # task_object.f3()


   
if __name__ == "__main__":
    fate()

