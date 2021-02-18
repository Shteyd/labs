from random import randint

yourChoice = int(input("Какой вариант вы хотите выбрать (1 / 2 / 3 / 4): "))

def options(yourChoice):
    some_list = list(map(int, input("Введите элементы списка: ").split()))
    if yourChoice == 1:
        some_list = some_list[2:]
        for i in range(2):
            some_list.append(randint(1, 10))
        return some_list
    if yourChoice == 2:
        some_list = some_list[::2]
        for i in range(2):
            some_list.append(randint(1, 10))
        return some_list
    if yourChoice == 3:
        some_list = some_list[:4] + some_list[8:]
        for i in range(2):
            some_list.append(randint(1, 10))
        return some_list
    if yourChoice == 4:
        new_list = []; id = 0
        for i in range(5):
            new_list.append(randint(1, 10))
        for i in some_list:
            if id % 2 == 0:
                new_list.append(i)
            id += 1
        return new_list

print(options(yourChoice))