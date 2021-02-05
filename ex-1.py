from tkinter import *

root = Tk()


def resize():
    height_val = height.get()
    width_val = width.get()
    root.geometry(f"{width_val}x{height_val}")


root.title("Gk security")
root.geometry("500x400")
root.resizable("false","false")
Label(root, text="New Resizing window", font="comicsanses,20,bold").grid(row=0, column=2)
Label(root, text="WIDTH", font="11,bold",padx=30,pady=10).grid(row=1, column=1)
Label(root, text="HEIGHT", font="11,bold",padx=30,pady=10).grid(row=2, column=1)
width = StringVar()
height = StringVar()
width_value = Entry(root, textvariable=width).grid(row=1, column=2)
height_value = Entry(root, textvariable=height).grid(row=2, column=2)
Button(root, text="Submit", command=resize).grid(row=3, column=2)
Button(root, text="Quit", command=quit).grid(row=3, column=3)
root.mainloop()
exit()
