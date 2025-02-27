from pydantic import BaseModel
from typing import Optional

class CompanySchema(BaseModel):
    company_name: str
    location: str

    class Config:
        orm_mode = True 

class EmployeeSchema(BaseModel):
    name: str
    designation: str
    salary: float
    company_name: str

    class Config:
        orm_mode = True