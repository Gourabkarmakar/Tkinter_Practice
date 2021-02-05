# Geometry Resize

from tkinter import *


def update():
    print(f"Update size By Height:{height.get()} and width:{width.get()}")
    root.geometry(f"{width.get()}x{height.get()}")


root = Tk()
root.geometry("500x300")
root.resizable("false", "false")
root.title("Gk security")

width = StringVar()
height = StringVar()
Label(root, text="Please Enter Height").pack()
Entry(root, textvariable=height).pack()
Label(root, text="Please Enter Width").pack()
Entry(root, textvariable=width).pack()
Button(root, text="Apply", command=update).pack()

root.mainloop()
