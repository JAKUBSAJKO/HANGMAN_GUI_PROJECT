from tkinter import *
from PIL import ImageTk, Image
from tkinter_custom_button import TkinterCustomButton
from tkinter import messagebox
import random
import words

# Variable
word = ''
category = ''
user_word = []
numLives = 5

def inTheCenter(master):
    window_height = 540
    window_width = 980
    screen_width = master.winfo_screenwidth()
    screen_height = master.winfo_screenheight()
    x_cordinate = int((screen_width / 2) - (window_width / 2))
    y_cordinate = int((screen_height / 2) - (window_height / 2))
    master.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate-10, y_cordinate-16))

# Main Window
root = Tk()
root.title("HANGMAN")
root.resizable(width=FALSE, height=FALSE)
inTheCenter(root)

# Icon
icon = PhotoImage(file='files/icon.png')
root.tk.call('wm', 'iconphoto', root._w, icon)

# Game Window
def game_window(word):
    def letter_info(letter):
        def used_button(button, letter, row, col, px, py):
            button = TkinterCustomButton(master=game, text=letter, hover_color="#5a0600",
                                       fg_color="#5a0600", text_color="#000000", width=width_btn, height=height_btn,
                                       corner_radius=0, text_font=("montserrat", 14, "bold"))
            button.grid(row=row, column=col, pady=(px, py))

        def find_index(word, letter):
            indexes = []

            for index, letter_in_word in enumerate(word):
                if letter.lower() == letter_in_word:
                    indexes.append(index)

            return indexes

        def check_pasword(word, letter):
            global user_word
            global numLives

            found_indexes = find_index(word, letter)

            if len(found_indexes) == 0:
                numLives -= 1

                if numLives == 4:
                    numLivesLabel = Label(game, image=num_lives_4)
                    numLivesLabel.grid(row=0, columnspan=16, padx=(680, 0), pady=(60, 0))

                if numLives == 3:
                    numLivesLabel = Label(game, image=num_lives_3)
                    numLivesLabel.grid(row=0, columnspan=16, padx=(680, 0), pady=(60, 0))

                if numLives == 2:
                    numLivesLabel = Label(game, image=num_lives_2)
                    numLivesLabel.grid(row=0, columnspan=16, padx=(680, 0), pady=(60, 0))

                if numLives == 1:
                    numLivesLabel = Label(game, image=num_lives_1)
                    numLivesLabel.grid(row=0, columnspan=16, padx=(680, 0), pady=(60, 0))

                if numLives == 0:
                    numLivesLabel = Label(game, image=num_lives_0)
                    numLivesLabel.grid(row=0, columnspan=16, padx=(680, 0), pady=(60, 0))

                if numLives == 0:
                    lose = messagebox.showerror(
                        'HANGMAN', 'Niestety nie uda??o si?? zgadn???? has??a :(\nHas??o to ' + word.upper(), parent=game)
                    next_game = messagebox.askyesno('HANGMAN', 'Czy chcesz zagra?? jeszcze raz?', parent=game)
                    if next_game == 1:
                        numLives = 5
                        user_word = []
                        game.destroy()
                        root.deiconify()

                        if len(words.sport) == 0 and len(words.matematyka) == 0 and len(words.muzyka) == 0 and len(
                                words.literatura) == 0 \
                                and len(words.filmy_seriale) == 0:
                            end_game = messagebox.showinfo(
                                "HANGMAN", "Niestety wyczerpa??e?? wszystkie has??a :(\nGra zostanie zamkni??ta.")
                            root.destroy()

                    else:
                        exit_mess = messagebox.askyesno('HANGMAN', 'Czy na pewno chcesz wyj???? do pulpitu?', parent=game)
                        if exit_mess == 1:
                            game.destroy()
                            root.destroy()
                        else:
                            numLives = 5
                            user_word = []
                            game.destroy()
                            root.deiconify()

            else:
                for index in found_indexes:
                    user_word[index] = letter

                displayPasswordLabel = Label(game, text=" ".join(user_word), font=("montserrat", 44, "bold"))
                displayPasswordLabel.grid(row=1, columnspan=16)

                if "".join(user_word).lower() == word:
                    win = messagebox.showinfo('HANGMAN', 'GRATULACJ??! Uda??o ci si?? zgadn???? has??o :)', parent=game)
                    next_game = messagebox.askyesno('HANGMAN', 'Czy chcesz zagra?? jeszcze raz?', parent=game)
                    if next_game == 1:
                        numLives = 5
                        user_word = []
                        game.destroy()
                        root.deiconify()

                        if len(words.sport) == 0 and len(words.matematyka) == 0 and len(words.muzyka) == 0 and len(
                                words.literatura) == 0 \
                                and len(words.filmy_seriale) == 0:

                            end_game = messagebox.showinfo(
                                "HANGMAN", "Niestety wyczerpa??e?? wszystkie has??a :(\nGra zostanie zamkni??ta.")
                            root.destroy()

                    else:
                        exit_mess = messagebox.askyesno('HANGMAN', 'Czy na pewno chcesz wyj???? do pulpitu?', parent=game)
                        if exit_mess == 1:
                            game.destroy()
                            root.destroy()
                        else:
                            numLives = 5
                            user_word = []
                            game.destroy()
                            root.deiconify()

        if letter == "A":
            used_button(btn1, letter, 4, 0, 20, 10)
            check_pasword(word, letter)

        if letter == "??":
            used_button(btn2, letter, 4, 1, 20, 10)
            check_pasword(word, letter)

        if letter == "B":
            used_button(btn3, letter, 4, 2, 20, 10)
            check_pasword(word, letter)

        if letter == "C":
            used_button(btn4, letter, 4, 3, 20, 10)
            check_pasword(word, letter)

        if letter == "??":
            used_button(btn5, letter, 4, 4, 20, 10)
            check_pasword(word, letter)

        if letter == "D":
            used_button(btn6, letter, 4, 5, 20, 10)
            check_pasword(word, letter)

        if letter == "E":
            used_button(btn7, letter, 4, 6, 20, 10)
            check_pasword(word, letter)

        if letter == "??":
            used_button(btn8, letter, 4, 7, 20, 10)
            check_pasword(word, letter)

        if letter == "F":
            used_button(btn9, letter, 4, 8, 20, 10)
            check_pasword(word, letter)

        if letter == "G":
            used_button(btn10, letter, 4, 9, 20, 10)
            check_pasword(word, letter)

        if letter == "H":
            used_button(btn11, letter, 4, 10, 20, 10)
            check_pasword(word, letter)

        if letter == "I":
            used_button(btn12, letter, 4, 11, 20, 10)
            check_pasword(word, letter)

        if letter == "J":
            used_button(btn13, letter, 4, 12, 20, 10)
            check_pasword(word, letter)

        if letter == "K":
            used_button(btn14, letter, 4, 13, 20, 10)
            check_pasword(word, letter)

        if letter == "L":
            used_button(btn15, letter, 4, 14, 20, 10)
            check_pasword(word, letter)

        if letter == "??":
            used_button(btn16, letter, 4, 15, 20, 10)
            check_pasword(word, letter)

        if letter == "M":
            used_button(btn17, letter, 5, 0, 10, 10)
            check_pasword(word, letter)

        if letter == "N":
            used_button(btn18, letter, 5, 1, 10, 10)
            check_pasword(word, letter)

        if letter == "??":
            used_button(btn19, letter, 5, 2, 10, 10)
            check_pasword(word, letter)

        if letter == "O":
            used_button(btn20, letter, 5, 3, 10, 10)
            check_pasword(word, letter)

        if letter == "??":
            used_button(btn21, letter, 5, 4, 10, 10)
            check_pasword(word, letter)

        if letter == "P":
            used_button(btn22, letter, 5, 5, 10, 10)
            check_pasword(word, letter)

        if letter == "R":
            used_button(btn23, letter, 5, 6, 10, 10)
            check_pasword(word, letter)

        if letter == "S":
            used_button(btn24, letter, 5, 7, 10, 10)
            check_pasword(word, letter)

        if letter == "??":
            used_button(btn25, letter, 5, 8, 10, 10)
            check_pasword(word, letter)

        if letter == "T":
            used_button(btn26, letter, 5, 9, 10, 10)
            check_pasword(word, letter)

        if letter == "U":
            used_button(btn27, letter, 5, 10, 10, 10)
            check_pasword(word, letter)

        if letter == "W":
            used_button(btn28, letter, 5, 11, 10, 10)
            check_pasword(word, letter)

        if letter == "Y":
            used_button(btn29, letter, 5, 12, 10, 10)
            check_pasword(word, letter)

        if letter == "Z":
            used_button(btn30, letter, 5, 13, 10, 10)
            check_pasword(word, letter)

        if letter == "??":
            used_button(btn31, letter, 5, 14, 10, 10)
            check_pasword(word, letter)

        if letter == "??":
            used_button(btn32, letter, 5, 15, 10, 10)
            check_pasword(word, letter)

    def back():
        global user_word
        global numLives

        areyousure = messagebox.askyesno('HANGMAN', 'Czy na pewno chcesz wyj?????', parent=game)
        if areyousure == 1:
            numLives = 5
            user_word = []
            game.destroy()
            root.deiconify()

    global user_word

    root.withdraw()
    game = Toplevel()
    game.title("HANGMAN")
    game.resizable(width=FALSE, height=FALSE)
    inTheCenter(game)

    # Icon
    iconGame = PhotoImage(file='files/icon.png')
    game.tk.call('wm', 'iconphoto', game._w, icon)

    logoLabelGame = Label(game, image=logo)
    logoLabelGame.grid(row=0, columnspan=16, padx=(289, 289), pady=(60, 60))

    # Live Graphics
    global num_lives_0
    global num_lives_1
    global num_lives_2
    global num_lives_3
    global num_lives_4
    global num_lives_5

    num_lives_0 = ImageTk.PhotoImage(Image.open('files/numLives_0.png'))
    num_lives_1 = ImageTk.PhotoImage(Image.open('files/numLives_1.png'))
    num_lives_2 = ImageTk.PhotoImage(Image.open('files/numLives_2.png'))
    num_lives_3 = ImageTk.PhotoImage(Image.open('files/numLives_3.png'))
    num_lives_4 = ImageTk.PhotoImage(Image.open('files/numLives_4.png'))
    num_lives_5 = ImageTk.PhotoImage(Image.open('files/numLives_5.png'))

    # Display Lives Graphics
    numLivesLabel = Label(game, image=num_lives_5)
    numLivesLabel.grid(row=0, columnspan=16, padx=(680, 0), pady=(60, 0))

    # Display Password
    displayPasswordLabel = Label(game, text=" ".join(user_word), font=("montserrat", 44, "bold"))
    displayPasswordLabel.grid(row=1, columnspan=16)

    # Display Category
    global category
    categoryLabel = Label(game, text="KATEGORIA: " + category, font=("montserrat", 10, "italic"))
    categoryLabel.grid(row=2, columnspan=16, pady=(10,0), sticky='we')

    # Letters Buttons - Width And Height
    width_btn = 40
    height_btn = 60

    # Letters Buttons
    btn1 = TkinterCustomButton(master=game, text="A", command=lambda: letter_info("A"), hover_color="#a85c16",
                               fg_color="#d87215", text_color="#ffffff", width=width_btn, height=height_btn,
                               corner_radius=0, text_font=("montserrat", 14, "bold"))
    btn1.grid(row=4, column=0, pady=(20, 10))
    btn2 = TkinterCustomButton(master=game, text="??", command=lambda: letter_info("??"), hover_color="#a85c16",
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
    btn5 = TkinterCustomButton(master=game, text="??", command=lambda: letter_info("??"), hover_color="#a85c16",
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
    btn8 = TkinterCustomButton(master=game, text="??", command=lambda: letter_info("??"), hover_color="#a85c16",
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
    btn16 = TkinterCustomButton(master=game, text="??", command=lambda: letter_info("??"), hover_color="#a85c16",
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
    btn19 = TkinterCustomButton(master=game, text="??", command=lambda: letter_info("??"), hover_color="#a85c16",
                                fg_color="#d87215", text_color="#ffffff", width=width_btn, height=height_btn,
                                corner_radius=0, text_font=("montserrat", 14, "bold"))
    btn19.grid(row=5, column=2)
    btn20 = TkinterCustomButton(master=game, text="O", command=lambda: letter_info("O"), hover_color="#a85c16",
                                fg_color="#d87215", text_color="#ffffff", width=width_btn, height=height_btn,
                                corner_radius=0, text_font=("montserrat", 14, "bold"))
    btn20.grid(row=5, column=3)
    btn21 = TkinterCustomButton(master=game, text="??", command=lambda: letter_info("??"), hover_color="#a85c16",
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
    btn25 = TkinterCustomButton(master=game, text="??", command=lambda: letter_info("??"), hover_color="#a85c16",
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
    btn31 = TkinterCustomButton(master=game, text="??", command=lambda: letter_info("??"), hover_color="#a85c16",
                                fg_color="#d87215", text_color="#ffffff", width=width_btn, height=height_btn,
                                corner_radius=0, text_font=("montserrat", 14, "bold"))
    btn31.grid(row=5, column=14)
    btn32 = TkinterCustomButton(master=game, text="??", command=lambda: letter_info("??"), hover_color="#a85c16",
                                fg_color="#d87215", text_color="#ffffff", width=width_btn, height=height_btn,
                                corner_radius=0, text_font=("montserrat", 14, "bold"))
    btn32.grid(row=5, column=15)

    exitBtn = TkinterCustomButton(master=game, text="WYJD??", command=back, hover_color="#730000", fg_color="#9a0000",
                                  width=120, height=46, corner_radius=10, text_font=("montserrat", 10, "bold"))
    exitBtn.grid(row=6, columnspan=16, pady=(10, 10))

    # X Button Event
    game.protocol("WM_DELETE_WINDOW", back)

def game_rules():
    def back_from_gr():
        game_rules.destroy()
        root.deiconify()

    global icon
    global gr_graphic

    root.withdraw()
    game_rules = Toplevel()
    game_rules.title("HANGMAN")
    game_rules.resizable(width=FALSE, height=FALSE)
    inTheCenter(game_rules)

    # Icon
    game_rules.tk.call('wm', 'iconphoto', game_rules._w, icon)

    gr_graphic = ImageTk.PhotoImage(Image.open('files/game_rules.png'))
    grLabel = Label(game_rules, image=gr_graphic)
    grLabel.grid(row=0)

    backBtn = TkinterCustomButton(master=game_rules, text="WR????", command=back_from_gr, hover_color="#730000",
                                  fg_color="#9a0000", width=100, height=40, corner_radius=10,
                                  text_font=("montserrat", 10, "bold"))
    backBtn.grid(row=0, pady=(440, 0))

    # X Button Event
    game_rules.protocol("WM_DELETE_WINDOW", back_from_gr)

def exit_game():
    exit = messagebox.askyesno("HANGMAN", "Czy na pewno chcesz zamkn???? gr???")
    if exit == 1:
        root.destroy()

def empty_cat():
    empty = messagebox.showerror("HANGMAN", "Niestety wykoszysta??e?? wszyskie has??a z tej kategorii.\nWybierz inn?? kategori??!")

def cat_sport():
    word = random.choice(words.sport)
    words.sport.remove(word)

    global category
    category = 'SPORT'

    if len(words.sport) == 0:
        cat1 = TkinterCustomButton(text="SPORT", command=empty_cat, hover_color="#740800", fg_color="#740800",
                                   width=140,
                                   height=60, corner_radius=10, text_font=("montserrat", 10, "bold"))
        cat1.grid(row=2, column=0, padx=(60, 0))

    for _ in word:
        user_word.append("_")

    game_window(word)

def cat_math():
    word = random.choice(words.matematyka)
    words.matematyka.remove(word)

    global category
    category = 'MATEMATYKA'

    if len(words.matematyka) == 0:
        cat2 = TkinterCustomButton(text="MATEMATYKA", command=empty_cat, hover_color="#740800", fg_color="#740800",
                                   width=140,
                                   height=60, corner_radius=10, text_font=("montserrat", 10, "bold"))
        cat2.grid(row=2, column=1)

    for _ in word:
        user_word.append("_")

    game_window(word)

def cat_music():
    word = random.choice(words.muzyka)
    words.muzyka.remove(word)

    global category
    category = 'MUZYKA'

    if len(words.muzyka) == 0:
        cat3 = TkinterCustomButton(text="MUZYKA", command=empty_cat, hover_color="#740800", fg_color="#740800",
                                   width=140,
                                   height=60, corner_radius=10, text_font=("montserrat", 10, "bold"))
        cat3.grid(row=2, column=2)

    for _ in word:
        user_word.append("_")

    game_window(word)

def cat_literature ():
    word = random.choice(words.literatura)
    words.literatura.remove(word)

    global category
    category = 'LITERATURA'

    if len(words.literatura) == 0:
        cat4 = TkinterCustomButton(text="LITERATURA", command=empty_cat, hover_color="#740800", fg_color="#740800",
                                   width=140, height=60, corner_radius=10, text_font=("montserrat", 10, "bold"))
        cat4.grid(row=2, column=3)

    for _ in word:
        user_word.append("_")

    game_window(word)

def cat_movies_and_series():
    word = random.choice(words.filmy_seriale)
    words.filmy_seriale.remove(word)

    global category
    category = 'FILMY I SERIALE'

    if len(words.filmy_seriale) == 0:
        cat5 = TkinterCustomButton(text="FILMY\nI SERIALE", command=empty_cat, hover_color="#740800",
                                   fg_color="#740800", width=140, height=60, corner_radius=10,
                                   text_font=("montserrat", 10, "bold"))
        cat5.grid(row=2, column=4, padx=(0, 60))

    for _ in word:
        user_word.append("_")

    game_window(word)

# Logo And Question Label
logo = ImageTk.PhotoImage(Image.open('files/logo.png'))
logoLabel = Label(root, image=logo)
logoLabel.grid(row=0, columnspan=5, padx=(289, 289), pady=(80, 60))

questionLabel = Label(root, text="Jak?? kategori?? wybierasz?", font=("montserrat", 20, "normal", "italic"))
questionLabel.grid(row=1, columnspan=5, padx=(289, 289), pady=(20, 40))

# Buttons Category
cat1 = TkinterCustomButton(text="SPORT", command=cat_sport, hover_color="#346202", fg_color="#4f9107", width=140,
                           height=60, corner_radius=10, text_font=("montserrat", 10, "bold"))
cat1.grid(row=2, column=0, padx=(60, 0))
cat2 = TkinterCustomButton(text="MATEMATYKA", command=cat_math, hover_color="#346202", fg_color="#4f9107", width=140,
                           height=60, corner_radius=10, text_font=("montserrat", 10, "bold"))
cat2.grid(row=2, column=1)
cat3 = TkinterCustomButton(text="MUZYKA", command=cat_music, hover_color="#346202", fg_color="#4f9107", width=140,
                           height=60, corner_radius=10, text_font=("montserrat", 10, "bold"))
cat3.grid(row=2, column=2)
cat4 = TkinterCustomButton(text="LITERATURA", command=cat_literature, hover_color="#346202", fg_color="#4f9107",
                           width=140, height=60, corner_radius=10, text_font=("montserrat", 10, "bold"))
cat4.grid(row=2, column=3)
cat5 = TkinterCustomButton(text="FILMY\nI SERIALE", command=cat_movies_and_series, hover_color="#346202",
                           fg_color="#4f9107", width=140, height=60, corner_radius=10,
                           text_font=("montserrat", 10, "bold"))
cat5.grid(row=2, column=4, padx=(0, 60))
rulesBtn = TkinterCustomButton(text="ZASADY GRY", command=game_rules, hover_color="#174363", fg_color="#295e86",
                               width=120, height=46, corner_radius=10, text_font=("montserrat", 10, "bold"))
rulesBtn.grid(row=3, columnspan=5, padx=(50,220), pady=(80, 0))
exitBtn = TkinterCustomButton(text="WYJD??", command=exit_game, hover_color="#730000", fg_color="#9a0000", width=120,
                              height=46, corner_radius=10, text_font=("montserrat", 10, "bold"))
exitBtn.grid(row=3, columnspan=5, padx=(170, 0), pady=(80, 0))

root.mainloop()