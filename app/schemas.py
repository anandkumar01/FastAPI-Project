from pydantic import BaseModel
from typing import Optional

class CompanySchema(BaseModel):
    company_name: str
    location: str

    class Config:
        from_attributes = True 

class EmployeeSchema(BaseModel):
    name: str
    email: str
    designation: str
    salary: float
    company_name: str

    class Config:
        from_attributes = True