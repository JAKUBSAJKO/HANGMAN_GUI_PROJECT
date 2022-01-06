from tkinter import *
from PIL import ImageTk, Image
from tkinter_custom_button import TkinterCustomButton

root = Tk()
root.geometry("340x200")

label = Label(root, text="to jest test")
label.grid(row=0, columnspan=3)
btn1 = TkinterCustomButton(master=root)
btn1.grid(row=1, column=0)
btn2 = TkinterCustomButton(master=root)
btn2.grid(row=2, column=1)
btn3 = TkinterCustomButton(master=root)
btn3.grid(row=3, column=2)

root.mainloop()