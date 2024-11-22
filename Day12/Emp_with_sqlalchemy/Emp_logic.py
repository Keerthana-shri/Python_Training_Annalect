from Emp_db import Database

class Logic:
    def __init__(self):
        self.db = Database()

    def update_employee_location(self, empno, location):
        return self.db.update_employee_location(empno, location)

    def get_all_employees(self):
        return self.db.get_all()

    def get_employee_on_empid(self, empno):
        return self.db.get_on_empid(empno)

    def get_employee_on_location(self, location):
        return self.db.get_on_location(location)