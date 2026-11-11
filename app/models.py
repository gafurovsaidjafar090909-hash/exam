from datetime import date, datetime
from sqlalchemy import String, ForeignKey, Text, DateTime, Boolean, Date
from sqlalchemy.orm import Mapped, mapped_column
from .database import Base


class Project(Base):
    __tablename__ = 'project'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(150), unique=True)
    desciption: Mapped[str | None] = mapped_column(Text)
    create_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)


class Employee(Base):
    __tablename__ = "employee"
    id: Mapped[int] = mapped_column(primary_key=True)
    full_name: Mapped[str] = mapped_column(String(150))
    email: Mapped[str | None] = mapped_column(String(150))
    pasition: Mapped[str | None] = mapped_column(String(100))
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    create_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)


class Task(Base):
    __tablename__ = 'task'
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(200))
    desciption: Mapped[str | None] = mapped_column(Text)
    status: Mapped[str] = mapped_column(String(20), default='todo')
    priority: Mapped[int | None] = mapped_column()
    deadline: Mapped[date | None] = mapped_column(Date)
    create_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    project_id: Mapped[int] = mapped_column(ForeignKey("project.id"))
    employee_id: Mapped[int | None] = mapped_column(ForeignKey("employee.id"))
