# Create a Splash screen

from tkinter import *

splash = Tk()

win_wid_info = int(splash.winfo_screenwidth() / 3)
win_hei_info = int(splash.winfo_screenheight() / 3)

screen_height = splash.winfo_screenheight()
screen_width = splash.winfo_screenwidth()

x_c = int((screen_width/2)-(win_wid_info/2))
y_c = int((screen_height/2)-(win_hei_info/2))

splash.geometry(f"{win_wid_info}x{win_hei_info}+{x_c}+{y_c}")

# Hide The Title
splash.overrideredirect(True)

# set Background color
splash.config(bg="black")

# Set A label in Splash screen
Label(splash, text="Splash Scrren", font=("Helvatica", 19, "bold"), bg="black", fg="white").pack(pady=20)


def main_window():
    # destroy splash screen
    splash.destroy()

    # This is main screen and

    main = Tk()
    main.title("Splash -> Main")
    win_wid_info = int(main.winfo_screenwidth() / 3)
    win_hei_info = int(main.winfo_screenheight() / 3)

    screen_height = main.winfo_screenheight()
    screen_width = main.winfo_screenwidth()

    x_c = int((screen_width/2)-(win_wid_info/2))
    y_c = int((screen_height/2)-(win_hei_info/2))

    main.geometry(f"{win_wid_info}x{win_hei_info}+{x_c}+{y_c}")

    main.config(bg="gray")

    Label(main, text="Main Scrren", font=("Helvatica", 19, "bold"), bg="black", fg="white").pack(pady=(20, 0), ipadx=10,
                                                                                                 ipady=10)


# Calling Main window After 2000 milisecond
splash.after(2000, main_window)

mainloop()
