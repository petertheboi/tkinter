import sqlite3


def new_user(name, password, admin):
    conn = sqlite3.connect('pos_system.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (name, password, admin) VALUES (?, ?, ?)", (name, password, admin))
    conn.commit()
    conn.close()

def fetch_user():
    conn = sqlite3.connect('pos_system.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    conn.close()
    print (users)
    return users

def remove_user(id):
    conn = sqlite3.connect('pos_system.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE id = ?", (id,))
    conn.commit()
    conn.close()

def update_info(name, password, admin, id):
    conn = sqlite3.connect('pos_system.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET name = ?, password = ?, admin = ? WHERE id = ?", (name, password, admin, id))
    cursor.execute("SELECT * FROM products")
    conn.commit()
    conn.close()
