from tkinter import *
from PIL import ImageTk, Image

root = Tk()

root.geometry("650x444")

# photo= PhotoImage(file="Goutam.jpg")

# for Jpg images
image = Image.open("Goutam.jpg")
photo = ImageTk.PhotoImage(image)

label_1 = Label(image=photo)
label_1.pack()

Button(root,text="Close Window",command=exit).pack()

root.mainloop()
