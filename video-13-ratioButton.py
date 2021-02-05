from tkinter import *
import tkinter.messagebox as tmsg


def order():
    print(f"your order is {var.get()}")
    tmsg.showinfo("order", f"Your Order {var.get()} is in stock")


root = Tk()
root.title("Gk security")
root.geometry("350x400")
root.resizable('false', 'false')
var = StringVar()

Label(root, text="Please Order your food.", pady=10).pack()
radio = Radiobutton(root, text="Fish Fry", variable=var, value="Fish Fry", padx=10).pack(anchor="w")
radio2 = Radiobutton(root, text="Fish Tikki", variable=var, value="Fish Tikki", padx=10).pack(anchor="w")
radio3 = Radiobutton(root, text="Tanduri Chicken", variable=var, value="Tanduri Chicken", padx=10).pack(anchor="w")
radio4 = Radiobutton(root, text="Chili Checken", variable=var, value="Chili Checken", padx=10).pack(anchor="w")
Button(root, text="Submit", command=order).pack()
root.mainloop()
