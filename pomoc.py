from tkinter import *
from PIL import ImageTk, Image
from tkinter_custom_button import TkinterCustomButton

root = Tk()
root.geometry("980x540")

img = ImageTk.PhotoImage(Image.open('files/logo.png'))
myLabel = Label(root, image=img)
myLabel.grid(row=0, columnspan=16, padx=(289, 289), pady=(80, 60))

img2 = ImageTk.PhotoImage(Image.open('files/numLives_1.png'))
myLabel1 = Label(root, image=img2)
myLabel1.grid(row=0, columnspan=16, padx=(800, 0), pady=(60, 0))

root.mainloop()