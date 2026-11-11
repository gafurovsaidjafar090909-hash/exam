from datetime import date, datetime
from typing import Literal
from pydantic import BaseModel,ConfigDict,Field


class ProjectBase(BaseModel):
    name : str = Field(min_length=1,max_length=100)
    desciption : str | None = None

class ProjectCreate(ProjectBase):
    pass


class ProjectUpdate(BaseModel):
    name: str | None = Field(default=None, min_length=1,max_length=100)
    desciption : str | None = None

class ProjectResponse(ProjectBase):
    id : int
    model_config = ConfigDict(from_attributes=True)





class EmployeeBase(BaseModel):
    full_name : str = Field(min_length=1,max_length=150)
    email : str | None = None
    pasition : str | None = None
    is_active : bool = True


class EmployeeCreate(EmployeeBase):
    pass


class EmployeeUpdate(BaseModel):
    full_name : str | None = Field(default=None, min_length=1,max_length=150)
    email : str | None = None
    pasition : str | None = None
    is_active : bool | None = None


class EmployeeResponse(EmployeeBase):
    id : int
    model_config = ConfigDict(from_attributes=True)





class TaskBase(BaseModel):
    title : str = Field(min_length=1,max_length=200)
    desciption : str | None = None
    status : Literal["todo", "in_progress", "done"] = "todo"
    priority : int | None = Field(default=None, ge=1, le=5)
    deadline : date | None = None
    project_id : int
    employee_id : int | None = None


class TaskCreate(TaskBase):
    pass


class TaskUpdate(BaseModel):
    title : str | None = Field(default=None, min_length=1,max_length=200)
    desciption : str | None = None
    status : Literal["todo", "in_progress", "done"] | None = None
    priority : int | None = Field(default=None, ge=1, le=5)
    deadline : date | None = None
    project_id : int | None = None
    employee_id : int | None = None


class TaskResponse(TaskBase):
    id : int
    create_at : datetime
    model_config = ConfigDict(from_attributes=True)


class TaskAssign(BaseModel):
    employee_id : int | None = None


class TaskStatusUpdate(BaseModel):
    status : Literal["todo", "in_progress", "done"]
