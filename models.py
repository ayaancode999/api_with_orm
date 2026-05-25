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

class Payment_Method(str,Enum):
    CREDIT_CARD="Credit card"
    CASH="Cash"
    BANK_TRANSFER="Bank transfer"
    FINANCING="Financing"
    LEASE="Lease"

class Transaction_status(str,Enum):
    PENDING="Pendng"
    COMPLETE="Complete"
    CANCELLED="Cancelled"
    REFUNDED="Refunded"

class Transactions(SQLModel, table=True):
    id:Optional[int]=Field(default=None, primary_key=True)
    car_id:int=Field(foreign_key="cars.id")
    customer_id:int=Field(foreign_key="customers.id")
    employees_id:Optional[int]=Field(default=None, foreign_key="employees.id")
    sale_price:int
    discount:int=0
    tax:float=0
    total_amount:int
    payment_method:Payment_Method=Payment_Method.CREDIT_CARD
    financing_bank:Optional[str]=None
    financing_term_months:Optional[int]=None
    down_payment:Optional[int]=None
    monthly_installments:Optional[float]=None
    interest_rate:Optional[float]=None
    transaction_status:Transaction_status=Transaction_status.PENDING
    sale_date:date=Field(default_factory=date.today)
    delivery_date:Optional[int]=None
    notes:Optional[str]=None
    cars:Optional[Cars]=Relationship(back_populates="transactions",sa_relationship={"foreign_keys": "[Transactions.car_id]"},)
    customers:Optional[Customers]=Relationship(back_populates="transactions")
    employees:Optional[Employees]=Relationship(back_populates="transactions")



    