import tkinter as tk
from tkinter import messagebox
from datetime import date


def calculate_age():
    try:
        day = int(day_var.get())
        month = int(month_var.get())
        year = int(year_var.get())

        birth_date = date(year, month, day)
        today = date.today()

        if birth_date > today:
            messagebox.showerror("Invalid Date", "Date of birth cannot be in the future.")
            return

        age_years = today.year - birth_date.year
        if (today.month, today.day) < (birth_date.month, birth_date.day):
            age_years -= 1

        result_label.config(text=f"Present age: {age_years} years")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers for day, month, and year.")
    except Exception as e:
        messagebox.showerror("Error", str(e))


root = tk.Tk()
root.title("Age Calculator")
root.geometry("320x220")
root.resizable(False, False)

frame = tk.Frame(root, padx=15, pady=15)
frame.pack(expand=True, fill="both")

label = tk.Label(frame, text="Enter your date of birth:", font=("Arial", 12))
label.grid(row=0, column=0, columnspan=2, pady=(0, 10), sticky="w")

tk.Label(frame, text="Day:").grid(row=1, column=0, sticky="e", padx=(0, 5), pady=5)
day_var = tk.StringVar()
day_entry = tk.Entry(frame, textvariable=day_var, width=10)
day_entry.grid(row=1, column=1, sticky="w", pady=5)

tk.Label(frame, text="Month:").grid(row=2, column=0, sticky="e", padx=(0, 5), pady=5)
month_var = tk.StringVar()
month_entry = tk.Entry(frame, textvariable=month_var, width=10)
month_entry.grid(row=2, column=1, sticky="w", pady=5)

tk.Label(frame, text="Year:").grid(row=3, column=0, sticky="e", padx=(0, 5), pady=5)
year_var = tk.StringVar()
year_entry = tk.Entry(frame, textvariable=year_var, width=10)
year_entry.grid(row=3, column=1, sticky="w", pady=5)

calc_button = tk.Button(frame, text="Calculate Age", command=calculate_age, width=20)
calc_button.grid(row=4, column=0, columnspan=2, pady=15)

result_label = tk.Label(frame, text="Present age: ", font=("Arial", 11, "bold"))
result_label.grid(row=5, column=0, columnspan=2)

root.mainloop()
