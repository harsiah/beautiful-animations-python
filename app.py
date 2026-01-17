import tkinter as tk
from tkinter import messagebox, filedialog
from datetime import datetime
import sqlite3

# ----------- DATABASE SETUP -----------
conn = sqlite3.connect("sales.db")
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS sales (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT,
    product_name TEXT,
    price INTEGER,
    quantity INTEGER,
    total INTEGER,
    amount INTEGER,
    change_amount INTEGER
)
""")
conn.commit()

# ----------- FUNCTIONS -----------
products = []

def add_product():
    try:
        name = entry_name.get()
        price = int(entry_price.get())
        qty = int(entry_qty.get())

        if name == "":
            messagebox.showerror("Error", "Product name required")
            return

        total = price * qty
        products.append((name, price, qty, total))
        listbox.insert(tk.END, f"{name} | {price} x {qty} = {total}")
        update_total()

        entry_name.delete(0, tk.END)
        entry_price.delete(0, tk.END)
        entry_qty.delete(0, tk.END)

    except:
        messagebox.showerror("Error", "Enter valid numbers")

def delete_product():
    selected = listbox.curselection()
    if not selected:
        messagebox.showerror("Error", "Select product to delete")
        return
    index = selected[0]
    listbox.delete(index)
    products.pop(index)
    update_total()

def update_total():
    total_price = sum(item[3] for item in products)
    label_total.config(text=f"Total Price: Rp {total_price}")

def calculate_change():
    try:
        amount = int(entry_amount.get())
        total_price = sum(item[3] for item in products)
        change = amount - total_price
        if change < 0:
            messagebox.showerror("Error", "Insufficient payment")
        else:
            label_change.config(text=f"Change: Rp {change}")
    except:
        messagebox.showerror("Error", "Invalid amount")

def generate_receipt():
    if not products:
        messagebox.showerror("Error", "No products")
        return

    try:
        amount = int(entry_amount.get())
    except:
        amount = 0

    total_price = sum(item[3] for item in products)
    change = amount - total_price

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    receipt = "===== RECEIPT =====\n"
    receipt += f"Date: {now}\n\n"
    for p in products:
        receipt += f"{p[0]} - {p[1]} x {p[2]} = Rp {p[3]}\n"
    receipt += "\n-------------------\n"
    receipt += f"Total   : Rp {total_price}\n"
    receipt += f"Amount  : Rp {amount}\n"
    receipt += f"Change  : Rp {change}\n"
    receipt += "===================\nThank you!\n"

    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text File", "*.txt")]
    )

    if file_path:
        with open(file_path, "w") as file:
            file.write(receipt)
        messagebox.showinfo("Success", "Receipt saved successfully")
        save_sales_to_db(now, amount, change)

def save_sales_to_db(date, amount, change):
    for p in products:
        cursor.execute("""
        INSERT INTO sales (date, product_name, price, quantity, total, amount, change_amount)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (date, p[0], p[1], p[2], p[3], amount, change))
    conn.commit()

def new_transaction():
    listbox.delete(0, tk.END)
    entry_name.delete(0, tk.END)
    entry_price.delete(0, tk.END)
    entry_qty.delete(0, tk.END)
    entry_amount.delete(0, tk.END)
    label_total.config(text="Total Price: Rp 0")
    label_change.config(text="Change: Rp 0")
    products.clear()

# ----------- UI -----------
root = tk.Tk()
root.title("Cashier Application")

# Inputs
tk.Label(root, text="Product Name").grid(row=0, column=0)
entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1)

tk.Label(root, text="Price").grid(row=1, column=0)
entry_price = tk.Entry(root)
entry_price.grid(row=1, column=1)

tk.Label(root, text="Quantity").grid(row=2, column=0)
entry_qty = tk.Entry(root)
entry_qty.grid(row=2, column=1)

tk.Button(root, text="Add Product", command=add_product).grid(row=3, column=0, columnspan=2)

# Product list
listbox = tk.Listbox(root, width=50)
listbox.grid(row=4, column=0, columnspan=2)

tk.Button(root, text="Delete Selected", command=delete_product).grid(row=5, column=0, columnspan=2)

# Total
label_total = tk.Label(root, text="Total Price: Rp 0", font=("Arial", 10, "bold"))
label_total.grid(row=6, column=0, columnspan=2)

# Payment
tk.Label(root, text="Amount").grid(row=7, column=0)
entry_amount = tk.Entry(root)
entry_amount.grid(row=7, column=1)

tk.Button(root, text="Calculate Change", command=calculate_change).grid(row=8, column=0, columnspan=2)
label_change = tk.Label(root, text="Change: Rp 0", font=("Arial", 10, "bold"))
label_change.grid(row=9, column=0, columnspan=2)

# Receipt & New Transaction
tk.Button(root, text="Generate Receipt", command=generate_receipt).grid(row=10, column=0, columnspan=2)
tk.Button(root, text="New Transaction / Clear All", command=new_transaction).grid(row=11, column=0, columnspan=2)

root.mainloop()