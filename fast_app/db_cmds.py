


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