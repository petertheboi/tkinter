import sqlite3

def create_db():
    conn = sqlite3.connect('pos_system.db')
    cursor = conn.cursor()

    # Create products, customers, and sales tables
    cursor.execute('''CREATE TABLE IF NOT EXISTS products (
                        id INTEGER PRIMARY KEY,
                        name TEXT,
                        price REAL,
                        stock INTEGER)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY,
                        name TEXT,
                        password TEXT,
                        admin BOOLEAN)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS sales (
                        id INTEGER PRIMARY KEY,
                        product_id INTEGER,
                        quantity INTEGER,
                        total REAL,
                        date TEXT,
                        customer_id INTEGER,
                        FOREIGN KEY (product_id) REFERENCES products(id),
                        FOREIGN KEY (customer_id) REFERENCES users(id))''')
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS cart_item (
                        product_id INTEGER,
                        product_name TEXT,
                        quantity INTEGER,
                        date TEXT,
                        total REAL,
                        new_stock INTEGER,
                        FOREIGN KEY (product_id) REFERENCES products(id)
    )''')
    conn.commit()
    conn.close()

# Create the database when the program starts
create_db()
