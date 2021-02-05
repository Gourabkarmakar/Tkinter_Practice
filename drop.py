from tkinter import *
from datetime import date
from PIL import Image

root = Tk()

if sys.platform.startswith("win"):
    root.iconbitmap("./hacker.ico")
else:
    root.iconphoto(True, PhotoImage(file="ghost.png"))

title = "Drop Down Menu"
root.title(f"{title}")

width_scren = int(root.winfo_screenwidth() / 3)
height_scren = int(root.winfo_screenheight() / 3)

root.geometry(f"{width_scren}x{height_scren}")

# print Today
today = date.today()
print(today.strftime("%A"))

# clicked is use for storing option
clicked = StringVar()
clicked.set(today.strftime("%A"))
drop_menu = OptionMenu(root, clicked, "Monday", "Tuesday", "Wednesday", "Thisrday", "Friday", "Saturday", "Sunday")
drop_menu.pack(fill=X)

Date_print = Label(root, text="", font=("HELVATICA", 25, "bold"))
Date_print.pack(pady=20)


def show():
    Label(root, text=clicked.get(), fg="brown2").pack(pady=1)


my_button = Button(root, text="Show Selections", command=show).pack()
Date_print.config(text=today)

root.mainloop()
