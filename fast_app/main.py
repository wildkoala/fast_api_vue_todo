from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

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

@app.post("/todos/")
def get_todos(

    db: Session = Depends(get_db)
    ):
    return crud.create_todo_item(db=db, new_todo=new_todo)

@app.post("/create/")
def create_todo(
    new_todo: schemas.TodoCreate,
    db: Session = Depends(get_db)
    ):
    return crud.create_todo_item(db=db, new_todo=new_todo)