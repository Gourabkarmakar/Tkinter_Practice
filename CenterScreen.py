from tkinter import *

root = Tk()
root.title("Gksecurity- Center Screen")
app_width = 300
app_height = 500
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Get Center Positions App
x = int((screen_width / 2) - (app_width / 2))
y = int((screen_height / 2) - (app_height / 2))

root.geometry(f'{app_width}x{app_height}+{x}+{y}')
My_label = Label(root, text="Window Width: {}, Window Height: {}".format(screen_width, screen_height))
My_label.pack()

root.mainloop()
