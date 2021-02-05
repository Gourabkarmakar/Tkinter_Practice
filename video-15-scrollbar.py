from tkinter import *

root = Tk()
root.geometry("350x300")
scrollbar = Scrollbar(root)
scrollbar.pack(fill='y', side=RIGHT)
listbox = Listbox(root, yscrollcommand=scrollbar.set)
for i in range(100):
    listbox.insert(END, f"Your number is {i}")

listbox.pack(fill=BOTH)
scrollbar.config(command=listbox.yview)
root.mainloop()
