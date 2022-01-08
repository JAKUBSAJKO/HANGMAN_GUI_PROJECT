from tkinter import *
from PIL import ImageTk, Image
from tkinter_custom_button import TkinterCustomButton
from tkinter import messagebox

root = Tk()
root.geometry("980x540")

test = messagebox.showinfo("test", 'test')
print(test)
if test == 'ok':
    label = Label(root, text='ttttt').pack()

root.mainloop()