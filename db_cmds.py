from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql.sqltypes import Boolean

#SQLALCHEMY_DATABASE_URL = "postgresql://<username>:<password>@<ip/domain_name>:<port>/<database_name>"
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:mysecretpassword@localhost:5432/db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

base = declarative_base()

class Todo(base):  
    __tablename__ = 'todos'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String)
    is_complete = Column(Boolean)

    def as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}

Session = sessionmaker(engine)  
session = Session()

base.metadata.create_all(engine)

# Create
def create_todo(title):
    new_todo = Todo(title = title, is_complete = False)  
    session.add(new_todo)  
    session.commit()

# Read
def read_todos():
    todos = session.query(Todo)
    to_return = []
    for todo in todos:  
        to_return.append(todo.as_dict())
    return to_return
    
# Update
def update_todo(title, new_title = None, new_is_complete = None):
    if new_is_complete == None and new_title == None:
        return

    todos = session.query(Todo).filter(Todo.title == title)
    for todo in todos:  
        if new_title != None:
            todo.title = new_title
        if new_is_complete != None:
            todo.is_complete = new_is_complete
        session.commit()

# Delete
def delete_todo(title):
    todos = session.query(Todo).filter(Todo.title == title)
    for todo in todos:  
        session.delete(todo)  
        session.commit() 

# Delete all
def clear_todos():
    todos = session.query(Todo)
    for todo in todos:  
        session.delete(todo)  
        session.commit() 