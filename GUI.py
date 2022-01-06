from tkinter import *
from PIL import ImageTk, Image
from tkinter_custom_button import TkinterCustomButton
from tkinter import messagebox
import random
import words

# Variable
word = ''

root = Tk()
root.title("HANGMAN")
root.geometry("980x540")

# Function

def game_window(word):
    def letter_info(letter):
        turn = letter
        test = Label(game, text="Kliknięcto literę -> " + letter).grid(row=2, columnspan=5)

    def back():
        game.destroy()
        root.deiconify()

    root.withdraw()
    game = Toplevel()
    game.title("HANGMAN")
    game.geometry("980x540")

    logoLabelGame = Label(game, image=logo)
    logoLabelGame.grid(row=0, columnspan=15, padx=(289, 289), pady=(60, 60))

    # Letters Buttons
    width_btn = 40
    height_btn = 60

    btn1 = TkinterCustomButton(master=game, text="A", command=lambda: letter_info("A"), hover_color="#a85c16",
                               fg_color="#d87215", text_color="#ffffff", width=width_btn, height=height_btn,
                               corner_radius=0, text_font=("montserrat", 14, "bold"))
    btn1.grid(row=4, column=0, pady=(20, 10))
    btn2 = TkinterCustomButton(master=game, text="Ą", command=lambda: letter_info("Ą"), hover_color="#a85c16",
                               fg_color="#d87215", text_color="#ffffff", width=width_btn, height=height_btn,
                               corner_radius=0, text_font=("montserrat", 14, "bold"))
    btn2.grid(row=4, column=1, pady=(20, 10))
    btn3 = TkinterCustomButton(master=game, text="B", command=lambda: letter_info("B"), hover_color="#a85c16",
                               fg_color="#d87215", text_color="#ffffff", width=width_btn, height=height_btn,
                               corner_radius=0, text_font=("montserrat", 14, "bold"))
    btn3.grid(row=4, column=2, pady=(20, 10))
    btn4 = TkinterCustomButton(master=game, text="C", command=lambda: letter_info("C"), hover_color="#a85c16",
                               fg_color="#d87215", text_color="#ffffff", width=width_btn, height=height_btn,
                               corner_radius=0, text_font=("montserrat", 14, "bold"))
    btn4.grid(row=4, column=3, pady=(20, 10))
    btn5 = TkinterCustomButton(master=game, text="Ć", command=lambda: letter_info("Ć"), hover_color="#a85c16",
                               fg_color="#d87215", text_color="#ffffff", width=width_btn, height=height_btn,
                               corner_radius=0, text_font=("montserrat", 14, "bold"))
    btn5.grid(row=4, column=4, pady=(20, 10))
    btn6 = TkinterCustomButton(master=game, text="D", command=lambda: letter_info("D"), hover_color="#a85c16",
                               fg_color="#d87215", text_color="#ffffff", width=width_btn, height=height_btn,
                               corner_radius=0, text_font=("montserrat", 14, "bold"))
    btn6.grid(row=4, column=5, pady=(20, 10))
    btn7 = TkinterCustomButton(master=game, text="E", command=lambda: letter_info("E"), hover_color="#a85c16",
                               fg_color="#d87215", text_color="#ffffff", width=width_btn, height=height_btn,
                               corner_radius=0, text_font=("montserrat", 14, "bold"))
    btn7.grid(row=4, column=6, pady=(20, 10))
    btn8 = TkinterCustomButton(master=game, text="Ę", command=lambda: letter_info("Ę"), hover_color="#a85c16",
                               fg_color="#d87215", text_color="#ffffff", width=width_btn, height=height_btn,
                               corner_radius=0, text_font=("montserrat", 14, "bold"))
    btn8.grid(row=4, column=7, pady=(20, 10))
    btn9 = TkinterCustomButton(master=game, text="F", command=lambda: letter_info("F"), hover_color="#a85c16",
                               fg_color="#d87215", text_color="#ffffff", width=width_btn, height=height_btn,
                               corner_radius=0, text_font=("montserrat", 14, "bold"))
    btn9.grid(row=4, column=8, pady=(20, 10))
    btn10 = TkinterCustomButton(master=game, text="G", command=lambda: letter_info("G"), hover_color="#a85c16",
                                fg_color="#d87215", text_color="#ffffff", width=width_btn, height=height_btn,
                                corner_radius=0, text_font=("montserrat", 14, "bold"))
    btn10.grid(row=4, column=9, pady=(20, 10))
    btn11 = TkinterCustomButton(master=game, text="H", command=lambda: letter_info("H"), hover_color="#a85c16",
                                fg_color="#d87215", text_color="#ffffff", width=width_btn, height=height_btn,
                                corner_radius=0, text_font=("montserrat", 14, "bold"))
    btn11.grid(row=4, column=10, pady=(20, 10))
    btn12 = TkinterCustomButton(master=game, text="I", command=lambda: letter_info("I"), hover_color="#a85c16",
                                fg_color="#d87215", text_color="#ffffff", width=width_btn, height=height_btn,
                                corner_radius=0, text_font=("montserrat", 14, "bold"))
    btn12.grid(row=4, column=11, pady=(20, 10))
    btn13 = TkinterCustomButton(master=game, text="J", command=lambda: letter_info("J"), hover_color="#a85c16",
                                fg_color="#d87215", text_color="#ffffff", width=width_btn, height=height_btn,
                                corner_radius=0, text_font=("montserrat", 14, "bold"))
    btn13.grid(row=4, column=12, pady=(20, 10))
    btn14 = TkinterCustomButton(master=game, text="K", command=lambda: letter_info("K"), hover_color="#a85c16",
                                fg_color="#d87215", text_color="#ffffff", width=width_btn, height=height_btn,
                                corner_radius=0, text_font=("montserrat", 14, "bold"))
    btn14.grid(row=4, column=13, pady=(20, 10))
    btn15 = TkinterCustomButton(master=game, text="L", command=lambda: letter_info("L"), hover_color="#a85c16",
                                fg_color="#d87215", text_color="#ffffff", width=width_btn, height=height_btn,
                                corner_radius=0, text_font=("montserrat", 14, "bold"))
    btn15.grid(row=4, column=14, pady=(20, 10))
    btn16 = TkinterCustomButton(master=game, text="Ł", command=lambda: letter_info("Ł"), hover_color="#a85c16",
                                fg_color="#d87215", text_color="#ffffff", width=width_btn, height=height_btn,
                                corner_radius=0, text_font=("montserrat", 14, "bold"))
    btn16.grid(row=4, column=15, pady=(20, 10))
    btn17 = TkinterCustomButton(master=game, text="M", command=lambda: letter_info("M"), hover_color="#a85c16",
                                fg_color="#d87215", text_color="#ffffff", width=width_btn, height=height_btn,
                                corner_radius=0, text_font=("montserrat", 14, "bold"))
    btn17.grid(row=5, column=0, pady=(10, 10))
    btn18 = TkinterCustomButton(master=game, text="N", command=lambda: letter_info("N"), hover_color="#a85c16",
                                fg_color="#d87215", text_color="#ffffff", width=width_btn, height=height_btn,
                                corner_radius=0, text_font=("montserrat", 14, "bold"))
    btn18.grid(row=5, column=1)
    btn19 = TkinterCustomButton(master=game, text="Ń", command=lambda: letter_info("Ń"), hover_color="#a85c16",
                                fg_color="#d87215", text_color="#ffffff", width=width_btn, height=height_btn,
                                corner_radius=0, text_font=("montserrat", 14, "bold"))
    btn19.grid(row=5, column=2)
    btn20 = TkinterCustomButton(master=game, text="O", command=lambda: letter_info("O"), hover_color="#a85c16",
                                fg_color="#d87215", text_color="#ffffff", width=width_btn, height=height_btn,
                                corner_radius=0, text_font=("montserrat", 14, "bold"))
    btn20.grid(row=5, column=3)
    btn21 = TkinterCustomButton(master=game, text="Ó", command=lambda: letter_info("Ó"), hover_color="#a85c16",
                                fg_color="#d87215", text_color="#ffffff", width=width_btn, height=height_btn,
                                corner_radius=0, text_font=("montserrat", 14, "bold"))
    btn21.grid(row=5, column=4)
    btn22 = TkinterCustomButton(master=game, text="P", command=lambda: letter_info("P"), hover_color="#a85c16",
                                fg_color="#d87215", text_color="#ffffff", width=width_btn, height=height_btn,
                                corner_radius=0, text_font=("montserrat", 14, "bold"))
    btn22.grid(row=5, column=5)
    btn23 = TkinterCustomButton(master=game, text="R", command=lambda: letter_info("R"), hover_color="#a85c16",
                                fg_color="#d87215", text_color="#ffffff", width=width_btn, height=height_btn,
                                corner_radius=0, text_font=("montserrat", 14, "bold"))
    btn23.grid(row=5, column=6)
    btn24 = TkinterCustomButton(master=game, text="S", command=lambda: letter_info("S"), hover_color="#a85c16",
                                fg_color="#d87215", text_color="#ffffff", width=width_btn, height=height_btn,
                                corner_radius=0, text_font=("montserrat", 14, "bold"))
    btn24.grid(row=5, column=7)
    btn25 = TkinterCustomButton(master=game, text="Ś", command=lambda: letter_info("Ś"), hover_color="#a85c16",
                                fg_color="#d87215", text_color="#ffffff", width=width_btn, height=height_btn,
                                corner_radius=0, text_font=("montserrat", 14, "bold"))
    btn25.grid(row=5, column=8)
    btn26 = TkinterCustomButton(master=game, text="T", command=lambda: letter_info("T"), hover_color="#a85c16",
                                fg_color="#d87215", text_color="#ffffff", width=width_btn, height=height_btn,
                                corner_radius=0, text_font=("montserrat", 14, "bold"))
    btn26.grid(row=5, column=9)
    btn27 = TkinterCustomButton(master=game, text="U", command=lambda: letter_info("U"), hover_color="#a85c16",
                                fg_color="#d87215", text_color="#ffffff", width=width_btn, height=height_btn,
                                corner_radius=0, text_font=("montserrat", 14, "bold"))
    btn27.grid(row=5, column=10)
    btn28 = TkinterCustomButton(master=game, text="W", command=lambda: letter_info("W"), hover_color="#a85c16",
                                fg_color="#d87215", text_color="#ffffff", width=width_btn, height=height_btn,
                                corner_radius=0, text_font=("montserrat", 14, "bold"))
    btn28.grid(row=5, column=11)
    btn29 = TkinterCustomButton(master=game, text="Y", command=lambda: letter_info("Y"), hover_color="#a85c16",
                                fg_color="#d87215", text_color="#ffffff", width=width_btn, height=height_btn,
                                corner_radius=0, text_font=("montserrat", 14, "bold"))
    btn29.grid(row=5, column=12)
    btn30 = TkinterCustomButton(master=game, text="Z", command=lambda: letter_info("Z"), hover_color="#a85c16",
                                fg_color="#d87215", text_color="#ffffff", width=width_btn, height=height_btn,
                                corner_radius=0, text_font=("montserrat", 14, "bold"))
    btn30.grid(row=5, column=13)
    btn31 = TkinterCustomButton(master=game, text="Ź", command=lambda: letter_info("Ź"), hover_color="#a85c16",
                                fg_color="#d87215", text_color="#ffffff", width=width_btn, height=height_btn,
                                corner_radius=0, text_font=("montserrat", 14, "bold"))
    btn31.grid(row=5, column=14)
    btn32 = TkinterCustomButton(master=game, text="Ż", command=lambda: letter_info("Ż"), hover_color="#a85c16",
                                fg_color="#d87215", text_color="#ffffff", width=width_btn, height=height_btn,
                                corner_radius=0, text_font=("montserrat", 14, "bold"))
    btn32.grid(row=5, column=15)

    Lab11 = Label(game, text=word)
    Lab11.grid(row=6, columnspan=5)

    Btn = Button(game, text='Back', command=back)
    Btn.grid(row=7, columnspan=5)


