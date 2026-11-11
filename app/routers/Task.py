from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud
from ..database import get_db
from ..schemas import TaskCreate, TaskUpdate, TaskResponse, TaskAssign, TaskStatusUpdate


router = APIRouter(prefix="/task", tags=["task"])
DB = Annotated[Session, Depends(get_db)]


def check_relations(db: Session, project_id: int | None, employee_id: int | None):
    if project_id is not None and crud.get_Project_id(db, project_id) is None:
        raise HTTPException(status_code=404, detail="Project not found")
    if employee_id is not None and crud.get_Employee_id(db, employee_id) is None:
        raise HTTPException(status_code=404, detail="Employee not found")


@router.get("/", response_model=list[TaskResponse])
async def get_tasks(db: DB):
    return crud.get_Task(db)


@router.get("/{task_id}", response_model=TaskResponse)
async def get_task_by_id(task_id: int, db: DB):
    task = crud.get_Task_id(db, task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@router.post("/", response_model=TaskResponse, status_code=201)
async def create_task(data: TaskCreate, db: DB):
    check_relations(db, data.project_id, data.employee_id)
    return crud.create_Task(db, data)


@router.put("/{task_id}", response_model=TaskResponse)
async def update_task(task_id: int, data: TaskUpdate, db: DB):
    for field in ("title", "status", "project_id"):
        if field in data.model_fields_set and getattr(data, field) is None:
            raise HTTPException(status_code=422, detail=f"{field} cannot be null")
    check_relations(db, data.project_id, data.employee_id)
    task = crud.update_task(db, task_id, data)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@router.patch("/{task_id}/assign", response_model=TaskResponse)
async def assign_task(task_id: int, data: TaskAssign, db: DB):
    if data.employee_id is not None:
        employee = crud.get_Employee_id(db, data.employee_id)
        if employee is None:
            raise HTTPException(status_code=404, detail="Employee not found")
        if not employee.is_active:
            raise HTTPException(status_code=400, detail="Employee is not active")
    task = crud.assign_task(db, task_id, data.employee_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@router.patch("/{task_id}/status", response_model=TaskResponse)
async def update_task_status(task_id: int, data: TaskStatusUpdate, db: DB):
    task = crud.update_task_status(db, task_id, data.status)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@router.delete("/{task_id}")
async def delete_task(task_id: int, db: DB):
    if not crud.delete_task(db, task_id):
        raise HTTPException(status_code=404, detail="Task not found")
    return {"detail": "Deleted successfully"}
