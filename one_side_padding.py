from tkinter import *

root = Tk()

if sys.platform.startswith("win"):
    root.iconbitmap("hacker.ico")
else:
    root.iconphoto(
        True,
        PhotoImage(file="./ghost.ico")
    )

win_width = int(root.winfo_screenwidth() / 3)
win_heigth = int(root.winfo_screenheight() / 3)

root.geometry(f"{win_width}x{win_heigth}")
root.title("One Side Padding")
root.config(bg="RoyalBlue3")

Button(root, text="Left Side").grid(row=1, column=1, pady=20, padx=(0, 50))
Button(root, text="Right Side").grid(row=1, column=3, pady=20)

root.mainloop()
