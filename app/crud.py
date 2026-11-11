from sqlalchemy import select
from sqlalchemy.orm import Session
from . import models, schemas


def get_Project(db: Session):
    return db.scalars(select(models.Project)).all()

def get_Project_id(db: Session, Project_id: int):
    return db.get(models.Project, Project_id)

def create_Project(db: Session, data: schemas.ProjectCreate):
    project = models.Project(**data.model_dump())
    db.add(project)
    db.commit()
    db.refresh(project)
    return project


def update_project(db: Session, project_id: int, project_data:schemas.ProjectUpdate):
    data = project_data.model_dump(exclude_unset=True)
    project = db.get(models.Project, project_id)
    if project:
        for key, value in data.items():
            setattr(project, key, value)
        db.commit()
        db.refresh(project)
    return project


def delete_project(db: Session, project_id: int):
    project = db.get(models.Project, project_id)
    if project:
        db.delete(project)
        db.commit()
        return True
    return False


def get_Employee(db: Session):
    return db.scalars(select(models.Employee)).all()

def get_Employee_id(db: Session, employee_id: int):
    return db.get(models.Employee, employee_id)

def create_Employee(db: Session, data: schemas.EmployeeCreate):
    employee = models.Employee(**data.model_dump())
    db.add(employee)
    db.commit()
    db.refresh(employee)
    return employee


def update_employee(db: Session, employee_id: int, employee_data: schemas.EmployeeUpdate):
    data = employee_data.model_dump(exclude_unset=True)
    employee = db.get(models.Employee, employee_id)
    if employee:
        for key, value in data.items():
            setattr(employee, key, value)
        db.commit()
        db.refresh(employee)
    return employee



def delete_employee(db: Session, employee_id: int):
    employee = db.get(models.Employee, employee_id)
    if employee:
        db.delete(employee)
        db.commit()
        return True
    return False



def get_Task(db: Session):
    return db.scalars(select(models.Task)).all()

def get_Task_id(db: Session, task_id: int):
    return db.get(models.Task, task_id)

def create_Task(db: Session, data: schemas.TaskCreate):
    task = models.Task(**data.model_dump())
    db.add(task)
    db.commit()
    db.refresh(task)
    return task


def update_task(db: Session, task_id: int, task_data: schemas.TaskUpdate):
    data = task_data.model_dump(exclude_unset=True)
    task = db.get(models.Task, task_id)
    if task:
        for key, value in data.items():
            setattr(task, key, value)
        db.commit()
        db.refresh(task)
    return task


def delete_task(db: Session, task_id: int):
    task = db.get(models.Task, task_id)
    if task:
        db.delete(task)
        db.commit()
        return True
    return False


def assign_task(db: Session, task_id: int, employee_id: int | None):
    task = db.get(models.Task, task_id)
    if task:
        task.employee_id = employee_id
        db.commit()
        db.refresh(task)
    return task


def update_task_status(db: Session, task_id: int, status: str):
    task = db.get(models.Task, task_id)
    if task:
        task.status = status
        db.commit()
        db.refresh(task)
    return task
