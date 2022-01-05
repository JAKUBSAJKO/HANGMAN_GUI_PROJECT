import random
import words

used_passwords = []

# print(len(words.test))
#
# test = random.choice(words.test)
# words.test.remove(test)
#
# print(len(words.test))
#
# test = random.choice(words.test)
# words.test.remove(test)
#
# print(len(words.test))
#
# test = random.choice(words.test)
# words.test.remove(test)
#
# print(len(words.test))


while True:
    test = random.choice(words.test)
    words.test.remove(test)

    if len(words.test) == 0:
        print("sorry")
    else:
        print("koniec")
        break