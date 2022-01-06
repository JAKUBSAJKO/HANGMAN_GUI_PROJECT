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
    root.withdraw()
    game = Toplevel()
    game.title("HANGMAN")
    game.geometry("980x540")

    Lab111 = Label(game, text=word)
    Lab111.pack()


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