from tkinter import *
from tkinter import PhotoImage

if __name__ == '__main__':
    # Basic Tkinter setup

    root = Tk()
    root.title("Notepad")
    root.iconphoto(True, PhotoImage(file="./ghost.ico"))

    winWidth = root.winfo_screenwidth()
    winHeight = root.winfo_screenheight()

    root.geometry(f"{winWidth}x{winHeight}")
    # Add Text area
    TextArea = Text(root, font="lucida 13")
    file = None

    # Create Menubar
    Menubar=Menu(root)
    Filiemenu=Menu(Menubar)

    
    root.resizable("false", "false")
    root.mainloop()
