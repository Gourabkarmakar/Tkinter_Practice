from tkinter import *

root = Tk()
root.geometry("414x200")
root.title("Gk security")
# Important lable options
# text = adds the text
# bg = background
# fg = foreground
# pady x =X padding
# pady y =Y padding
# relief = bordar styling = SUNKEN ,RAISED ,GROOVE,RIDGE

title_label = Label(text='''Lorem ipsum dolor sit amet consectetur adipisicing elit. "
                       \n"Ut ad illum aliquid consectetur natus, eveniet modi ab. Omnis, "
                       \n"placeat magnam quas praesentium laudantium, esse, "
                       \n"reprehenderit mollitia libero quos earum quam explicabo fuga inventore excepturi'''
                    , bg="red", fg="white", padx=20, pady=30, font=("comicsanses ", 11, "bold"), borderwidth=10,
                    relief=SUNKEN)
# title_label.pack(anchor="ne", side="top",fill=X)
title_label.pack(side="left", fill=Y)

root.mainloop()
