from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from .database import get_db
from .schemas import EmployeeSchema
from .crud import *

app = FastAPI()

# ------ COMPANY ENDPOINTS ------
@app.get('/companies/')
def read_companies(db: Session = Depends(get_db)):
    return get_all_companies

@app.get('/companies/{company_id}')
def read_company(company_id, db: Session = Depends(get_db)):
    company = get_company_by_id(db, company_id)
    if not company:
        raise HTTPException(status_code=404, detail="Company not found!")
    return company

@app.post('/companies/')
def add_company(company_data: CompanySchema, db: Session = Depends(get_db)):
    return create_company(db, company_data)

@app.delete('/companies/{company_id}')
def remove_company(company_id: int, db: Session = Depends(get_db)):
    if not delete_company(db, company_id):
        raise HTTPException(status_code=404, detail="Company not found!")
    return {"message" : "Company deleted successfully"}


# ------ EMPLOYEE ENDPOINTS ------
@app.get('/employees/')
def read_employees(db: Session = Depends(get_db)):
    return get_all_employees(db)

@app.get('/employees/{emp_id}')
def read_employee(emp_id: int, db: Session = Depends(get_db)):
    employee = get_employee_by_id(db, emp_id)
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found!")
    return employee

@app.post('/employees/')
def add_employee(emp_data: EmployeeSchema, db: Session = Depends(get_db)):
    try:
        return create_employee(db, emp_data)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@app.put('employees/{emp_id}')
def modify_employee(emp_id: int, emp_data: EmployeeSchema, db: Session = Depends(get_db)):
    updated_employee = update_employee(db, emp_id, emp_data)
    if not update_employee:
        raise HTTPException(status_code=404, detail="Employee not found!")
    return update_employee

@app.patch('/employees/{emp_id}')
def partial_update_employee(emp_id: int, emp_data: dict, db: Session = Depends(get_db)):
    try:
        update_employee = patch_employee(db, emp_id, emp_data)
        if not update_employee:
            raise HTTPException(status_code=404, detail="Employee not found!")
        return update_employee
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.delete('/employees/{emp_id}')
def remove_employee(emp_id: int, db: Session = Depends(get_db)):
    if not delete_employee(db, emp_id):
        raise HTTPException(status_code=404, detail="Employee not found!")
    return {"message" : "Employee deleted successfully"}
