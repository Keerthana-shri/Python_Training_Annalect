import csv

class Emp:
    def __init__(self,empno, deptid):
        self.empno= empno
        self.deptid= deptid
    
    def __str__(self):
        return f"Employee Number: {self.empno} - Employee Department ID: {self.deptid}"
    
    def to_csv_row(self):
        return [self.empno, self.deptid]
       
    @classmethod
    def from_csv_row(cls, row):
        empno, deptid = row
        a= cls(int(empno), int(deptid))
        return a


def write_emp_to_csv(i, filename='emp.csv'):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(Emp.to_csv_row())
        print("Success")
        

def read_from_csv(filename='emp.csv'):
    with open(filename, mode='r', newline='') as file:
        reader = csv.reader(file)
        # Write the header row
        next(reader) # Skip the header row
        for row in reader:
            emp_object = Emp.from_csv_row(row)
        return emp_object

emp_object_from_file = read_from_csv("emp.csv")
print(emp_object_from_file)      

emp_object1= Emp(1, 90)
write_emp_to_csv(emp_object1, "emp.csv")

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
