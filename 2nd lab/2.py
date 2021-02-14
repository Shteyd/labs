yourChoice = int(input("Какой вариант вы хотите выбрать (1 / 2 / 3 / 4): "))

def options(yourChoice):
    yourLens = list(input("Введите несколько строк").split())
    if yourChoice == 1:
        for i in yourLens:
            if 10 > len(i) > 5:
                print(i)
    if yourChoice == 2:
        for i in yourLens:
            if len(i) < 10:
                print(i)
    if yourChoice == 3:
        for i in yourLens:
            if i[-1] == 'r':
                print(i)
    if yourChoice == 4:
        for i in yourLens:
            if i[0] == 'r':
                print(i)

options(yourChoice)