class Employee:
    def __init__(self, empno, empname, location, deptid):
        self.empno = empno
        self.empname = empname
        self.location = location
        self.deptid = deptid

    def __str__(self):
        return f"Employee Number: {self.empno} - Employee Name: {self.empname} - Employee Location: {self.location} - Employee Dept ID: {self.deptid}"