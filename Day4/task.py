class Task:

    def __init__(self,taskid,taskname,priority,status,location):
        self.taskid=taskid
        self.taskname=taskname
        self.priority=priority
        self.status=status
        self.location=location
    
    def __str__(self):
        return f"Taskid: {self.taskid} - Taskname: {self.taskname} - Priority: {self.priority} - Status: {self.status} - Location: {self.location}"
        