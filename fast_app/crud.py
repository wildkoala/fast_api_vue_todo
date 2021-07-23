from fast_app import schemas
from sqlalchemy.orm import Session
from . import models

def get_todo_item(db: Session, id: int):
    return db.query(models.Todo).filter(models.Todo.id == id).first()

def create_todo_item(db: Session, new_todo: schemas.TodoBase):
    new_todo = models.Todo(title=new_todo.title, is_complete=new_todo.is_complete)
    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)
    return new_todo
