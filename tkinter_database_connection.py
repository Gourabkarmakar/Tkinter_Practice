from tkinter import *
import sys
import sqlite3 as sql3



root = Tk()
if sys.platform.startswith("win"):
    root.iconbitmap("hacker.ico")
else:
    root.iconphoto(
    True,
    PhotoImage(file="ghost.ico")
    )

try:
    conn=sql3.connect("tkinter_1st.db")
    if conn:
        print("Database Connection Sucessfull")
    else:
        print("Show some Problem to connect")

except Exception as e:
    print("Not Connected With DataBase")



dbase=conn.cursor()

dbase.execute(
    """
        CREATE TABLE "Details" (
	"first_name"	TEXT NOT NULL,
	"last_name"	TEXT NOT NULL,
	"aadhar_number"	NUMERIC NOT NULL,
	"voter"	TEXT NOT NULL DEFAULT 'N/A',
	"c/o"	TEXT NOT NULL DEFAULT 'N/A',
	"mobile_number"	NUMERIC);

    """
)

conn.commit()
conn.close()

root.title("Connecting Database")
window_height = int(root.winfo_screenheight() / 3)
window_width = int(root.winfo_screenwidth() / 3)
root.geometry(f"{window_width}x{window_height}")
root.mainloop()
