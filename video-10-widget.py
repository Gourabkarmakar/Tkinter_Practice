from tkinter import *
root = Tk()
root.title("Gk security")
root.resizable("false", "false")
canvas_width = 800
canvas_height = 400
root.geometry(f"{canvas_width}x{canvas_height}")
can_widget = Canvas(root, width=canvas_width, height=canvas_height)
can_widget.pack()
can_widget.create_line(0, 0, 800, 400)
can_widget.create_line(0, 400, 800, 0, fill="red")

can_widget.create_rectangle(50, 50, 750, 350, fill="gray")
can_widget.create_oval(70, 70, 730, 330, fill="yellow")
can_widget.create_text(400, 200, text="Python3", fill="blue")
can_widget.create_arc(50, 50, 100, 10)
widget = Label(can_widget, text='Spam', fg='white', bg='black')
widget.pack()
can_widget.create_window(350, 200, window=widget)
root.mainloop()
