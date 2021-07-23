from typing import Optional
from fastapi import FastAPI

import db_cmds

# Create the FastAPI
app = FastAPI()

@app.get("/")
def get_todos():
    todos = db_cmds.read_todos()
    return todos


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

