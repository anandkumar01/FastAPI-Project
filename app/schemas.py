from pydantic import BaseModel, EmailStr

class CompanySchema(BaseModel):
    id: int
    company_name: str
    location: str

    class Config:
        from_attributes = True 

class EmployeeSchema(BaseModel):
    name: str
    email: EmailStr
    designation: str
    salary: float
    company_name: str

class EmployeeResponse(BaseModel):
    id: int
    name: str
    email: str
    designation: str
    salary: float
    company: CompanySchema

    class Config:
        from_attributes = True