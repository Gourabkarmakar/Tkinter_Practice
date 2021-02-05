from tkinter import *
import time
import tkinter.messagebox as tmsg


class GUI(Tk):
    def __init__(self):
        super().__init__()
        self.title("Gk security")
        self.geometry("737x344")

    def status(self):
        self.var = StringVar()
        self.var.set("Ready")
        self.statusbar = Label(self, textvar=self.var, relief=SUNKEN, anchor="w")
        self.statusbar.pack(side=BOTTOM, fill=X)

    def createButtom(self, inptext):
        Button(text=inptext, command=self.click).pack()

    def tksleep(self, number):
        try:
            time.sleep(number)
        except:
            print("Got a Error: {}".format())

    def click(self):
        print("Button click")


if __name__ == '__main__':
    window = GUI()
    window.status()
    window.createButtom("UPDATE")
    window.tksleep(2)
    print("You are in Tkinter")
    window.mainloop()
