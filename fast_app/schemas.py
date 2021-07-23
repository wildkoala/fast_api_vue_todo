from fast_app.database import Base
from typing import Optional
from pydantic import BaseModel


class TodoCreate(BaseModel):
    title: str

class TodoRD(BaseModel):
    id: int

class TodoUpdate(BaseModel):
    id: int
    new_title: Optional[str]
    new_is_complete: Optional[bool]

class Todo(BaseModel):
    id: int
    title: str
    is_complete: bool