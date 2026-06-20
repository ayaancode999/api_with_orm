from fastapi import FastAPI, Depends,HTTPException
from models import Employees, Customers, Transactions
from database import create_db, get_session
from sqlmodel import Session,select
app=FastAPI(title="Car Dealership", version="1.0.0")

@app.on_event("startup")
def on_startup():
    create_db()

@app.get("/")
def hello_world():
    return "hello world"

@app.post("/customers", response_model=Customers)
def add_customer(customer:Customers,session:Session=Depends(get_session)):
    session.add(customer)
    session.commit()
    session.refresh(customer)
    return customer 
                 
                                                            
@app.post("/employees",response_model=Employees)
def add_employee(employee:Employees,session:Session=Depends(get_session)):
    if employee.national_id:
        existing_id=session.exec(select(Employees).where(Employees.national_id==employee.national_id)).first()
        if existing_id:
            raise HTTPException(status_code=400,detail="employee with id already exists")
    email=session.exec(select(Employees).where(Employees.national_id==employee.national_id)).first()
    if email:
            raise HTTPException(status_code=400,detail="employee with email already exists")
    session.add(employee)
    session.commit()
    session.refresh(employee)
    return employee

@app.get("/employees",response_model=list[Employees])
def get_employees(session:Session=Depends(get_session)):
     return session.exec(select(Employees)).all()

@app.get("/employees/{id}",response_model=Employees)
def employee_id(id:int,session:Session=Depends(get_session)):
     employee=session.get(Employees,id)
     if not employee:
          raise HTTPException(status_code=404,detail="not found")
     return employee

    