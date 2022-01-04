import sys

numLives = 5
word = "testowe"
used_letter = []

user_word = []

def find_index(word, letter):
    indexes = []

    for index, letter_in_word in enumerate(word):
        if letter == letter_in_word:
            indexes.append(index)

    return indexes

def show_state_of_game():
    print()
    print(" ".join(user_word).upper())
    print("Pozostało prób:", numLives)
    print("Użyte litery:", " ".join(used_letter).upper())
    print()

for _ in word:
    user_word.append("_")

while True:
    letter = input("Podaj literę: ")
    used_letter.append(letter)

    found_indexes = find_index(word, letter)

    if len(found_indexes) == 0:
        print('Nie ma takiej litery!')
        numLives -= 1

        if numLives == 0:
            print('Koniec gry :(')
            sys.exit(0)
    else:
        for index in found_indexes:
            user_word[index] = letter

        if "".join(user_word) == word:
            print("Brawo, to jest to słowo!")
            sys.exit(0)

    show_state_of_game()