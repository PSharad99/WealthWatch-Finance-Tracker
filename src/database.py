import sqlite3

def init_db():
    with sqlite3.connect("wealth.db") as conn:
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS expenses 
                          (id INTEGER PRIMARY KEY, 
                           category TEXT, 
                           amount REAL, 
                           date TEXT)''')
        conn.commit()

def add_expense(category, amount):
    with sqlite3.connect("wealth.db") as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO expenses (category, amount, date) VALUES (?, ?, DATE('now'))", 
                       (category, amount))
        conn.commit()