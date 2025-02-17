import sqlite3
from datetime import datetime
from SetDatabase import create_db

def process_sale_admin(product_id, quantity, customer_id=None):
    conn = sqlite3.connect('pos_system.db')
    cursor = conn.cursor()

    # Check stock and price of the product
    cursor.execute("SELECT price, stock FROM products WHERE id = ?", (product_id,))
    product = cursor.fetchone()

    if product and product[1] >= quantity:
        total = product[0] * quantity
        new_stock = product[1] - quantity
        cursor.execute("UPDATE products SET stock = ? WHERE id = ?", (new_stock, product_id))

        # Insert sale into sales table
        cursor.execute("INSERT INTO sales (product_id, quantity, total, date, customer_id) VALUES (?, ?, ?, ?, ?)",
                       (product_id, quantity, total, datetime.now().strftime("%Y-%m-%d %H:%M:%S"), customer_id))
        
        conn.commit()
        conn.close()
        return f"Sale successful! Total: ${total:.2f}"
    else:
        conn.close()
        return "Error: Not enough stock or product does not exist."

def process_item(product_id, quantity):
    create_db()
    conn = sqlite3.connect('pos_system.db')
    cursor = conn.cursor()
    cursor.execute("SELECT name, price, stock FROM products WHERE id = ?", (product_id,))
    product = cursor.fetchone()
    
    if product and product[2] >= quantity:
        total = product[1] * quantity
        new_stock = product[2] - quantity
        product_name = product[0]
        print (product[0], product[1], product[2])
        cursor.execute("INSERT INTO cart_item (product_id, product_name, quantity, date, total, new_stock) VALUES (?, ?, ?, ?, ?, ?)",
                       (product_id, product_name, quantity, datetime.now().strftime("%Y-%m-%d %H:%M:%S"), total, new_stock))
        conn.commit()
        conn.close()
    else:
        conn.close()
        return "Error: Not enough stock or product does not exist"

def process_sale():
    conn = sqlite3.connect('pos_system.db')
    cursor = conn.cursor()
    total = 0
    
    cursor.execute("SELECT * FROM cart_item")
    product = cursor.fetchall()
    for info in product:
        total += info[4]
        cursor.execute("UPDATE products SET stock = ? WHERE id = ?", (info[5], info[0]))
        cursor.execute("INSERT INTO sales (product_id, quantity, total, date, customer_id) VALUES (?, ?, ?, ?, ?) ",
                   (info[0], info[2], info[4], info[3], None))
        conn.commit()
    total_label = f"Total:\t\t ${round(total, 2)}"
    return total_label
    
def clear_data():
    create_db()
    conn = sqlite3.connect('pos_system.db')
    cursor = conn.cursor()
    
    cursor.execute("DELETE FROM cart_item")
    conn.commit()
    
    cursor.execute("SELECT * FROM cart_item")
    blank = cursor.fetchall()
    print (blank)
    conn.close()
    return blank
