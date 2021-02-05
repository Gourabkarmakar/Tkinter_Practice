from tkinter import *


def click(event):
    global scvalue
    # cget is use for get button text
    text = event.widget.cget("text")
    print(text)
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            try:
                value = eval(screen.get())
            except Exception as e:
                print(e)
                value = "ERROR"

        scvalue.set(value)
        screen.update()

    elif text == "C":
        scvalue.set("")
        screen.update()

    else:
        scvalue.set(scvalue.get() + text)
        screen.update()


root = Tk()
titl = "Calculator By @Gk security"
root.title(f"{titl}")
Height = 644
Width = 400

root.geometry(f"{Width}x{Height}")

root.resizable("false", "false")

scvalue = StringVar()
scvalue.set("")

screen = Entry(root, textvar=scvalue, font="lucida 20 bold")
screen.pack(fill=X, ipadx=8, pady=10)

f = Frame(root, bg="gray")

b9 = Button(f, text="9", padx=20, pady=15, font="lucida 30 bold", bg="gray")
b9.pack(side=LEFT, padx=12, pady=12)
b9.bind("<Button-1>", click)

b8 = Button(f, text="8", padx=20, pady=15, font="lucida 30 bold", bg="gray")
b8.pack(side=LEFT, padx=12, pady=12)
b8.bind("<Button-1>", click)

b7 = Button(f, text="7", padx=20, pady=15, font="lucida 30 bold", bg="gray")
b7.pack(side=LEFT, padx=12, pady=12)
b7.bind("<Button-1>", click)

bC = Button(f, text="C", padx=20, pady=15, font="lucida 30 bold", bg="gray")
bC.pack(side=LEFT, padx=12, pady=12)
bC.bind("<Button-1>", click)
f.pack()

f = Frame(root, bg="gray")

b6 = Button(f, text="6", padx=20, pady=15, font="lucida 30 bold", bg="gray")
b6.pack(side=LEFT, padx=12, pady=12)
b6.bind("<Button-1>", click)

b5 = Button(f, text="5", padx=20, pady=15, font="lucida 30 bold", bg="gray")
b5.pack(side=LEFT, padx=12, pady=12)
b5.bind("<Button-1>", click)

b4 = Button(f, text="4", padx=20, pady=15, font="lucida 30 bold", bg="gray")
b4.pack(side=LEFT, padx=12, pady=12)
b4.bind("<Button-1>", click)

bmul = Button(f, text="*", padx=20, pady=15, font="lucida 30 bold", bg="gray")
bmul.pack(side=LEFT, padx=12, pady=12)
bmul.bind("<Button-1>", click)

f.pack()

f = Frame(root, bg="gray")

b3 = Button(f, text="3", padx=20, pady=15, font="lucida 30 bold", bg="gray")
b3.pack(side=LEFT, padx=12, pady=12)
b3.bind("<Button-1>", click)

b2 = Button(f, text="2", padx=20, pady=15, font="lucida 30 bold", bg="gray")
b2.pack(side=LEFT, padx=12, pady=12)
b2.bind("<Button-1>", click)

b1 = Button(f, text="1", padx=20, pady=15, font="lucida 30 bold", bg="gray")
b1.pack(side=LEFT, padx=12, pady=12)
b1.bind("<Button-1>", click)

badd = Button(f, text="+", padx=20, pady=15, font="lucida 30 bold", bg="gray")
badd.pack(side=LEFT, padx=12, pady=12)
badd.bind("<Button-1>", click)

f.pack()

f = Frame(root, bg="gray")

b13 = Button(f, text="0", padx=20, pady=15, font="lucida 30 bold", bg="gray")
b13.pack(side=LEFT, padx=12, pady=12)
b13.bind("<Button-1>", click)

b12 = Button(f, text="%", padx=20, pady=15, font="lucida 30 bold", bg="gray")
b12.pack(side=LEFT, padx=12, pady=12)
b12.bind("<Button-1>", click)

b11 = Button(f, text="-", padx=20, pady=15, font="lucida 30 bold", bg="gray")
b11.pack(side=LEFT, padx=12, pady=12)
b11.bind("<Button-1>", click)

b10 = Button(f, text="=", padx=20, pady=15, font="lucida 30 bold", bg="gray")
b10.pack(side=LEFT, padx=12, pady=12)
b10.bind("<Button-1>", click)

f.pack()

f = Frame(root, bg="gray")

b14 = Button(f, text="/", padx=20, pady=15, font="lucida 30 bold", bg="gray")
b14.pack(side=LEFT, padx=12, pady=12)
b14.bind("<Button-1>", click)

b14 = Button(f, text="Exit", padx=20, pady=15, font="lucida 20 bold", bg="gray")
b14.pack(side=LEFT, padx=12, pady=12)
b14.bind("<Button-1>", exit)

f.pack()
root.mainloop()
