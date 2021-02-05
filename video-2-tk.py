from tkinter import *

root = Tk()

# width x height
root.geometry("444x234")

# width , height
root.minsize(350, 200)

# width , height

root.maxsize(1000, 550)
lable_1 = Label(text="This is a lable 1 Text")
lable_1.pack()

root.mainloop()
