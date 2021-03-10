from tkinter import *

root = Tk()
root.geometry("500x400")
root.title("Gk security")
f1 = Frame(root, bg="skyblue", borderwidth=6, relief=SUNKEN)
f1.pack(side=LEFT, fill=Y)
f2 = Frame(root, borderwidth=6, bg="skyblue", relief=SUNKEN)
f2.pack(side=TOP, fill=X)
l = Label(f1, text="Tkinter", bg="red", padx=50, pady=20)
l.pack(pady=142)
l = Label(f2, text="Wellcome to The Demo project", bg="red", padx=50, pady=20, font=("Helvetica", 16, "bold"))
l.pack()
root.mainloop()
