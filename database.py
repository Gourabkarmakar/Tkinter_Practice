# Database connections and Create a record
import sqlite3
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
    # Create a Database
    conn = sqlite3.connect('skFund.db')

    # create a cursor
    c = conn.cursor()

    # insert Into Table
    c.execute(
        "INSERT INTO members VALUES (:ent_f_name, :ent_l_name, :ent_phone, :ent_pin, :ent_address, :ent_fund_amount)", {
            'ent_f_name': ent_f_name.get(),
            'ent_l_name': ent_l_name.get(),
            'ent_phone': ent_phone.get(),
            'ent_pin': ent_pin.get(),
            'ent_address': ent_address.get(),
            'ent_fund_amount': ent_fund_amount.get()
        })
    # Commit Changes
    conn.commit()

    # Close connections
    conn.close()

    # Clear The Text Boxes
    ent_f_name.delete(0, END)
    ent_l_name.delete(0, END)
    ent_phone.delete(0, END)
    ent_pin.delete(0, END)
    ent_address.delete(0, END)
    ent_fund_amount.delete(0, END)


# Query The Database
def query():
    # Create a Database
    conn = sqlite3.connect('skFund.db')

    # create a cursor
    c = conn.cursor()

    # insert Into Table
    c.execute(
        "SELECT *,oid FROM members"
    )
    # Fetch All Record
    records = c.fetchall()
    # Loop The Records
    printRecordes = ''
    for record in records:
        printRecordes += str(record) + "\n"

    query_label = Label(root, text=printRecordes)
    query_label.grid(row=11, column=0, columnspan=2)

    # Commit Changes
    conn.commit()

    # Close connections
    conn.close()


def delete():
    # Create a Database
    conn = sqlite3.connect('skFund.db')

    # create a cursor
    c = conn.cursor()

    # Delete Record
    c.execute(
        "DELETE FROM members WHERE oid = " + ent_select_members.get()
    )
    ent_select_members.delete(0, END)
    # Commit Changes
    conn.commit()

    # Close connections
    conn.close()


def update():
    # Create a Database
    conn = sqlite3.connect('skFund.db')

    # create a cursor
    c = conn.cursor()

    record_id = ent_select_members.get()

    # Update Record
    c.execute(
        """ UPDATE members SET 
        first_name = :first_name,
        last_name = :last_name,
        phone = :phone,
        pin = :pin,
        address = :address,
        fund_amount = :fund_amount 
        WHERE oid = :oid
        """,
        {
            'first_name': ent_f_name_edit.get(),
            'last_name': ent_l_name_edit.get(),
            'phone': ent_phone_edit.get(),
            'pin': ent_pin_edit.get(),
            'address': ent_address_edit.get(),
            'fund_amount': ent_fund_amount_edit.get(),

            'oid': record_id
        }
    )
    # Commit Changes
    conn.commit()

    # Close connections
    conn.close()
    edit.destroy()


def edit():
    # Create Global
    global edit
    global ent_f_name_edit
    global ent_l_name_edit
    global ent_phone_edit
    global ent_pin_edit
    global ent_address_edit
    global ent_fund_amount_edit

    # Create a Database
    conn = sqlite3.connect('skFund.db')

    # create a cursor
    c = conn.cursor()

    record_id = ent_select_members.get()
    # Edit Record
    c.execute(
        "SELECT * FROM members WHERE oid = " + record_id
    )
    records = c.fetchall()

    edit = Tk()

    edit.title("Update Record")
    # Create Label
    f_name_edit = Label(edit, text="First Name: ")
    l_name_edit = Label(edit, text="Last Name: ")
    phone_edit = Label(edit, text="Phone Number: ")
    pin_edit = Label(edit, text="Pin Code: ")
    address_edit = Label(edit, text="Address: ")
    fund_amount_edit = Label(edit, text="Fund Amount: ")


    # Create Entry Widget
    ent_f_name_edit = Entry(edit, width=30)
    ent_l_name_edit = Entry(edit, width=30)
    ent_phone_edit = Entry(edit, width=30)
    ent_pin_edit = Entry(edit, width=30)
    ent_address_edit = Entry(edit, width=30)
    ent_fund_amount_edit = Entry(edit, width=30)


    # Add Grid
    f_name_edit.grid(row=0, column=0)
    ent_f_name_edit.grid(row=0, column=1)
    l_name_edit.grid(row=1, column=0)
    ent_l_name_edit.grid(row=1, column=1)
    phone_edit.grid(row=2, column=0)
    ent_phone_edit.grid(row=2, column=1)
    pin_edit.grid(row=3, column=0)
    ent_pin_edit.grid(row=3, column=1)
    address_edit.grid(row=4, column=0)
    ent_address_edit.grid(row=4, column=1)
    fund_amount_edit.grid(row=5, column=0)
    ent_fund_amount_edit.grid(row=5, column=1)

    # Loop Through Record
    for record in records:
        ent_f_name_edit.insert(0, record[0])
        ent_l_name_edit.insert(0, record[1])
        ent_phone_edit.insert(0, record[2])
        ent_pin_edit.insert(0, record[3])
        ent_address_edit.insert(0, record[4])
        ent_fund_amount_edit.insert(0, record[5])

    print(ent_f_name_edit.get(), ent_l_name_edit.get(), ent_phone_edit.get(), ent_pin_edit.get(), ent_address_edit.get(), ent_fund_amount_edit.get())

    # Create a save Button To Update Record
    save = Button(edit, text="Save Record", command=update)
    save.grid(row=6, column=0, columnspan=2, ipadx=138, pady=(10, 0))

    # Commit Changes
    conn.commit()

    # Close connections
    conn.close()


# Create Label
f_name = Label(root, text="First Name: ")
l_name = Label(root, text="Last Name: ")
phone = Label(root, text="Phone Number: ")
pin = Label(root, text="Pin Code: ")
address = Label(root, text="Address: ")
fund_amount = Label(root, text="Fund Amount: ")
select_members = Label(root, text="Select ID")

# Create Entry Widget
ent_f_name = Entry(root, width=30)
ent_l_name = Entry(root, width=30)
ent_phone = Entry(root, width=30)
ent_pin = Entry(root, width=30)
ent_address = Entry(root, width=30)
ent_fund_amount = Entry(root, width=30)
ent_select_members = Entry(root, width=30)

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
select_members.grid(row=8, column=0)
ent_select_members.grid(row=8, column=1)

# Submit Button
submit_btn = Button(root, text="Add Record To Data Base", command=submit)
submit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)
# Query Button
query_btn = Button(root, text="Query Database", command=query)
query_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=130)

# Delete Button
delete_btn = Button(root, text="Delete Record", command=delete)
delete_btn.grid(row=9, column=0, columnspan=2, ipadx=138, pady=(10, 0))

# Create a Update Button
edit_btn = Button(root, text="Edit Record", command=edit)
edit_btn.grid(row=10, column=0, columnspan=2, ipadx=138, pady=(10, 0))

root.mainloop()
