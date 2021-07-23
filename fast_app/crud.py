from sqlalchemy.orm import Session
from . import models, schemas

def get_todo_item(db: Session, todo_id: int):
    return db.query(models.Todo).filter(models.Todo.id == todo_id).first()

def create_todo_item(db: Session, new_todo: schemas.TodoCreate):
    add_to_db = models.Todo(title=new_todo.title)
    db.add(add_to_db)
    db.commit()
    db.refresh(add_to_db)
    return add_to_db
