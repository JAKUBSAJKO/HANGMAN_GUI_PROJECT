from tkinter import *
from PIL import ImageTk, Image
from tkinter_custom_button import TkinterCustomButton
from tkinter import messagebox

root = Tk()
root.geometry("980x540")

def new():
    root.withdraw()
    root1 = Toplevel()
    root1.geometry("980x540")




btn = Button(root, text='Click me!', command=new).pack()

root.mainloop()