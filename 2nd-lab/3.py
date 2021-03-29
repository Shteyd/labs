from random import choice, randint
from string import ascii_letters, digits

yourChoice = int(input("Какой вариант вы хотите выбрать (1 / 2 / 3 / 4): "))

def options(yourChoice):
    newLen = ''
    if yourChoice == 1:
        for _ in range(0, 5):
            newLen += chr(randint(1040, 1072))
        return newLen
    if yourChoice == 2:
        N = int(input("Введите N: "))
        return 'R'*N
    if yourChoice == 3:
        for i in range(5):
            newLen += randint(0, 9)
        if '3' not in newLen:
            newLen[randint(randint(0, 5))] = 3
        return newLen
    if yourChoice == 4:
        lettersAndDigits = ascii_letters + digits
        for i in range(8):
            newLen += choice(lettersAndDigits)
        if newLen.isalpha() == True:
            newLen[randint(0, 7)] = choice(digits)
        return newLen

print(options(yourChoice))