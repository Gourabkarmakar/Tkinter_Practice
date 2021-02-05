from tkinter import *

root = Tk()
root.title("Search And Autofill")


# Update The Listbox
def update(data):
    # clear The Listbox
    mylist.delete(0, END)

    # Add topping To Our Listbox
    for item in data:
        mylist.insert(END, item)


def fillout(event):
    # Delete The Entery box
    myentry.delete(0, END)

    # Add Clicked list item to Entery Box
    myentry.insert(0, mylist.get(ACTIVE))


def check(event):
    # grab what is Type
    typed = myentry.get()
    if typed == '':
        data = toppings
    else:
        data = []
        # Check every time for every words
        for item in toppings:
            # Check every word by letter
            if typed.lower() in item.lower():
                # if lerret found in word then item append in data list
                data.append(item)
    # At last update work
    update(data)


# Create a Label
mylabel = Label(root, text="Start Typing...", font=("Helvetica", 24), fg="gray")
mylabel.pack(pady=20)

# Create a Entry
myentry = Entry(root, font=("Helvetica", 20))
myentry.pack()

# Create a Listbox
mylist = Listbox(root, width=30)
mylist.pack(pady=40)

# Create a list of pizza toppings
toppings = ['Pepperoni', "Peppers", "pizza", "Mushrooms", "Cheese", "Onion", "Hum", "Toco"]

# Add the topping into our list
update(toppings)

# Create a Binding in list
mylist.bind("<<ListboxSelect>>", fillout)

# Create a Binding in entry Box
myentry.bind("<KeyRelease>", check)

root.mainloop()
