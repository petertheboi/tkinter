import sqlite3
from tkinter import *
import tkinter as tk
from ProductManagement import fetch_products

def generate_sales_report():
    conn = sqlite3.connect('pos_system.db')
    cursor = conn.cursor()
    
    # Get sales data
    cursor.execute('''SELECT sales.id, products.name, sales.quantity, sales.total, sales.date, customers.name 
                      FROM sales
                      JOIN products ON sales.product_id = products.id
                      LEFT JOIN customers ON sales.customer_id = customers.id''')
    sales = cursor.fetchall()
    # Format the report
    report = "Sales Report\n"
    report += "ID | Product | Quantity | Total | Date | Customer\n"
    report += "-" * 60 + "\n"
    for sale in sales:
        report += f"{sale[0]} | {sale[1]} | {sale[2]} | {sale[3]:.2f} | {sale[4]} | {sale[5] if sale[5] else 'N/A'}\n"

    conn.close()
    return report

def generate_stock_report():
    stock = fetch_products()
    report = "Stock Report\n"
    report += "ID | Product | Price | Stock \n"
    report += "-" * 60 + "\n"
    for item in stock:
        report += f"{item[0]} | {item[1]} | {item[2]} | {item[3]}\n"
    return report

def generate_product_list():
    stock = fetch_products()
    report = "ID | Product | Price \n"
    report += "-" * 20 + "\n"
    for item in stock:
        report += f"{item[0]} | {item[1]} | {item[2]}\n"
    return report

def add_item_to_frame(id):
    conn = sqlite3.connect('pos_system.db')
    cursor = conn.cursor()
    cursor.execute("SELECT product_name, quantity, total FROM cart_item where product_id = ?", (id,))
    item = cursor.fetchone()
    print (item)
    report = ""
    report += f"- {item[0]}\tx\t{item[1]}\t ${item[2]}\n"
    conn.close()
    return report
    
    
    