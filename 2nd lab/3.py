from random import choice, randint
from string import ascii_letters, digits

yourChoice = int(input("Какой вариант вы хотите выбрать (1 / 2 / 3 / 4): "))

def options(yourChoice):
    if yourChoice == 1:
        bigRuLetters = list('АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'); newLen = []
        for _ in range(0, 5):
            newLen.append(choice(bigRuLetters))
        return newLen
    if yourChoice == 2:
        N = int(input("Введите N: "))
        return 'R'*N
    if yourChoice == 3:
        newLen = ''
        for i in range(5):
            newLen += choice(digits)
        if '3' not in newLen:
            newLen[randint(5)] = 3
        return newLen
    if yourChoice == 4:
        lettersAndDigits = ascii_letters + digits; newLen = ''
        for i in range(8):
            newLen += choice(lettersAndDigits)
        if newLen.isalpha():
            newLen[randint(0, 7)] = choice(digits)
        return newLen

print(options(yourChoice))