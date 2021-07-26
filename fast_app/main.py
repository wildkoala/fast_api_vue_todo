from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import Optional
from . import crud, models, schemas
from .database import engine, SessionLocal

models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


app = FastAPI()

# Get a specific todo
@app.get("/todo/{todo_id}")
def get_todos(todo_id: int, db: Session = Depends(get_db)):
    return crud.get_todo_by_id(db=db, todo_id=todo_id)

# Get all todos
@app.get("/todos/")
def get_todos(db: Session = Depends(get_db)):
    return crud.get_todos(db=db)

# Create a new todo
@app.post("/create/")
def create_todo(
    new_todo: schemas.TodoCreate,
    db: Session = Depends(get_db)
    ):
    return crud.create_todo_item(db=db, new_todo=new_todo)

# Update an existing todo
@app.put("/update/{todo_id}")
def update_todo(todo_id: int, 
                new_title: Optional[str] = None, 
                new_is_complete: Optional[bool] = None,
                db: Session = Depends(get_db)
                ):
    if new_title == None and new_is_complete == None:
        raise HTTPException(status_code=400, detail="Must provide new title or is_complete value")
    return crud.update_todo(db=db, todo_id=todo_id, new_title=new_title, new_is_complete=new_is_complete)

# Delete a todo
@app.delete("/delete/{todo_id}")
def delete_todo(todo_id: int, 
                db: Session = Depends(get_db)
                ):
    return crud.delete_todo(db=db, todo_id=todo_id)
