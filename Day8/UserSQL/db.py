import sqlite3
from user import User
 
class Database:
    def __init__(self, db_name='my_database1.db'):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.initialize_db()
 
    def initialize_db(self):
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL
        )
        ''')
        self.connection.commit()
 
    def adduser(self, user_obj):
        query = 'INSERT INTO users (name, age) VALUES (?, ?)'
        self.cursor.execute(query, (user_obj.name, user_obj.age))
        self.connection.commit()
        return True
 
    def getallusers(self):
        self.cursor.execute('SELECT * FROM users')
        rows = self.cursor.fetchall()
        return [User(row[1], row[2]) for row in rows]
 
    def cleanup(self):
        self.cursor.close()
        self.connection.close()
        return True


