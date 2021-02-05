from tkinter import Tk, font
root = Tk()
fonts=font.families()
print(fonts.type())
fonts.foreach(()=>{
    with open('fonts.txt','w') as f:
    f.write(f"{fonts}")
})



root.mainloop()
