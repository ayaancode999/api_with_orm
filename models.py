from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from datetime import date
from enum import Enum


class Employee_Role(str, Enum):
    salesperson = "salesperson"
    manager = "manager"
    mechanic = "mechanic"
    receptionist = "receptionist"
    finance_officer = "finance_officer"


class Employees(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    full_name: str
    date_of_birth: Optional[date] = None
    role: Employee_Role
    hiring_date: date = Field(default_factory=date.today)
    salary: float
    status: bool = True
    # add list of sales


class Customers(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    full_name: str
    date_of_birth: Optional[date] = None
    phone_number:int
    national_id:Optional[str]=Field(default=None,unique=True)
    email:Optional[str]=Field(unique=True)
    address:Optional[str]=None
    membership:bool=False
    register_date:date=Field(default_factory=date.today)
    # add list of purchases 

class Car_Brand(str,Enum):
    TOYOTA = "Toyota"
    FORD = "Ford"
    BMW = "BMW"
    VOLKSWAGEN = "Volkswagen"
    MERCEDES_BENZ = "Mercedes-Benz"
    HONDA = "Honda"
    HYUNDAI = "Hyundai"
    TESLA = "Tesla"
    NISSAN = "Nissan"
    AUDI = "Audi"


class Condition(str, Enum):
    USED="Used"
    NEW="New"


class Fuel_type(str, Enum):
    ELECTRIC="Electric"
    HYBRID="Hybrid"
    DIESEL="Diesel"
    PETROL="Petrol"

class Transmission(str, Enum):
    AUTOMATIC="Automatic"
    MANUAL="Manual"

class Drive_type(str, Enum):
    FOUR_WHEEL_DRIVE="4WD"
    FORWARD_WHEEL_DRIVE="FWD"
    BACKWARD_WHEEL_DRIVE="BWD"

class In_stock(str, Enum):
    SOLD="Sold"
    IN_STOCK="In stock"

class Cars(SQLModel, table=True):
    id : Optional[int] = Field(default=None, primary_key=True)
    vin_number:str=Field(unique=True,max_length=17,min_length=17)
    maker:Car_Brand
    model:str
    colour:str
    trim:str
    date_of_creation:date
    fuel_type:Fuel_type
    condition:Condition=Condition.NEW
    transmission:Transmission
    drive_type:Drive_type
    horse_power:int
    engine_capacity:float
    seats:int
    mileage:int=0
    cost_price:float
    retail_price:float
    minimum_price:float
    in_stock:In_stock





    