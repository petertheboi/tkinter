from admin_GUI import admin_GUI
from staff_gui import POS_GUI
from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
import tkinter as tk
import sqlite3
from SetDatabase import create_db
from UserManagement import new_user, fetch_user

class login_gui:
    def __init__(self, root):
        self.root = root
        self.root.title("Login Gui")
        create_db()
        self.widget_creation()
    def widget_creation(self):
        def register():
            name = self.username_entry.get()
            password = self.password_entry.get()
            admin = False
            
            if name == "" and password == "":
                self.username_entry.delete(0, END)
                self.password_entry.delete(0, END)
                messagebox.showerror("Incorrect", "Please Enter Something")
            else:
                new_user(name, password, admin)
                self.username_entry.delete(0, END)
                self.password_entry.delete(0, END)
                messagebox.showinfo("Successful","You have successfully register!")
            
        self.frame = tk.LabelFrame(root, text = "Login", padx=20, pady=20)
        self.frame.pack(padx=10, pady=10)       
        
        self.username_label = tk.Label(self.frame, text = "Username")
        self.username_entry = tk.Entry(self.frame)
        
        self.password_label = tk.Label(self.frame, text = "Password")
        self.password_entry = tk.Entry(self.frame, show = "*")
        
        self.login_button = tk.Button(self.frame, text = "Login", command= self.login_process)
        self.register_button = tk.Button(self.frame, text= "Register", command=register )
        
        self.username_label.grid(row = 0, column = 0, padx= 10, pady= 10)
        self.username_entry.grid(row = 0, column = 1)
        self.password_label.grid(row = 1, column = 0, padx= 10, pady= 10)
        self.password_entry.grid(row = 1, column = 1)
        self.login_button.grid(row = 2, column = 0, padx= 5, pady= 5)
        self.register_button.grid(row = 2, column = 1, padx= (25, 0), pady= 5)
        
    def login_process(self):
        self.users = fetch_user()
        self.current_user = self.username_entry.get()
        
        for user in self.users:
            if user[1] == self.current_user:
                if self.password_entry.get() != user[2]:
                    messagebox.showerror("Incorrect", "Please Enter The Password Again!")
                else: 
                    if user[3] == 1:
                        self.username_entry.delete(0, END)
                        self.password_entry.delete(0, END)
                        admin_root = tk.Tk()
                        self.admin = admin_GUI(admin_root)
                        admin_root.mainloop()
                    else:
                        self.username_entry.delete(0, END)
                        self.password_entry.delete(0, END)
                        staff_root = tk.Tk()
                        self.staff = POS_GUI(staff_root)
                        staff_root.mainloop()
        
if __name__ == "__main__":
    root = tk.Tk()
    login_interface = login_gui(root)
    root.mainloop()
