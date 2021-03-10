from tkinter import *
from tkinter import ttk
import tkinter.messagebox as tmsg

root = Tk()
root.title("Tabs By | Gksecurity")
root.geometry("500x500")

my_notebook = ttk.Notebook(root)
my_notebook.pack(fill="both")


def hide():
    tmsg._show("RedTab", "Hide Redtab")
    my_notebook.hide(1)


def show():
    my_notebook.add(my_frame_2, text="Red Tab")


my_frame_1 = Frame(my_notebook, width=500, height=500, bg="blue")
my_frame_2 = Frame(my_notebook, width=500, height=500, bg="red")
my_frame_1.pack(fill="both", expand=1)
my_frame_2.pack(fill="both", expand=1)

my_notebook.add(my_frame_1, text="Blue Tab")
my_notebook.add(my_frame_2, text="Red Tab")

my_botton = Button(my_frame_1, text="Hide Tab-2", command=hide)
my_botton.pack()
my_botton2 = Button(my_frame_1, text="Show Tab-2", command=show)
my_botton2.pack(pady=10)

root.mainloop()
