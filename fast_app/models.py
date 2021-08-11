from sqlalchemy import Boolean, Column, Integer, String
import database

class Todo(database.Base):  
    __tablename__ = 'todos'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    is_complete = Column(Boolean, default=False)