import sqlite3

def view_all():
    connection = sqlite3.connect("employee.db")
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM Employee')
    employees = cursor.fetchall()
    connection.close()
    return employees

if __name__ == "__main__":
    employees = view_all()
    for emp in employees:
        print(emp)