from sqlalchemy.orm import Session
from .models import Company, Employee
from .schemas import CompanySchema, EmployeeSchema

# ------Companies CRUD operations------
def get_all_companies(db: Session):
    return db.query(Company).all()

def get_company_by_id(db: Session, company_id: int):
    return db.query(Company).filter(Company.id == company_id).first()

def create_company(db: Session, company_data: CompanySchema):
    company = Company(**company_data.model_dump())
    db.add(company)
    db.commit()
    db.refresh(company)
    return company

def delete_company(db: Session, company_id: int):
    company = db.query(Company).filter(Company.id == company_id).first()
    if not company:
        return None
    db.delete(company)
    db.commit()
    return True

# ------Employees CRUD operations------
def get_all_employees(db: Session):
    return db.query(Employee).all()

def get_employee_by_id(db: Session, emp_id: int):
    return db.query(Employee).filter(Employee.id == emp_id).first()

def get_employee_by_email(db: Session, email: str):
    return db.query(Employee).filter(Employee.email == email).first()

def create_employee(db: Session, emp_data: EmployeeSchema):
    company = db.query(Company).filter(Company.company_name == emp_data.company_name).first()
    existing_employee = get_employee_by_email(db, emp_data.email)
    if not company:
        raise ValueError("Company not found!")
    
    if existing_employee:
        raise ValueError("Employee with this email is already present")
    
    new_employee = Employee(
        name = emp_data.name,
        email = emp_data.email,
        designation = emp_data.designation,
        salary = emp_data.salary,
        company = company
    )
    db.add(new_employee)
    db.commit()
    db.refresh(new_employee)
    return new_employee

def update_employee(db: Session, emp_id: int, emp_data: EmployeeSchema):
    employee = db.query(Employee).filter(Employee.id == emp_id).first()
    if not employee:
        return None
    company = db.query(Company).filter(Company.company_name == emp_data.company_name).first()
    if not company:
        raise ValueError("Company not found!")
    
    employee.name = emp_data.name
    employee.designation = emp_data.designation
    employee.salary = emp_data.salary
    employee.company = company

    db.commit()
    db.refresh(employee)
    return employee

def patch_employee(db: Session, emp_id: int, emp_data: EmployeeSchema):
    employee = db.query(Employee).filter(Employee.id == emp_id).first()
    if not employee:
        return None
    if "company_name" in emp_data:
        company = db.query(Employee).filter(Company.company_name == emp_data["company_name"]).first()
        if not company:
            raise ValueError("Company not found!")
        employee.company = company

        for key, value in emp_data.items():
            if hasattr(employee, key):
                setattr(employee, key, value)
        
        db.commit()
        db.refresh(employee)
        return employee
    
def delete_employee(db: Session, emp_id: int):
    employee = db.query(Employee).filter(Employee.id == emp_id).first()
    if not employee:
        return None
    db.delete(employee)
    db.commit()
    return True
