from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from Emp_logic import Logic

app = FastAPI()
logic = Logic()

class UpdateLocationModel(BaseModel):
    location: str

@app.put("/employees/{empno}", status_code=status.HTTP_200_OK)
def update_employee_location(empno: int, location: UpdateLocationModel):
    if logic.update_employee_location(empno, location.location):
        return {"message": "Employee location updated successfully"}
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Employee not found")

@app.get("/employees", status_code=status.HTTP_200_OK)
def get_all_employees():
    employees = logic.get_all_employees()
    if employees:
        return {"employees": employees}
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No employees found")

@app.get("/employees/{empno}", status_code=status.HTTP_200_OK)
def get_employee_by_id(empno: int):
    employee = logic.get_employee_on_empid(empno)
    if employee:
        return {"employee": employee}
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Employee not found")

@app.get("/employees/location/{location}", status_code=status.HTTP_200_OK)
def get_employees_by_location(location: str):
    employees = logic.get_employee_on_location(location)
    if employees:
        return {"employees": employees}
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No employees found in this location")


