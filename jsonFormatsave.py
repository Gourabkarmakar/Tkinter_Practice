from tkinter import *
import json

Titles = "Save To Json Fromat"
root = Tk()
root.title(Titles)


def write_json(setdata, file_name="./data.json"):
    print("Got data")
    with open(file_name, 'w'):
        json.dump(setdata, file_name, indent=4)


def save_data():
    name = name_ent.get()
    post_office = po_ent.get()
    police_stations = ps_ent.get()
    pin_code = pin_ent.get()
    # print(f"{name}: {post_office}: {police_stations}: {pin_code}")

    data = {}
    data["Name"] = name
    data["Post_Office"] = post_office
    data["Police_Stations"] = police_stations
    data["Pin_Code"] = pin_code

    python_to_json = json.dumps(data, indent=4)
    print(python_to_json)
    print(type(python_to_json))

    # json.loads(data)

    df = open("data.json")
    try:
        j_p = json.load(df)
        temp = j_p
        temp.append(data)
    except Exception as e:
        print(e)
        print("got error")

    # write_json(j_p)


name_lbl = Label(root, text="Name", font=("comicsanses ", 15), padx=30, pady=10)
po_lbl = Label(root, text="Post office", font=("comicsanses ", 15), padx=30, pady=10)
ps_lbl = Label(root, text="Police Station", font=("comicsanses ", 15), padx=30, pady=10)
pin_lbl = Label(root, text="Pin", font=("comicsanses ", 15), padx=30, pady=10)

name_ent = Entry(root, font=("Helvetica", 14))
po_ent = Entry(root, font=("Helvetica", 14))
ps_ent = Entry(root, font=("Helvetica", 14))
pin_ent = Entry(root, font=("Helvetica", 14))

button = Button(root, text="Save", font=("comicsanses ", 15), bg="black", fg="white", padx=30, pady=10,
                command=save_data)

name_lbl.grid(row=0, column=0)
po_lbl.grid(row=1, column=0)
ps_lbl.grid(row=2, column=0)
pin_lbl.grid(row=3, column=0)

name_ent.grid(row=0, column=1, padx=20)
po_ent.grid(row=1, column=1, padx=20)
ps_ent.grid(row=2, column=1, padx=20)
pin_ent.grid(row=3, column=1, padx=20)

button.grid(row=4, column=0)

root.mainloop()
