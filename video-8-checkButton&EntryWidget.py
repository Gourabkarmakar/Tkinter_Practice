from tkinter import *

root = Tk()


def data():
    print(f"Your Name is {namevalue.get()}")
    print(f"Phone is {phonevalue.get()}")
    print(f"Your Gender is {gendervalue.get()}")
    print(f"Your Emergency contact is {emargencyvalue.get()}")
    print(f"Your Payment Mode is {paymentvalue.get()}")


root.title("Gk security")
root.geometry("500x400")
root.resizable("false", "false")
Label(root, text="Welcome to Data Entry From", font=("comicsanses ", 11, "bold"), pady=10).grid(row=0, column=3)
name = Label(root, text="Name: ")
phone = Label(root, text="Phone: ")
gender = Label(root, text="Gender: ")
emargency = Label(root, text="Emargency Contact: ")
payment = Label(root, text="Payment mode: ")

name.grid(row=1, column=2)
phone.grid(row=2, column=2)
gender.grid(row=3, column=2)
emargency.grid(row=4, column=2)
payment.grid(row=5, column=2)

namevalue = StringVar()
phonevalue = StringVar()
gendervalue = StringVar()
emargencyvalue = StringVar()
paymentvalue = StringVar()
foodservicevalue = IntVar()

nameentry = Entry(root, textvariable=namevalue)
phoneentry = Entry(root, textvariable=phonevalue)
genderentry = Entry(root, textvariable=gendervalue)
emargencyentry = Entry(root, textvariable=emargencyvalue)
paymententry = Entry(root, textvariable=paymentvalue)

nameentry.grid(row=1, column=3)
phoneentry.grid(row=2, column=3)
genderentry.grid(row=3, column=3)
emargencyentry.grid(row=4, column=3)
paymententry.grid(row=5, column=3)

foodservice = Checkbutton(root, text="Want to Updates About News", variable=foodservicevalue, pady=5).grid(row=6,
                                                                                                           column=3)
Button(text="Submit", command=data).grid(row=7, column=2)
root.mainloop()
