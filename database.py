import sqlite3 as sql
from sqlite3 import Connection, Cursor


class Database:
    def __init__(self, db_path: str):
        self.db_path = db_path
        self.conn = None
        self.cursor = None

    def connect(self) -> tuple[Connection, Cursor] | None:
        try:
            self.conn = sql.connect(self.db_path)
            self.cursor = self.conn.cursor()
            res = self.cursor.execute("SELECT 1")
            res.fetchone()

            print("✅ Database connected successfully !")
            return self.conn, self.cursor
        except Exception as error:
            print(f"❌ Database connection failed. \nError : {error}")


db = Database("todo_db.db")
db.connect()

conn: Connection = db.conn
cursor: Cursor = db.cursor

