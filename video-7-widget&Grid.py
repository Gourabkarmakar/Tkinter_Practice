from tkinter import *


def getvals():
    print(f"The value of username is {uservalue.get()}")
    print(f"The value of passsword is {passvalue.get()}")


root = Tk()
root.geometry("500x400")
root.resizable("false", "false")
root.title("Gk security")

user = Label(root, text="User Name: ", font=("Helvetica", 20, "bold")).grid(row=0, column=0, pady=20)
password = Label(root, text="Password: ", font=("Helvetica", 20, "bold")).grid(row=1, column=0, pady=20)
# variable classes in Tkinter
# BooleanVar,DoubleVar,IntVar,StringVar
uservalue = StringVar()
passvalue = StringVar()

userentry = Entry(root, textvariable=uservalue, font=("Helvetica", 20))
passentry = Entry(root, textvariable=passvalue, font=("Helvetica", 20))

userentry.grid(row=0, column=1)
passentry.grid(row=1, column=1)
Button(text="Submit", command=getvals).grid(row=3, column=1, columnspan=2,ipadx=20)
root.mainloop()
