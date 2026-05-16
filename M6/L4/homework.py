import tkinter as tk
from tkinter import messagebox


def calculate_compound_interest():
    try:
        principal = float(principal_entry.get())
        rate = float(rate_entry.get())
        time = float(time_entry.get())
        if principal < 0 or rate < 0 or time < 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid non-negative numbers.")
        return

    amount = principal * ((1 + rate / 100) ** time)
    compound_interest = amount - principal
    result_var.set(
        f"Amount: {amount:.2f}\nCompound Interest: {compound_interest:.2f}"
    )


root = tk.Tk()
root.title("Compound Interest Calculator")
root.geometry("320x220")
root.resizable(False, False)

principal_label = tk.Label(root, text="Principal Amount:")
principal_label.pack(pady=(10, 0))
principal_entry = tk.Entry(root)
principal_entry.pack(fill="x", padx=20)

rate_label = tk.Label(root, text="Rate of Interest (% per period):")
rate_label.pack(pady=(10, 0))
rate_entry = tk.Entry(root)
rate_entry.pack(fill="x", padx=20)

time_label = tk.Label(root, text="Time Period (number of periods):")
time_label.pack(pady=(10, 0))
time_entry = tk.Entry(root)
time_entry.pack(fill="x", padx=20)

calculate_button = tk.Button(root, text="Calculate", command=calculate_compound_interest)
calculate_button.pack(pady=15)

result_var = tk.StringVar()
result_label = tk.Label(root, textvariable=result_var, justify="left")
result_label.pack(pady=(0, 10))

root.mainloop()
