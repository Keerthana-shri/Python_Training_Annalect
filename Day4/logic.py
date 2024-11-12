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
    
    def update_task(self,taskid, priority, status, location):
        for i in self.task:
            if i.taskid == taskid:
                i.priority = priority
                i.status = status
                i.location = location
                return True
            else:
                return False
    
    def remove_task(self, taskid):
        for i in self.task:
            if i.taskid == taskid:
                self.task.remove(i)
                return True
        return False
    
    def view_all(self):
        return self.task
    
    def view_on_status(self, status):
        status_tasks = []
        for i in self.task:
            if i.status == status:
                status_tasks.append(i)
        if status_tasks:
            return status_tasks
        return False

    def view_on_priority(self, priority):
        priority_tasks = []
        for i in self.task:
            if i.priority == priority:
                priority_tasks.append(i)
        if priority_tasks:
            return priority_tasks
        return False
    
    def view_on_location(self, location):
        location_tasks = []
        for i in self.task:
            if i.location == location:
                location_tasks.append(i)
        if location_tasks:
            return location_tasks
        return False


