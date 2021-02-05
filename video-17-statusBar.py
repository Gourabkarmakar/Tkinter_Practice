from tkinter import *
import tkinter.messagebox as tmsg


def upload():
    import time
    statusvar.set("Busy..")
    stbar.update()
    time.sleep(2)
    statusvar.set("Ready for next Instraction")
    tmsg.showinfo("Upload status", "Complete.....")


root = Tk()
height = 300
width = 450
root.geometry(f"{width}x{height}")
root.resizable("false", "false")
root.title("Gk security")
statusvar = StringVar()
statusvar.set("Ready")

stbar = Label(root, textvariable=statusvar, relief=SUNKEN, anchor="e")
stbar.pack(side=BOTTOM, fill=X)
Button(root, text="Upload", command=upload).pack()

root.mainloop()
