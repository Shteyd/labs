from random import randint

yourChoice = int(input("Какой вариант вы хотите выбрать (1 / 2 / 3 / 4): "))

def options(yourChoice):
    user_list = input("Введите элементы списка: ").split()
    if yourChoice == 1:
        del user_list[:2]
        for _ in range(2):
            user_list.insert(randint(0, 9), input("Введите элемент: "))
        return user_list
    if yourChoice == 2:
        user_list = user_list[::2]
        for _ in range(2):
            user_list.insert(randint(0, len(user_list)), input("Введите элемент: "))
        return user_list
    if yourChoice == 3:
        del user_list[4:9]
        for _ in range(2):
            user_list.insert(randint(0, len(user_list)), input("Введите элемент: "))
        return user_list
    if yourChoice == 4:
        new_data = input("Введите 5 новых элементов списка: ").split()
        user_list.extend(new_data)
        return user_list[1::2]

print(options(yourChoice))