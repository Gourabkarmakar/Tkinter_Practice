from tkinter import *


def b1(event):
    print(f"You clicked Button on {event.x}, {event.y}")


root = Tk()
root.title("Gk security")
root.resizable("false", "false")
root.geometry("400x350")
widget = Button(root, text="Clicked")
widget.pack()
widget.bind("<Button-1>", b1)
widget.bind("<Double-1>", quit)
root.mainloop()