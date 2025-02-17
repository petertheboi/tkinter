import tkinter as tk
from tkinter import messagebox, ttk
from tkinter import *
import sqlite3
from GenerateSaleReport import generate_sales_report, generate_product_list, add_item_to_frame
from SetDatabase import create_db
from SaleProcessing import process_sale, process_item, clear_data

class POS_GUI:
    def __init__(self, root):
        self.root = root
        self.root.title("POS System")
        self.root.geometry("600x400")
        create_db()
        self.widget_creation()
        
    def widget_creation(self):
        def Product_List_gui():
            report = generate_product_list()
            product_label = tk.Label(self.product_list_frame, text = report).pack()
            
        def new_blank_frame():
            blank = clear_data()
            self.frame.destroy()
            self.frame = tk.LabelFrame(self.root, text= "Order Summary")
            self.frame.grid(row= 0, column= 1, padx=10, pady=10)
            temp_label = tk.Label(self.frame, text=blank).pack
        
        def sale_process():
            total = process_sale()
            temp_label = tk.Label(self.frame, text= total).pack()
        
        self.add_product_button = tk.Button(self.root, text = "Add Product", command=self.process_item_gui)
        self.add_product_button.grid(row=0, column=2)
        
        self.product_list_frame = tk.LabelFrame(self.root, text= "Product List")
        self.product_list_frame.grid(row=0, column=0, padx=10, pady=10)
        Product_List_gui()
        
        self.clear_button = tk.Button(self.root, text = "Clear Items", command=new_blank_frame)
        self.clear_button.grid(row= 1, column=1)
        
        self.process_button = tk.Button(self.root, text= "Process Sales", command= sale_process)
        self.process_button.grid(row=1, column=2, padx=10, pady=10)
        
    def process_item_gui(self):
        def process_sale_button():
            product_id = int(self.product_id_entry.get())
            quantity = int(self.quantity_entry.get())
            process_item(product_id, quantity)
            item = add_item_to_frame(product_id)
            frame_label = tk.Label(self.frame, text= item).pack()
            self.sale_window.destroy()

        self.sale_window = tk.Toplevel(self.root)
        self.sale_window.title("Process Sale")

        tk.Label(self.sale_window, text="Product ID:").pack()
        self.product_id_entry = tk.Entry(self.sale_window)
        self.product_id_entry.pack()

        tk.Label(self.sale_window, text="Quantity:").pack()
        self.quantity_entry = tk.Entry(self.sale_window)
        self.quantity_entry.pack()
        
        if hasattr(self, "frame"):
            pass
        else:
            self.frame = tk.LabelFrame(self.root, text= "Order Summary")
            self.frame.grid(row= 0, column= 1, padx=10, pady=10)

        tk.Button(self.sale_window, text="Process Sale", command=process_sale_button).pack()
        

if __name__ == "__main__":
    root = tk.Tk()
    app = POS_GUI(root)
    root.mainloop()          