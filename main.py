import sys
import string
import random
import words

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

# Start
while True:
    numLives = 5
    used_letter = []
    user_word = []

    while True:
        print("Którą kategorię wybierasz?")
        print("1. Sport")
        print("2. Matematyka")
        print("3. Muzyka")
        print("4. Literatura")
        print("5. Filmy i Seriale")

        if len(words.sport) == 0 and len(words.matematyka) == 0 and len(words.muzyka) == 0 and len(words.literatura) == 0 and len(words.filmy_seriale) == 0:
            print()
            print("Niestety wykorzystałeś wszystkie hasła :(")
            print("Gratulację wytrwałości. Jeśli chcesz jeszcze zagrać uruchom grę ponownie.")
            sys.exit(0)

        try:
            category = int(input("Wybieram kategorię numer: "))
            print()
        except ValueError:
            print("Możesz podać tylko numer kategorii!")
            continue

        if category == 1:
            if len(words.sport) == 0:
                print("Niestety nie ma więcej haseł w tej kategorii :(")
                print("Chcesz wybrać inną kategorię czy zakończyć grę?")
                try:
                    end_category_choise = int(input("1 - inna kategoria\n2 - koniec gry\nWybieram: "))
                    print()
                except ValueError:
                    print("Wybierz 1 lub 0!")

                if end_category_choise == 1:
                    continue
                else:
                    print("Dzięki za grę!")
                    sys.exit(0)

            word = random.choice(words.sport)
            words.sport.remove(word)
            break
        elif category == 2:
            if len(words.matematyka) == 0:
                print("Niestety nie ma więcej haseł w tej kategorii :(")
                print("Chcesz wybrać inną kategorię czy zakończyć grę?")
                try:
                    end_category_choise = int(input("1 - inna kategoria\n2 - koniec gry\nWybieram: "))
                    print()
                except ValueError:
                    print("Wybierz 1 lub 0!")

                if end_category_choise == 1:
                    continue
                else:
                    print("Dzięki za grę!")
                    sys.exit(0)

            # word = random.choice(words.matematyka)
            word = random.choice(words.matematyka)
            words.matematyka.remove(word)
            break
        elif category == 3:
            if len(words.muzyka) == 0:
                print("Niestety nie ma więcej haseł w tej kategorii :(")
                print("Chcesz wybrać inną kategorię czy zakończyć grę?")
                try:
                    end_category_choise = int(input("1 - inna kategoria\n2 - koniec gry\nWybieram: "))
                    print()
                except ValueError:
                    print("Wybierz 1 lub 0!")

                if end_category_choise == 1:
                    continue
                else:
                    print("Dzięki za grę!")
                    sys.exit(0)

            word = random.choice(words.muzyka)
            words.muzyka.remove(word)
            # word = random.choice(words.muzyka)
            break
        elif category == 4:
            if len(words.literatura) == 0:
                print("Niestety nie ma więcej haseł w tej kategorii :(")
                print("Chcesz wybrać inną kategorię czy zakończyć grę?")
                try:
                    end_category_choise = int(input("1 - inna kategoria\n2 - koniec gry\nWybieram: "))
                    print()
                except ValueError:
                    print("Wybierz 1 lub 0!")

                if end_category_choise == 1:
                    continue
                else:
                    print("Dzięki za grę!")
                    sys.exit(0)

            word = random.choice(words.literatura)
            words.literatura.remove(word)
            # word = random.choice(words.literatura)
            break
        elif category == 5:
            if len(words.filmy_seriale) == 0:
                print("Niestety nie ma więcej haseł w tej kategorii :(")
                print("Chcesz wybrać inną kategorię czy zakończyć grę?")
                try:
                    end_category_choise = int(input("1 - inna kategoria\n2 - koniec gry\nWybieram: "))
                    print()
                except ValueError:
                    print("Wybierz 1 lub 0!")

                if end_category_choise == 1:
                    continue
                else:
                    print("Dzięki za grę!")
                    sys.exit(0)

            word = random.choice(words.filmy_seriale)
            words.filmy_seriale.remove(word)
            # word = random.choice(words.filmy_seriale)
            break
        else:
            print("Podaj numer kategorii!")
            continue

    for _ in word:
        user_word.append("_")

    while True:
        letter = input("Podaj literę: ")

        if letter.isdigit() == True:
            print("Nie możesz podać liczby. Podaj literę!")
            print()
            continue
        elif len(letter) > 1 or len(letter) < 0:
            print("Możesz podać tylko jedną literę!")
            print()
            continue
        elif letter.lower() in used_letter:
            print("Już podałeś tę literę. Podaj inną!")
            print()
            continue
        elif letter in string.punctuation:
            print("Nie możesz podać znaku specjalnego. Podaj literę!")
            print()
            continue
        else:
            used_letter.append(letter.lower())

        found_indexes = find_index(word, letter.lower())

        if len(found_indexes) == 0:
            print('Nie ma takiej litery!')
            numLives -= 1

            if numLives == 0:
                print('Koniec gry :(')
                print("Hasło to:", " ".join(word).upper())

                print()
                while True:
                    try:
                        next_game = int(input("Czy chcesz zagrać jeszcze raz? Wpisz 1 jeśli chcesz zagrać jeszcze raz, 0 jeśli kończysz grę: "))
                        print()
                    except ValueError:
                        print("Podaj 1 jeśli chcesz grać dalej, 0 jeśli kończysz grę!")
                        continue
                    break

                if next_game == 1:
                    break
                else:
                    print("Dzięki za grę!")
                    sys.exit(0)
        else:
            for index in found_indexes:
                user_word[index] = letter.lower()

            if "".join(user_word) == word:
                print(" ".join(user_word).upper())
                print("Brawo, to jest to słowo!")
                print()

                while True:
                    try:
                        next_game = int(input("Czy chcesz zagrać jeszcze raz? Wpisz 1 jeśli chcesz zagrać jeszcze raz, 0 jeśli kończysz grę:"))
                        print()
                    except ValueError:
                        print("Podaj 1 jeśli chcesz grać dalej, 0 jeśli kończysz grę!")
                        continue
                    break

                if next_game == 1:
                    break
                else:
                    print("Dzięki za grę!")
                    sys.exit(0)

        show_state_of_game()