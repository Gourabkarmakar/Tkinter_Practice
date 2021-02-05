from tkinter import *
import tkinter.messagebox as tmsg


def getdoller():
    print(f"We have credited {sc.get()} To your bank account")
    tmsg.showinfo("Ammount Credited", f"Got {sc.get()}")


root = Tk()
root.title("Gk security")
root.geometry("500x400")
# sc=Scale(root,from_=0, to=100).pack()
Label(root, text="How many doller you want ?").pack()
sc = Scale(root, from_=0, to=100, orient=HORIZONTAL, tickinterval=30)
# sc.set(30)
sc.pack(fill=X, ipadx=20)

Button(root, text="Get Dollers", command=getdoller).pack()

root.mainloop()
