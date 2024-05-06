import tkinter as tk
from tkinter import messagebox
import mysql.connector

# Connect to MySQL database
def connect():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Isha@mysql1",
        database="pharmacy"
    )

# Add a new medicine to the inventory
def add_medicine():
    name = name_entry.get()
    quantity = quantity_entry.get()
    price = price_entry.get()

    conn = connect()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO medicines (name, quantity, price) VALUES (%s, %s, %s)", (name, quantity, price))
    conn.commit()
    conn.close()

    messagebox.showinfo("Success", "Medicine added successfully!")

# Display all medicines in the inventory
def view_medicines():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM medicines")
    rows = cursor.fetchall()
    conn.close()

    medicine_list.delete(0, tk.END)

    for row in rows:
        medicine_list.insert(tk.END, row)

# Main Window
root = tk.Tk()
root.title("Pharmacy Management System")
root.attributes('-fullscreen', True)

# Labels
tk.Label(root, text="Medicine Name:").pack()
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="Quantity:").pack()
quantity_entry = tk.Entry(root)
quantity_entry.pack()

tk.Label(root, text="Price:").pack()
price_entry = tk.Entry(root)
price_entry.pack()

# Buttons
add_button = tk.Button(root, text="Add Medicine", command=add_medicine)
add_button.pack()

view_button = tk.Button(root, text="View Medicines", command=view_medicines)
view_button.pack()

medicine_list = tk.Listbox(root, width=50)
medicine_list.pack()

exit_button = tk.Button(root, text="Exit", command=root.destroy)
exit_button.pack()

root.mainloop()
