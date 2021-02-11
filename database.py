# Database connections and Create a record
from tkinter import *
import sys

# Create a Object
root = Tk()

# Set Title photo
if sys.platform.startswith("win"):
    root.iconbitmap('./ghost.ico')
else:
    root.iconphoto(
        True,
        PhotoImage(file='./ghost.ico')
    )
# Create a title
root.title("Create a record In Database")


# define Submit
def submit():
    pass


# Create Label
f_name = Label(root, text="First Name: ")
l_name = Label(root, text="Last Name: ")
phone = Label(root, text="Phone Number: ")
pin = Label(root, text="Pin Code: ")
address = Label(root, text="Address: ")
fund_amount = Label(root, text="Fund Amount: ")

# Create Entry Widget
ent_f_name = Entry(root, width=30)
ent_l_name = Entry(root, width=30)
ent_phone = Entry(root, width=30)
ent_pin = Entry(root, width=30)
ent_address = Entry(root, width=30)
ent_fund_amount = Entry(root, width=30)

# Add Grid
f_name.grid(row=0, column=0)
ent_f_name.grid(row=0, column=1)
l_name.grid(row=1, column=0)
ent_l_name.grid(row=1, column=1)
phone.grid(row=2, column=0)
ent_phone.grid(row=2, column=1)
pin.grid(row=3, column=0)
ent_pin.grid(row=3, column=1)
address.grid(row=4, column=0)
ent_address.grid(row=4, column=1)
fund_amount.grid(row=5, column=0)
ent_fund_amount.grid(row=5, column=1)

# Submit Button
submit_btn = Button(root, text="Add Record To Data Base", command=submit)
submit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

root.mainloop()
