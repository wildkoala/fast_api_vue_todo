from sqlalchemy import Boolean, Column, Integer, String
from .database import Base

class Todo(Base):  
    __tablename__ = 'todos'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String)
    is_complete = Column(Boolean, default=False)