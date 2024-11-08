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
        for task in all_task:
            return(f"taskId: {task['taskid']} , status: {task['status']}")
    else:
        return ("No tasks available.")