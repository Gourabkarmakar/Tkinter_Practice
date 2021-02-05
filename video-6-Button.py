from tkinter import *
root=Tk()
root.title("Gk security")
root.geometry("500x400")

def hello():
    print("you press Button")

frame=Frame(root,borderwidth=3,bg="lightgreen",pady=30,relief=SUNKEN)
frame.pack(side=TOP,anchor="nw",fill="x")
b1=Button(frame,fg="blue",text="HELLO",command=hello)
b1.pack(side=LEFT,padx=10)

b2=Button(frame,fg="blue",text="HELLO")
b2.pack(side=LEFT,padx=10)

b3=Button(frame,fg="blue",text="HELLO")
b3.pack(side=LEFT,padx=10)

b4=Button(frame,fg="blue",text="HELLO")
b4.pack(side=LEFT,padx=10)

b5=Button(frame,fg="blue",text="HELLO")
b5.pack(side=LEFT,padx=10)

root.mainloop()