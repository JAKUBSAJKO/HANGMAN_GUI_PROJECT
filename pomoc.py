from tkinter import *
from PIL import ImageTk, Image
from tkinter_custom_button import TkinterCustomButton

root = Tk()
root.geometry("340x200")

word = 'abba'
click = 'd'
user_word = []

def find_index(word, letter):
    indexes = []

    for index, letter_in_word in enumerate(word):
        if letter == letter_in_word:
            indexes.append(index)

    return indexes

for _ in word:
    user_word.append("_")



while True:
    found_indexes = find_index(word, click)

    if len(found_indexes) == 0:
        print("Nie ma")
    else:
        print("jest")

    break

root.mainloop()