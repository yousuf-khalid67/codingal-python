# Import necessary libraries
from tkinter import *

# Create window
root = Tk()
root.title("Event Handler")
root.geometry("100x100")
def open_top_window():
    top=Toplevel()
    top.title("Event Handler")
    top.geometry("50x50")
button = Button(root, text="open new window", command=open_top_window)
button.pack()

root.mainloop()
