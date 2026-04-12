from database import conn, cursor
from src.schemes.models import CategoryModal


def create_category(category: CategoryModal, id_user: int):
    cursor.execute("""
        INSERT INTO CATEGORIES (name, color, id_user) 
            VALUES (?, ?, ?)
    """, [category.name, category.color, id_user])
    conn.commit()

    return "Category created !"


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


def delete_category(cat_name: str):
    cursor.execute("""
        DELETE FROM CATEGORIES
            WHERE name = ?
    """, [cat_name])
    conn.commit()

    return "Category deleted !"


