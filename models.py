from sqlmodel import SQLModel,Field,Relationship
from typing import Optional,List
from datetime import date
from enum import Enum

class Employee_Role(str,Enum):
    salesperson = "salesperson"
    manager = "manager"
    mechanic = "mechanic"
    receptionist = "receptionist"
    finance_officer = "finance_officer"

class Employees(SQLModel,table=True):
    id:Optional[int]=Field(default=None,primary_key=True)
    full_name:str
    date_of_birth:Optional[date]=None
    role:Employee_Role
    hiring_date:date=Field(default_factory=date.today)
    salary:float
    status:bool=True
    #add list of sales


