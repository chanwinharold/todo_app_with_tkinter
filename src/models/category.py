from database import conn, cursor
from src.schemes.models import CategoryModal


def create_category(category: CategoryModal, id_user: int):
    cursor.execute("""
        INSERT INTO CATEGORIES (name, color, id_user) 
            VALUES (?, ?, ?)
    """, [category.name, category.color, id_user])
    conn.commit()

    cursor.execute("SELECT last_insert_rowid()")
    cat_id = cursor.fetchone()[0]

    cursor.execute("SELECT * FROM CATEGORIES WHERE id_cat = ?", [cat_id])
    result = cursor.fetchone()
    return result


def get_categories(id_user: int):
    cursor.execute("""
        SELECT *
        FROM CATEGORIES
        WHERE id_user = ?
    """, [id_user])

    return cursor.fetchall()


def update_category(category: CategoryModal):
    cursor.execute("""
        UPDATE CATEGORIES
        SET 
            name = ?,
            color = ?
        WHERE id_cat = ?
    """, [category.name, category.color, category.id_cat])
    conn.commit()

    return "Category updated !"


def delete_category(cat_id: int):
    cursor.execute("""
        DELETE FROM TODOS
        WHERE id_cat = ?
    """, [cat_id])
    cursor.execute("""
        DELETE FROM CATEGORIES
        WHERE id_cat = ?
    """, [cat_id])
    conn.commit()

    return "Category deleted !"


