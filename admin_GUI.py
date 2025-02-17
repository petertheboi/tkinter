import tkinter as tk
from tkinter import messagebox, ttk
import sqlite3
from GenerateSaleReport import generate_sales_report, generate_stock_report
from ProductManagement import add_product, update_product, remove_product, fetch_products
from SetDatabase import create_db
from SaleProcessing import process_sale
from UserManagement import update_info

# Create the root window
class admin_GUI:
    def __init__(self,root):
        self.root = root
        self.root.title("Admin System")
        self.root.geometry("600x400")
        create_db()
        self.the_menu()
    def the_menu(self):
        self.menu_bar = tk.Menu(self.root)
        self.root.config(menu=self.menu_bar)
        
        """self.bg_image = tk.PhotoImage(file="d:/advance programing/POS/image/bgr_image.png")
        self.background_label = tk.Label(self.root, image=self.bg_image)
        self.background_label.place(relwidth=1, relheight=1)"""
        # Add Product Menu
        self.product_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Product", menu=self.product_menu)
        self.product_menu.add_command(label="Add Product", command=self.add_product_gui)
        self.product_menu.add_command(label="Remove Product", command=self.remove_product_gui)
        self.product_menu.add_command(label="Update Product", command=self.update_product_gui)

        #Staff Info Manangement Menu
        self.staff_info_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Update Staff Infomation", menu=self.staff_info_menu)
        self.staff_info_menu.add_command(label="Change Staff Information", command= self.update_staff_info)
        
        # Sale Menu
        self.sale_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Sale", menu=self.sale_menu)
        self.sale_menu.add_command(label="Process Sale", command=self.process_sale_gui)

        # Sales Report Menu
        self.sales_report_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Sale Report", menu=self.sales_report_menu)
        self.sales_report_menu.add_command(label="Generate Sales Report", command=self.show_sales_report)
        
        #Stock Report Menu
        self.stock_report_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Stock Report", menu=self.stock_report_menu)
        self.stock_report_menu.add_command(label="Generate Stock Report", command=self.stock_report_gui)
        

    def add_product_gui(self):
        def add_product_to_db():
            name = self.name_entry.get()
            price = float(self.price_entry.get())
            stock = int(self.stock_entry.get())
            add_product(name, price, stock)
            messagebox.showinfo("Success", "Product added successfully!")
            self.add_product_window.destroy()

        self.add_product_window = tk.Toplevel(self.root)
        self.add_product_window.title("Add Product")
        self.add_product_window.geometry("150x150")
        
        tk.Label(self.add_product_window, text="Product Name:").pack()
        self.name_entry = tk.Entry(self.add_product_window)
        self.name_entry.pack()

        tk.Label(self.add_product_window, text="Price:").pack()
        self.price_entry = tk.Entry(self.add_product_window)
        self.price_entry.pack()

        tk.Label(self.add_product_window, text="Stock:").pack()
        self.stock_entry = tk.Entry(self.add_product_window)
        self.stock_entry.pack()
        
        tk.Button(self.add_product_window, text="Add Product", command=add_product_to_db).pack()
        
    def remove_product_gui(self):
        def remove_product_to_db():
            id = self.product_id_entry.get()
            remove_product(id)
            messagebox.showinfo("Success", "Product removed successfully!")
            self.remove_product_window.destroy()
            
        self.remove_product_window = tk.Toplevel(self.root)
        self.remove_product_window.title("Remove Product")
        self.remove_product_window.geometry("150x100")
        
        tk.Label(self.remove_product_window, text="Enter Product ID:").pack()
        self.product_id_entry = tk.Entry(self.remove_product_window)
        self.product_id_entry.pack()
        
        tk.Button(self.remove_product_window, text="Remove Product", command=remove_product_to_db).pack()
        
    def update_product_gui(self):
        def update_product_to_db():
            name = self.name_entry.get()
            price = float(self.price_entry.get())
            stock = int(self.stock_entry.get())
            id = self.product_id_entry.get()
            update_product(id, name, price, stock)
            messagebox.showinfo("Success", "Product updated successfully!")
            self.update_product_window.destroy()
            
        self.update_product_window = tk.Toplevel(self.root)
        self.update_product_window.title("Update Product")
        self.update_product_window.geometry("150x200")
        
        tk.Label(self.update_product_window, text="Product Name:").pack()
        self.name_entry = tk.Entry(self.update_product_window)
        self.name_entry.pack()

        tk.Label(self.update_product_window, text="Price:").pack()
        self.price_entry = tk.Entry(self.update_product_window)
        self.price_entry.pack()

        tk.Label(self.update_product_window, text="Stock:").pack()
        self.stock_entry = tk.Entry(self.update_product_window)
        self.stock_entry.pack()
        
        tk.Label(self.update_product_window, text="Enter Product ID:").pack()
        self.product_id_entry = tk.Entry(self.update_product_window)
        self.product_id_entry.pack()
        
        tk.Button(self.update_product_window, text="Update Product", command=update_product_to_db).pack(padx=10, pady=10)

    def process_sale_gui(self):
        def process_sale_button():
            product_id = int(self.product_id_entry.get())
            quantity = int(self.quantity_entry.get())
            customer_id = int(self.customer_id_entry.get()) if self.customer_id_entry.get() else None
            result = process_sale(product_id, quantity, customer_id)
            messagebox.showinfo("Sale", result)
            self.sale_window.destroy()

        self.sale_window = tk.Toplevel(self.root)
        self.sale_window.title("Process Sale")

        tk.Label(self.sale_window, text="Product ID:").pack()
        self.product_id_entry = tk.Entry(self.sale_window)
        self.product_id_entry.pack()

        tk.Label(self.sale_window, text="Quantity:").pack()
        self.quantity_entry = tk.Entry(self.sale_window)
        self.quantity_entry.pack()

        tk.Label(self.sale_window, text="Customer ID (optional):").pack()
        self.customer_id_entry = tk.Entry(self.sale_window)
        self.customer_id_entry.pack()

        tk.Button(self.sale_window, text="Process Sale", command=process_sale_button).pack()
    def show_sales_report(self):
        self.report = generate_sales_report()
        self.report_window = tk.Toplevel(self.root)
        self.report_window.title("Sales Report")
        self.report_text = tk.Text(self.report_window, width=80, height=20)
        self.report_text.pack()
        self.report_text.insert(tk.END, self.report)
        
    def stock_report_gui(self):
        self.report = generate_stock_report()
        self.stock_window = tk.Toplevel(self.root)
        self.stock_window.title("Stock Report")
        self.report_stock = tk.Text(self.stock_window, width=80, height=20)
        self.report_stock.pack()
        self.report_stock.insert(tk.END, self.report)
        
    def update_staff_info(self):
        def update_staff_info_to_db():
            name = self.name_entry.get()
            password = self.password_entry.get()
            access = self.admin_access_entry.get()
            id = self.staff_id_entry.get()
            update_info(name, password, access, id)
            messagebox.showinfo("Success", "Information updated successfully!")
            self.update_staff_window.destroy()
        self.update_staff_window = tk.Toplevel(self.root)
        self.update_staff_window.title("Update Product")
        self.update_staff_window.geometry("150x200")
        
        tk.Label(self.update_staff_window, text="Name:").pack()
        self.name_entry = tk.Entry(self.update_staff_window)
        self.name_entry.pack()

        tk.Label(self.update_staff_window, text="Password:").pack()
        self.password_entry = tk.Entry(self.update_staff_window)
        self.password_entry.pack()
        
        tk.Label(self.update_staff_window, text="Admin Command:").pack()
        self.admin_access_entry = tk.Entry(self.update_staff_window)
        self.admin_access_entry.insert(0, "1 for yes and 0 for no")
        self.admin_access_entry.pack()
        
        tk.Label(self.update_staff_window, text="Enter The Staff ID:").pack()
        self.staff_id_entry = tk.Entry(self.update_staff_window)
        self.staff_id_entry.pack()
        
        tk.Button(self.update_staff_window, text="Update Information", command=update_staff_info_to_db).pack(padx=10, pady=10)
if __name__ == "__main__":
    root = tk.Tk()
    app = admin_GUI(root)
    root.mainloop()     




