import sqlite3

class Database:
    def __init__(self, db_name="employee.db"):
        """Initialize the database connection."""
        self.db_name = db_name

    def connect(self):
        """Create a new database connection."""
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()

    def create_table(self):
        """Create the Employee table if it doesn't exist."""
        self.connect()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Employee (
                empno INTEGER PRIMARY KEY,
                empname TEXT NOT NULL,
                location TEXT NOT NULL,
                deptid INTEGER NOT NULL
            )
        ''')
        self.connection.commit()
        self.connection.close()

    def update_employee_location(self, empno, location):
        """Update an existing employee's location."""
        self.connect()
        self.cursor.execute('''
            UPDATE Employee
            SET location = :location
            WHERE empno = :empno
        ''', {'location': location, 'empno': empno})
        self.connection.commit()
        updated = self.cursor.rowcount > 0
        self.connection.close()
        return updated

    def get_all(self):
        """List all employees in the database."""
        self.connect()
        self.cursor.execute('SELECT * FROM Employee')
        employees = self.cursor.fetchall()
        self.connection.close()
        return employees

    def get_on_empid(self, empno):
        """View an employee by empno."""
        self.connect()
        self.cursor.execute('SELECT * FROM Employee WHERE empno = :empno', {'empno': empno})
        employee = self.cursor.fetchall()
        self.connection.close()
        return employee

    def get_on_location(self, location):
        """View employees by location."""
        self.connect()
        self.cursor.execute('SELECT * FROM Employee WHERE location = :location', {'location': location})
        employees = self.cursor.fetchall()
        self.connection.close()
        return employees

