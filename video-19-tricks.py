from tkinter import *
from tkinter import PhotoImage


root = Tk()
title = "Gk security"
root.title(f"{title}")
root.resizable("false", "false")
root.iconphoto(True, PhotoImage(file="./ghost.ico"))
root.config(background="gray")
dheight = root.winfo_screenheight()
dwidth = root.winfo_screenwidth()

root.geometry(f"{dwidth}x{dheight}")
Button(root, text="Close window", command=root.destroy).pack()

print(f"{dwidth}x{dheight}")
root.mainloop()
