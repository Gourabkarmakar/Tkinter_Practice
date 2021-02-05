from tkinter import *
import tkinter.ttk as ttk

root = Tk()
root.title("TRANSPARENT WINDOW")

if sys.platform.startswith('win'):
    root.iconbitmap("hacker.ico")
else:
    logo = PhotoImage(file="./ghost.ico")
    root.call("wm", "iconphoto", root.w, logo)

window_info_height = int(root.winfo_screenheight() / 3)
window_info_width = int(root.winfo_screenwidth() / 3)

root.geometry(f"{window_info_width}x{window_info_height}")

# root.attributes('-alpha', 0.3)

mylabel = Label(root, text="Hello World", font=("Helvetica", 20))
mylabel.pack(pady=20)


# Create a Slider

def slide(x):
    root.attributes('-alpha', my_slider.get())
    slide_label.config(text=round(my_slider.get(), 2))


def make_solid(e):
    new.attributes("-alpha", 1.0)


def new_window():
    global new
    new = Toplevel()
    new.attributes('-alpha', 0.5)
    new.bind("<Button-1>", make_solid)


my_slider = ttk.Scale(root, from_=0.1, to=1, value=0.7, orient=HORIZONTAL, command=slide)
my_slider.pack()

slide_label = Label(root, text="")
slide_label.pack(pady=10)

new_window = Button(root, text="New Window", command=new_window)
new_window.pack(pady=20)

root.mainloop()
