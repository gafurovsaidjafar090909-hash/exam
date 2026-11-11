from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud
from ..database import get_db
from ..schemas import EmployeeCreate, EmployeeUpdate, EmployeeResponse


router = APIRouter(prefix="/employee", tags=["employee"])
DB = Annotated[Session, Depends(get_db)]


@router.get("/", response_model=list[EmployeeResponse])
async def get_employees(db: DB):
    return crud.get_Employee(db)


@router.get("/{employee_id}", response_model=EmployeeResponse)
async def get_employee_by_id(employee_id: int, db: DB):
    employee = crud.get_Employee_id(db, employee_id)
    if employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return employee


@router.post("/", response_model=EmployeeResponse, status_code=201)
async def create_employee(data: EmployeeCreate, db: DB):
    return crud.create_Employee(db, data)


@router.put("/{employee_id}", response_model=EmployeeResponse)
async def update_employee(employee_id: int, data: EmployeeUpdate, db: DB):
    employee = crud.update_employee(db, employee_id, data)
    if employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return employee


@router.delete("/{employee_id}")
async def delete_employee(employee_id: int, db: DB):
    if not crud.delete_employee(db, employee_id):
        raise HTTPException(status_code=404, detail="Employee not found")
    return {"detail": "Deleted successfully"}
