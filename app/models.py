from sqlalchemy import Column, Integer, String, ForeignKey, DECIMAL
from sqlalchemy.orm import relationship
from .database import Base

class Company(Base):
    __tablename__ = "companies"

    id = Column(Integer, primary_key=True, index=True)
    company_name = Column(String, unique=True, index=True)
    location = Column(String, index=True)

    employees = relationship("Employee", back_populates="company")

class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    designation = Column(String)
    salary = Column(DECIMAL(10, 2))
    company_id = Column(Integer, ForeignKey("companies.id"))

    company = relationship("Company", back_populates="employees")