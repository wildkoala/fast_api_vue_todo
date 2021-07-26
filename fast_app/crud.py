from sqlalchemy.orm import Session
from . import models, schemas

def get_todo_by_id(db: Session, todo_id: int):
    return db.query(models.Todo).filter(models.Todo.id == todo_id).first()

def get_todos(db: Session):
    return db.query(models.Todo).all()

def create_todo_item(db: Session, new_todo: schemas.TodoCreate):
    add_to_db = models.Todo(title=new_todo.title)
    db.add(add_to_db)
    db.commit()
    db.refresh(add_to_db)
    return add_to_db

def update_todo(db: Session, todo_id: int, new_title: str, new_is_complete: bool):
    if new_title == None and new_is_complete == None:
        # Return some kind of error
        return -1 
    
    to_update = db.query(models.Todo).filter(models.Todo.id == todo_id).first()
    if new_title:
        to_update.title = new_title
    if new_is_complete:
        to_update.is_complete = new_is_complete

    db.commit()
    db.refresh(to_update)
    return to_update

def delete_todo(db: Session, todo_id: int):
    to_delete = db.query(models.Todo).filter(models.Todo.id == todo_id).delete()
    db.commit()
    return {'Deleted' : todo_id}
