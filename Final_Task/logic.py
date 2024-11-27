from db import Database, Employee
from datetime import datetime

class Logic:
    def __init__(self):
        self.db = Database()

    def search_employees(self, emp_id, first_name, last_name):
        employees = self.db.search_employees(emp_id, first_name, last_name)
        for emp in employees:
            emp.date_of_birth = emp.date_of_birth.strftime('%m/%d/%Y')
            emp.date_of_joining = emp.date_of_joining.strftime('%m/%d/%Y')
        return employees

    def create_employee(self, first_name, last_name, date_of_birth, date_of_joining, grade):
        date_of_birth = datetime.strptime(date_of_birth, '%m/%d/%Y').date()
        date_of_joining = datetime.strptime(date_of_joining, '%m/%d/%Y').date()
        
        employee = Employee(
            first_name=first_name,
            last_name=last_name,
            date_of_birth=date_of_birth,
            date_of_joining=date_of_joining,
            grade=grade
        )
        return self.db.create_employee(employee)

    def get_employee(self, emp_id):
        employee = self.db.get_employee(emp_id)
        if employee:
            employee.date_of_birth = employee.date_of_birth.strftime('%m/%d/%Y')
            employee.date_of_joining = employee.date_of_joining.strftime('%m/%d/%Y')
        return employee

    def update_employee(self, emp_id, updates):
        if 'date_of_birth' in updates:
            updates['date_of_birth'] = datetime.strptime(updates['date_of_birth'], '%m/%d/%Y').date()
        if 'date_of_joining' in updates:
            updates['date_of_joining'] = datetime.strptime(updates['date_of_joining'], '%m/%d/%Y').date()
        employee = self.db.update_employee(emp_id, updates)
        if employee:
            employee.date_of_birth = employee.date_of_birth.strftime('%m/%d/%Y')
            employee.date_of_joining = employee.date_of_joining.strftime('%m/%d/%Y')
        return employee

    def upload_csv(self, csv_content):
        return self.db.upload_csv(csv_content)

