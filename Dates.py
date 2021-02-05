from tkinter import *
from datetime import datetime

root = Tk()

# Title Set in app
root.title("Date Left year End")

window_info_height = root.winfo_screenheight()
window_info_width = root.winfo_screenwidth()
print(f"Height:{window_info_height}\n Width:{window_info_width}")

# Icon set in any paltform
if sys.platform.startswith('win'):
    root.iconbitmap('ghost.ico')
else:
    logo = PhotoImage(file='./ghost.ico')
    root.call('wm', 'iconphoto', root.w, logo)

# app size set
root.geometry("500x350")
root.resizable("false", "false")

# Set Top fream and Text
frameTop = Frame(root, bg="skyblue", borderwidth=2, relief=SUNKEN)
frameTop.pack(side=TOP, fill=X)
panic = Label(frameTop, text="Don't Panic", font=("Helvetica", 32, "bold"), bg="skyblue", fg="chocolate3")
panic.pack(pady=10, ipadx=10, ipady=10)

# Date Set
today = datetime.today()
frameTop2 = Frame(root, bg="azure2", borderwidth=2, relief=SUNKEN)
frameTop2.pack(side=TOP, fill=X)
f_today = datetime.today().strftime("%A - %B:%-d - %Y")
print(f_today)
print(today)
today_datetime = Label(frameTop2, text=f_today, font='bold')
today_datetime.pack()

# time Set

f_time = datetime.today().strftime("%I-%p : %M : %S")
# print(datetime)
now_time = Label(frameTop2, text=f_time)
now_time.pack()

total_day_in_year = int(365)
print(total_day_in_year)
day_no = int(datetime.today().strftime("%-j"))
print(day_no)

year = datetime.today().strftime("%Y")

left_days = total_day_in_year - day_no
Label(root, text=f"There are {left_days} Days Left in {year}", font=("Helvetica", 22, 'bold'), bg="IndianRed2").pack(
    fill=X, ipady=30)

freame_down = Frame(root, bg="seashell4", borderwidth=3, relief=SUNKEN)
freame_down.pack(side=LEFT, fill=Y)

Label(freame_down, text="Please Don't Scared...!!", font=("Helvetica", 8, 'bold'), bg="burlywood2").pack(pady=10, ipadx=10, ipady=10)
root.mainloop()
