import tkinter as tk


def convert_to_cm():
    try:
        inches = float(entry.get())
        centimeters = inches * 2.54
        result_label.config(text=f"{centimeters:.2f} cm")
    except ValueError:
        result_label.config(text="Please enter a valid number.")

root = tk.Tk()
root.title("Inches to Centimeters")

frame = tk.Frame(root, padx=10, pady=10)
frame.pack()

label = tk.Label(frame, text="Length in inches:")
label.grid(row=0, column=0, sticky="w")

entry = tk.Entry(frame, width=20)
entry.grid(row=0, column=1, padx=5)

button = tk.Button(frame, text="Convert", command=convert_to_cm)
button.grid(row=1, column=0, columnspan=2, pady=5)

result_label = tk.Label(frame, text="")
result_label.grid(row=2, column=0, columnspan=2)

root.mainloop()
