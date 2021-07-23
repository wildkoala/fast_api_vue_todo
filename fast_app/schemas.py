from pydantic import BaseModel


class TodoBase(BaseModel):
    title: str
    in_complete: bool

class Todo(TodoBase):
    id: int

    class Config:
        orm_mode = True