from tkinter import *
from PIL import ImageTk, Image

root = Tk()

# set Screen Size
win_width = int(root.winfo_screenwidth() / 3)
win_heigth = int(root.winfo_screenheight() / 3)

root.geometry(f"{win_width}x{win_heigth}")

root.geometry()

# set Icon
if sys.platform.startswith("win"):
    root.iconbitmap("./hacker.ico")
else:
    root.iconphoto(
        True,
        PhotoImage(file="./ghost.ico")
    )

my_photo = ImageTk.PhotoImage(Image.open("./hack.ico"))
mylabel = Label(image=my_photo)
mylabel.pack()

# Set Title
root.title("Image Loader App")
Button(root, text="close App", command=exit).pack(fill=X)

# close app
root.mainloop()
