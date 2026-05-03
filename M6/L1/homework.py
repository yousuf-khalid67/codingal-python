import tkinter as tk
from tkinter import messagebox


def calculate_product():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        product = num1 * num2
        result_label.config(text=f"Product: {product}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")


root = tk.Tk()
root.title("Multiply Two Numbers")
root.geometry("300x180")
root.resizable(False, False)

label1 = tk.Label(root, text="Enter first number:")
label1.pack(pady=(15, 0))
entry1 = tk.Entry(root)
entry1.pack()

label2 = tk.Label(root, text="Enter second number:")
label2.pack(pady=(10, 0))
entry2 = tk.Entry(root)
entry2.pack()

calculate_button = tk.Button(root, text="Calculate Product", command=calculate_product)
calculate_button.pack(pady=10)

result_label = tk.Label(root, text="Product: ")
result_label.pack()

root.mainloop()
