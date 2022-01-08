from tkinter import *
from PIL import ImageTk, Image
from tkinter_custom_button import TkinterCustomButton
from tkinter import messagebox

root = Tk()
root.geometry("980x540")
def test():
    def true():
        lal = Label(game, text='działa niestety').pack()

    root.withdraw()

    game = Toplevel()
    game.geometry("980x540")

    btn = Button(game, text='click again!', command=true).pack()

    test1 = messagebox.askyesno("TEST", "TAK", parent=game)

    if test1 == 1:
        myLabel = Label(game, text='TAK').pack()
    else:
        myLabel = Label(game, text="NIE").pack()


btn = Button(root, text="Click!", command=test).pack()


root.mainloop()