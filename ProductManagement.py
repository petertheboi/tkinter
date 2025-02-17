import sqlite3

def add_product(name, price, stock):
    conn = sqlite3.connect('pos_system.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO products (name, price, stock) VALUES (?, ?, ?)", (name, price, stock))
    conn.commit()
    conn.close()

def update_product(id, name, price, stock):
    conn = sqlite3.connect('pos_system.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE products SET name = ?, price = ?, stock = ? WHERE id = ?", (name, price, stock, id))
    cursor.execute("SELECT * FROM products")
    conn.commit()
    conn.close()

def remove_product(id):
    conn = sqlite3.connect('pos_system.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM products WHERE id = ?", (id,))
    conn.commit()
    conn.close()

def fetch_products():
    conn = sqlite3.connect('pos_system.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()
    conn.close()
    return products
