from presentation import presentation
from logic import logic
from task import Task

def fate():
    # print(f"Hello")
    # presentation_object=presentation()

    task_object=Task(1,"run", 1, "done", "cbe")
    print(task_object)

    logic_object=logic()
    
    adding_logic_object= logic_object.add(task_object)
    # adding_logic_object= logic_object.add(task_object)-----> if this statement is added again,
    # the condition will be False, bcoz we have already added the task in line 14, 
    # and now if we agin try to add the same task, the condition become False
    if adding_logic_object:
        print("Added")
    else:
        print("Failed")
   
    a= logic_object.view_all()
    for i in a:
        print(i)

    b= logic_object.update_task()
    
    # using the object we are calling the function
    # presentation_object.f1()
    # logic_object.f2()
    # task_object.f3()

    
    #print(task)

   
if __name__ == "__main__":
    fate()

