from tkinter import *
root=Tk()
root.title("Mimi window")
root.geometry("600x600")
name_label=Label(text="Enter Your Name", fg="pink", bg="black", width=600, height=2)
name_entry=Entry()
def display():
    name=name_entry.get()
    output.insert(END,"Hi "+ name )
btn=Button(text="Submit", bg="red", fg="pink",command=display)
output=Text(height=3)

output.pack()
btn.pack()
name_label.pack()

name_entry.pack()


root.mainloop()