def exit_game():
    exit = messagebox.askyesno("HANGMAN", "Czy na pewno chcesz zamknąć grę?")
    if exit == 1:
        root.destroy()

def cat_sport():
    word = random.choice(words.sport)
    game_window(word)

def cat_math():
    word = random.choice(words.matematyka)
    game_window(word)

def cat_music():
    word = random.choice(words.muzyka)
    game_window(word)

def cat_literature ():
    word = random.choice(words.literatura)
    game_window(word)

def cat_movies_and_series():
    word = random.choice(words.filmy_seriale)
    game_window(word)

# Logo And Question Label
logo = ImageTk.PhotoImage(Image.open('files/logo.png'))
logoLabel = Label(root, image=logo)
logoLabel.grid(row=0, columnspan=5, padx=(289, 289), pady=(80, 60))

questionLabel = Label(root, text="Jaką kategorię wybierasz?", font=("montserrat", 20, "normal", "italic"))
questionLabel.grid(row=1, columnspan=5, padx=(289, 289), pady=(20, 40))

# Buttons Category
cat1 = TkinterCustomButton(text="SPORT", command=cat_sport, hover_color="#808080", fg_color="#4d4d4d", width=140,
                           height=60, corner_radius=10, text_font=("montserrat", 10, "bold"))
