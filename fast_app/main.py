from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from . import crud, models
from .database import engine, SessionLocal

models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create the FastAPI
app = FastAPI()

@app.post("/create/", response_model=Todo)
def create_todo(
    id: int,
    title: str, 
    is_complete: bool, 
    db: Session = Depends(get_db)
    ):
    return crud.create_todo_item(db=db, id=id, title=title, is_complete=is_complete)