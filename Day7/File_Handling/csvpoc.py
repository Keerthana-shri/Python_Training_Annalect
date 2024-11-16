'''Importing necessary modules'''
import csv

class Emp:
    def __init__(self, empno, deptid):
        '''Initialize employee with employee number and department ID'''
        self.empno = empno
        self.deptid = deptid
    
    def __str__(self):
        '''Returns a formatted string with the employee's number and department ID'''
        return f"Employee Number: {self.empno} - Employee Department ID: {self.deptid}"
    
    def to_csv_row(self):
        '''Converts the employee object to a list for CSV writing'''
        return [self.empno, self.deptid]
       
    @classmethod
    def from_csv_row(cls, row):
        '''Creates an employee object from a CSV row'''
        empno, deptid = row
        return cls(int(empno), int(deptid))


def write_emp_to_csv(emp, filename='emp.csv'):
    '''Writes an employee object to a CSV file'''
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['empno', 'deptid'])  # Write the header row
        writer.writerow(emp.to_csv_row())  # Write the employee data
        print("Success")


def read_from_csv(filename='emp.csv'):
    '''Reads employee data from a CSV file and returns an employee object'''
    with open(filename, mode='r', newline='') as file:
        reader = csv.reader(file)
        try:
            next(reader)  # Skip the header row
        except StopIteration:
            print("The file is empty.")
            return None
        for row in reader:
            emp_object = Emp.from_csv_row(row)
        return emp_object


emp_object1 = Emp(1, 90)
'''Write the employee object to a CSV file'''
write_emp_to_csv(emp_object1, "emp.csv")

'''Read the employee object from the CSV file'''
emp_object_from_file = read_from_csv("emp.csv")
print(emp_object_from_file)



'''
Another way of writing the code:

import csv
 
class Emp:
    def __init__(self, emp_no, dept_id):
        self.emp_no = emp_no
        self.dept_id = dept_id
 
    def to_csv_row(self):
        return [self.emp_no, self.dept_id ]
 
    def __str__(self):
        return f"emp no: {self.emp_no}, dept id: {self.dept_id}"
 
    @classmethod
    def from_csv_row(cls, row):
        emp_no, dept_id = row
        return cls(int(emp_no), int(dept_id))
 
def write_emp_to_csv(emp, filename='emp.csv'):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
       
        # Write the header row
        writer.writerow(['emp_no', 'dept_id'])
       
        # Write each product as a row in the CSV
        writer.writerow(emp.to_csv_row())
 
def read_emp_from_csv(filename='emp.csv'):
    emp = []
    with open(filename, mode='r') as file:
        reader = csv.reader(file)
       
        # Skip the header row
        next(reader)
       
        # Read each row and create a Product object
        for row in reader:
            emp_detail = Emp.from_csv_row(row)
            emp.append(emp_detail)
 
    return emp
 
emp1 = Emp(1,145)
write_emp_to_csv(emp1)
emp_read = read_emp_from_csv()
for emp in emp_read:
    print(emp)

'''
