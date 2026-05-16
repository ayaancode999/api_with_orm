from fastapi import FastAPI
from models import Employees
from database import create_db, get_session
app=FastAPI(title="Car Dealership", version="1.0.0")

@app.on_event("startup")
def on_startup():
    create_db()

@app.get("/")
def hello_world():
    return "hello world"

# @app.post("/employees")
# def 