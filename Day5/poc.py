class Task:

    def __init__(self,taskid,taskname,priority,status,location):
        self.taskid=taskid
        self.taskname=taskname
        self.priority=priority
        self.status=status
        self.location=location
    
    def __str__(self):
        return f"Taskid: {self.taskid} - Taskname: {self.taskname} - Priority: {self.priority} - Status: {self.status} - Location: {self.location}"
        

all_tasks = [
    Task(1, "Cooking", 1, "done", "home"),
    Task(2, "Drawing", 3, "not done", "school"),
    Task(3, "Dancing", 2, "done", "extra class"),
]

def sort_by_priority(all_tasks):
    return sorted(all_tasks, key=lambda x: x.priority)

def sort_by_location(all_tasks):
    return sorted(all_tasks, key=lambda x: x.location)

def filter_by_location(all_tasks, location):
    return [x for x in all_tasks if x.location == location]

print("Sorting based on priority")
a=sort_by_priority(all_tasks)
for i in a:
    print(i)

print("Sorting based on location")
b=sort_by_location(all_tasks)
for i in b:
    print(i)

print("Filtering based on location ")
c= filter_by_location(all_tasks,"school")
for i in c:
    print(i)

