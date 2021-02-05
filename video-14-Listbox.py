from tkinter import *

root = Tk()


def add_item():
    print("Function called")
    global i
    i = 0
    for i in range(10):
        listbox.insert(ACTIVE, f"Value add {i} Times")


root.title("Gk security")
root.geometry("300x250")
listbox = Listbox(root)
listbox.pack()
listbox.insert(END, 'FIRST LINE ADDED')
Button(root, text="ADD ITEM", command=add_item).pack()
root.mainloop()
