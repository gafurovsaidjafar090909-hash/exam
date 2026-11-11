from fastapi import FastAPI
from .database import Base, engine
from . import models
from .routers import Project, Employee, Task

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(Project.router)
app.include_router(Employee.router)
app.include_router(Task.router)
