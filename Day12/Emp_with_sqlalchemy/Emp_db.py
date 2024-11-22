from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Step 1: Define the Database URL
DATABASE_URL = "sqlite:///./employee.db"

# Step 2: Create the SQLAlchemy engine
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Step 3: Create the Base class for the models
Base = declarative_base()

# Step 4: Define the Employee model (table)
class Employee(Base):
    __tablename__ = 'employees'

    empno = Column(Integer, primary_key=True, index=True)
    empname = Column(String, nullable=False)
    location = Column(String, nullable=False)
    deptid = Column(Integer, nullable=False)

    def __repr__(self):
        return f"Employee(empno={self.empno}, empname={self.empname}, location={self.location}, deptid={self.deptid})"

# Step 5: Create the session maker
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Step 6: Create the tables in the database
Base.metadata.create_all(bind=engine)

# Step 7: CRUD Operations
class Database:
    def __init__(self):
        self.Session = SessionLocal

    def create_table(self):
        Base.metadata.create_all(bind=engine)

    def update_employee_location(self, empno, location):
        session = self.Session()
        employee = session.query(Employee).filter(Employee.empno == empno).first()
        if employee:
            employee.location = location
            session.commit()
            session.close()
            return True
        session.close()
        return False

    def get_all(self):
        session = self.Session()
        employees = session.query(Employee).all()
        session.close()
        return employees

    def get_on_empid(self, empno):
        session = self.Session()
        employee = session.query(Employee).filter(Employee.empno == empno).first()
        session.close()
        return employee

    def get_on_location(self, location):
        session = self.Session()
        employees = session.query(Employee).filter(Employee.location == location).all()
        session.close()
        return employees