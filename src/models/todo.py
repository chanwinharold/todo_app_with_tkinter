from database import conn, cursor
from src.schemes.models import TodoModel

def create_todo(todo: TodoModel, id_cat: int):
    cursor.execute("""
        INSERT INTO TODOS (title, description, id_cat) 
            VALUES (?, ?, ?)
    """, [todo.title, todo.description, id_cat])
    conn.commit()

    cursor.execute("SELECT last_insert_rowid()")
    todo_id = cursor.fetchone()[0]

    cursor.execute("SELECT * FROM TODOS WHERE id_todo = ?", [todo_id])
    result = cursor.fetchone()
    return result

def get_all_todos(id_cat: int):
    cursor.execute("""
        SELECT *
        FROM TODOS
        WHERE id_cat = ?
    """, [id_cat])

    return cursor.fetchall()

def get_one_todo(id_todo: int):
    cursor.execute("""
        SELECT *
        FROM TODOS
        WHERE id_todo = ?
    """, [id_todo])

    return cursor.fetchone()

def update_todo(todo: TodoModel):
    cursor.execute("""
        UPDATE TODOS
        SET 
            title = ?,
            description = ?
        WHERE id_todo = ?
    """, [todo.title, todo.description, todo.id_todo])
    conn.commit()

    return "Todo updated !"


def delete_todo(id_todo: int):
    cursor.execute("""
        DELETE FROM TODOS
            WHERE id_todo = ?
    """, [id_todo])
    conn.commit()

    return "Todo deleted !"


def toggle_todo(id_todo: int, state: bool):
    cursor.execute("""
        UPDATE TODOS
        SET done = ?
        WHERE id_todo = ?
    """, [state, id_todo])
    conn.commit()

    return "Done !"

