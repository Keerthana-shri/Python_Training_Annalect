from fastapi import FastAPI, HTTPException, UploadFile, File, Depends
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from pydantic import BaseModel, ValidationError
from enum import Enum
from logic import Logic
import csv
import io
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()
logic = Logic()
security = HTTPBasic()

# Load credentials from environment variables
VALID_USERNAME = os.getenv("VALID_USERNAME")
VALID_PASSWORD = os.getenv("VALID_PASSWORD")

def login_and_authenticate(credentials: HTTPBasicCredentials = Depends(security)):
    if credentials.username == "" and credentials.password == "":
        raise HTTPException(status_code=401, detail="Username and password are missing")
    elif credentials.username == "":
        raise HTTPException(status_code=401, detail="Username is missing")
    elif credentials.password == "":
        raise HTTPException(status_code=401, detail="Password is missing")
    elif credentials.username != VALID_USERNAME or credentials.password != VALID_PASSWORD:
        raise HTTPException(status_code=401, detail="Your login credentials are not right, try again with right one")
    else:
        return {"message": "Login successful"}

class Grade(str, Enum):
    M1 = "M1"
    M2 = "M2"
    M3 = "M3"

class EmployeeModel(BaseModel):
    first_name: str
    last_name: str
    date_of_birth: str  # Expecting MM/DD/YYYY format
    date_of_joining: str  # Expecting MM/DD/YYYY format
    grade: Grade

class UpdateEmployeeModel(BaseModel):
    first_name: str = None
    last_name: str = None
    date_of_birth: str = None  # Expecting MM/DD/YYYY format
    date_of_joining: str = None  # Expecting MM/DD/YYYY format
    grade: str = None 

@app.post("/login", dependencies=[Depends(login_and_authenticate)])
def login():
    return {"message": "Login successful"}

@app.post("/employees", dependencies=[Depends(login_and_authenticate)])
def create_employee(employee: EmployeeModel):
    try:
        emp = logic.create_employee(
            first_name=employee.first_name,
            last_name=employee.last_name,
            date_of_birth=employee.date_of_birth,
            date_of_joining=employee.date_of_joining,
            grade=employee.grade
        )
        if emp:
            return {
                "message": f"Employee details of {emp.first_name} {emp.last_name} have been added successfully."
            }
        else:
            return {
                "message": f"Employee details of {employee.first_name} {employee.last_name} are already available."
            }
    except ValidationError as e:
        raise HTTPException(status_code=422, detail="The provided grade is invalid")

@app.get("/employees/{emp_id}", dependencies=[Depends(login_and_authenticate)])
def get_employee(emp_id: int):
    emp = logic.get_employee(emp_id)
    if emp:
        return {
            "id": emp.id,
            "first_name": emp.first_name,
            "last_name": emp.last_name,
            "date_of_birth": emp.date_of_birth,
            "date_of_joining": emp.date_of_joining,
            "grade": emp.grade
        }
    else:
        raise HTTPException(status_code=404, detail="Employee not found")

@app.get("/employees", dependencies=[Depends(login_and_authenticate)])
def get_all_employees():
    employees = logic.get_all_employees()
    return [
        {
            "id": emp.id,
            "first_name": emp.first_name,
            "last_name": emp.last_name,
            "date_of_birth": emp.date_of_birth,
            "date_of_joining": emp.date_of_joining,
            "grade": emp.grade
        }
        for emp in employees
    ]

@app.put("/employees/{emp_id}", dependencies=[Depends(login_and_authenticate)])
def update_employee(emp_id: int, updates: UpdateEmployeeModel):
    if updates.grade and updates.grade not in Grade.__members__:
        raise HTTPException(status_code=422, detail="The entered grade is invalid")
    
    try:
        emp = logic.update_employee(emp_id, updates.dict(exclude_unset=True))
        if emp:
            return {
                "message": f"Employee details of {emp.first_name} {emp.last_name} have been updated successfully."
            }
        else:
            return {
                "message": f"Failed to update employee details."
            }
    except ValidationError as e:
        raise HTTPException(status_code=422, detail="The entered grade is invalid")


@app.post("/upload-csv", dependencies=[Depends(login_and_authenticate)])
def upload_csv(file: UploadFile = File(...)):
    content = file.file.read().decode("utf-8")
    print(content)
    logic.upload_csv(content)
    return {"message": "CSV file uploaded successfully"}