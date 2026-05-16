import tkinter as tk


def check_strength():
    password = password_entry.get()
    length = len(password)

    if length == 0:
        strength = "No password entered"
    elif length < 4:
        strength = "Very Weak"
    elif length < 7:
        strength = "Weak"
    elif length < 10:
        strength = "Moderate"
    elif length < 13:
        strength = "Strong"
    else:
        strength = "Very Strong"

    result_label.config(text=f"Password strength: {strength}")


root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("360x180")
root.resizable(False, False)

frame = tk.Frame(root, padx=20, pady=15)
frame.pack(fill="both", expand=True)

label = tk.Label(frame, text="Enter password:", font=("Arial", 12))
label.pack(anchor="w")

password_entry = tk.Entry(frame, show="*", width=30)
password_entry.pack(pady=8)

check_button = tk.Button(frame, text="Check Strength", command=check_strength, width=18)
check_button.pack(pady=8)

result_label = tk.Label(frame, text="Password strength: ", font=("Arial", 11), fg="blue")
result_label.pack(pady=(8, 0), anchor="w")

root.mainloop()
