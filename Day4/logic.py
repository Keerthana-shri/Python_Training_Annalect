from task import Task

class logic:
    def __init__(self):
        self.task=[]

    def add(self,task_object):
        for i in self.task:
            if i.taskid == task_object.taskid:
                return False
        self.task.append(task_object)
        return True
    
    def view_all(self):
        return self.task
    
    def update_task(self,taskid, priority, status, location):
        for i in self.task:
            if i.taskid == taskid:
                i.priority = priority
                i.status = status
                i.location = location
                return f"Task {taskid} is updated"
            return f"Task {taskid} is not found"

