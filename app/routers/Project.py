from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud
from ..database import get_db
from ..schemas import ProjectCreate, ProjectUpdate, ProjectResponse


router = APIRouter(prefix="/project", tags=["project"])
DB = Annotated[Session, Depends(get_db)]


@router.get("/", response_model=list[ProjectResponse])
async def get_projects(db: DB):
    return crud.get_Project(db)


@router.get("/{project_id}", response_model=ProjectResponse)
async def get_project_by_id(project_id: int, db: DB):
    project = crud.get_Project_id(db, project_id)
    if project is None:
        raise HTTPException(status_code=404, detail="Project not found")
    return project


@router.post("/", response_model=ProjectResponse, status_code=201)
async def create_project(data: ProjectCreate, db: DB):
    return crud.create_Project(db, data)


@router.put("/{project_id}", response_model=ProjectResponse)
async def update_project(project_id: int, data: ProjectUpdate, db: DB):
    project = crud.update_project(db, project_id, data)
    if project is None:
        raise HTTPException(status_code=404, detail="Project not found")
    return project


@router.delete("/{project_id}")
async def delete_project(project_id: int, db: DB):
    if not crud.delete_project(db, project_id):
        raise HTTPException(status_code=404, detail="Project not found")
    return {"detail": "Deleted successfully"}
