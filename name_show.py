from tkinter import *

from import_function import name_it


def get_name():
    if entry_name.get():
        name = name_it(entry_name.get())
        lbl.config(text=name)
    else:
        lbl.config(text="Please Enter Your Name", fg="red")


root = Tk()
root.title("Entry name")
window_height = int(root.winfo_screenheight() / 2)
window_width = int(root.winfo_screenwidth() / 2)
root.geometry(f"{window_width}x{window_height}")

entry_name = Entry(root, foreground="blue", bd=3, width=30, textvariable="Enter your Name")
entry_name.pack(pady=10)
lbl = Label(root, text="", font=("Helvatica", 19, "bold"), fg="green")
lbl.pack(pady=20, ipadx=10, ipady=10)
Button(root, text="SUBMIT", command=get_name).pack(pady=20)
root.mainloop()
