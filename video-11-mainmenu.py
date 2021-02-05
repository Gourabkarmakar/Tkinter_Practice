from tkinter import *
import tkinter.messagebox as tmsg


def __init__():
    print("This is a INIT block")


def help():
    print("Want help")
    tmsg.showinfo("Help", "Gk security will help you with This GUI")


def mike():
    print("You press mike")


def dosti():
    oc = tmsg.askokcancel("Dosti karna Chateho", "Dost Ho to Ok warna dabao Cancel")
    print(oc)
    if oc:
        msg = "Tum Pakka dost ho"
        print(f"{oc} Dost")
    else:
        msg = "Tum Dost kun nehi banna chaceho...?, Kya galti hai meri"
        print(f"{oc} Dosti... So sad for me")
    tmsg.showinfo("Your Desion", msg)


def rate():
    value = tmsg.askquestion("Your Rating", "Your Experince is Good or Not")
    print(value)
    if value == "yes":
        msg = "Greate , Please rate us on Play Store"
        print(f"Thanks For pressing {value}")
    else:
        msg = "Please tell us your problem About this app, We solve it soon.."
        print(f"We are Trying our Best and You press {value}")

    tmsg.showinfo("Experince ", msg)


root = Tk()
root.title("Gk security")
root.geometry("700x550")
mymenu = Menu(root)

menuBar = Menu(root)

m1 = Menu(menuBar, tearoff=0)
m1.add_command(label="save", command=mike)
m1.add_command(label="open", command=mike)
m1.add_separator()
m1.add_command(label="open With", command=mike)
root.config(menu=menuBar)
menuBar.add_cascade(label="File", menu=m1)

m2 = Menu(menuBar, tearoff=0)
m2.add_command(label="save", command=mike)
m2.add_command(label="Exit", command=quit)
m2.add_command(label="open With", command=mike)
root.config(menu=menuBar)
menuBar.add_cascade(label="Exit", menu=m2)

m3 = Menu(menuBar, tearoff=0)
m3.add_command(label="Help", command=help)
m3.add_command(label="Rate Us", command=rate)
m3.add_command(label="Dosti", command=dosti)

root.config(menu=menuBar)
menuBar.add_cascade(label="Help", menu=m3)

root.mainloop()
