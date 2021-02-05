from tkinter import *
from PIL import ImageTk, Image
import glob


# Functions Define Here
def nextPhoto():
    # print("\tclicked")
    img = next(image_list)
    print("you Clicked Next Image :{}".format(img))
    img1.config(image=img)


root = Tk()
root.title("StatusBar@Gksecurity")
winhei = int(root.winfo_screenheight()/3)
winwid = int(root.winfo_screenwidth()/3)


root.geometry("{}x{}".format(winwid, winhei))
# Load Image
my_img4 = ImageTk.PhotoImage(Image.open("./hack.ico"))
my_img1 = ImageTk.PhotoImage(Image.open("./statusBar/ghost.ico"))
my_img2 = ImageTk.PhotoImage(Image.open('./statusBar/Goutam.jpg'))
my_img3 = ImageTk.PhotoImage(Image.open('./statusBar/DSC_4735.jpg'))
image_list = [my_img1, my_img2, my_img3, my_img4]

# Image list
# image_list = []
# for filename in glob.glob("./statusBar/*.png"):
#     print(filename)
#     img = Image.open(filename)
#     image_list.append(img)
#     print(image_list)


# Resize Image list
# resizeImage = []

# for image in image_list:
#     image.show(image)
#     try:
#         image.resize((300, 225), Image.ANTIALIAS)
#         resizeImage.append(image)
#     except:
#         print("{} This image is Not Resize".format(image))
#         resizeImage.append(image)


# ittrable Image list
image_list = iter(image_list)


if sys.platform.startswith("win"):
    root.iconbitmap("hacker.ico")
else:
    root.call('wm', 'iconphoto', root.w, PhotoImage(file="ghost.ico"))

statusvar = StringVar()
statusvar.set("Number of images")
stbar = Label(root, textvariable=statusvar, relief=SUNKEN, anchor="w")
stbar.pack(side=BOTTOM, fill=X)

img1 = Label(image=my_img4)
img1.pack()

nextimageButton = Button(root, text="Next Photo", command=nextPhoto).pack()
root.mainloop()