cat1.grid(row=2, column=0, padx=(60, 0))
cat2 = TkinterCustomButton(text="MATEMATYKA", command=cat_math, hover_color="#808080", fg_color="#4d4d4d", width=140,
                           height=60, corner_radius=10, text_font=("montserrat", 10, "bold"))
cat2.grid(row=2, column=1)
cat3 = TkinterCustomButton(text="MUZYKA", command=cat_music, hover_color="#808080", fg_color="#4d4d4d", width=140,
                           height=60, corner_radius=10, text_font=("montserrat", 10, "bold"))
cat3.grid(row=2, column=2)
cat4 = TkinterCustomButton(text="LITERATURA", command=cat_literature, hover_color="#808080", fg_color="#4d4d4d",
                           width=140, height=60, corner_radius=10, text_font=("montserrat", 10, "bold"))
cat4.grid(row=2, column=3)
cat5 = TkinterCustomButton(text="FILMY\nI SERIALE", command=cat_movies_and_series, hover_color="#808080",
                           fg_color="#4d4d4d", width=140, height=60, corner_radius=10,
                           text_font=("montserrat", 10, "bold"))
cat5.grid(row=2, column=4, padx=(0, 60))

exitBtn = TkinterCustomButton(text="EXIT", command=exit_game, hover_color="#730000", fg_color="#9a0000", width=120,
                              height=46, corner_radius=10, text_font=("montserrat", 10, "bold"))
exitBtn.grid(row=3, column=2, pady=(90, 0))

root.mainloop()