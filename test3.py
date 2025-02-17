import sqlite3
from tkinter import *
from tkinter import messagebox, ttk
import tkinter as tk
from SetDatabase import create_db
from UserManagement import fetch_user, remove_user
from SaleProcessing import process_item
"""s_root = tk.Tk()
app = POS_GUI(s_root)
s_root.mainloop()"""
"""def removing_stuff():
    id = entry.get()
    remove_user(id)
    entry.delete(0, END)
    messagebox.showinfo("Yes", "My Man!")
    
root = tk.Tk()
root.title("Testing")
entry = tk.Entry(root)
entry.grid(row= 0, column=0)
btn = Button(root, text = "Press Me", command=removing_stuff)
btn.grid(row=0, column=1)
bth2 = Button(root, text = "Press Me", command=fetch_user)
bth2.grid(row= 1, column=0)
root.mainloop()"""
"""conn = sqlite3.connect('pos_system.db')
cursor = conn.cursor()
cursor.execute("UPDATE users SET name = ?, password = ?, admin = ? Where id = ?", ("Ada1","pass1", 1, 1))
cursor.execute("SELECT * FROM users")
conn.commit()
conn.close()"""
create_db()
"""id = int(3)
conn = sqlite3.connect('pos_system.db')
cursor = conn.cursor()
cursor.execute("SELECT * FROM cart_item")
products = cursor.fetchall()
for i in products :
    print (i[4])
conn.close()"""
conn = sqlite3.connect('pos_system.db')
cursor = conn.cursor()
cursor.execute("SELECT * FROM users")
users = cursor.fetchall()
print (users)