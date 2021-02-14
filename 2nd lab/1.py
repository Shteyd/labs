from random import randint

yourChoice = int(input("Какой вариант вы хотите выбрать (1 / 2 / 3 / 4): "))
def options(yourChoice):
    my_number = randint(0, 100)
    if yourChoice == 1:
        while True:
            user_number = int(input("Введите число (0-100): "))
            if user_number < my_number:
                print("my_number = {0}\nuser_number = {1}".format(my_number, user_number))
                break
            else:
                print("Ещё раз")
    if yourChoice == 2:
        while True:
            user_number = int(input("Введите число (0-100): "))
            if user_number == my_number:
                print("my_number = {0}\nuser_number = {1}".format(my_number, user_number))
                break
            else:
                print("Ещё раз")
    if yourChoice == 3:
        while True:
            user_number = int(input("Введите число (0-100): "))
            if user_number == my_number:
                print("Ещё раз")
                break
            else:
                print("my_number = {0}\nuser_number = {1}".format(my_number, user_number))
    if yourChoice == 4:
        while True:
            user_number = int(input("Введите число (0-100): "))
            if user_number > my_number:
                print("my_number = {0}\nuser_number = {1}".format(my_number, user_number))
                break
            else:
                print("Ещё раз")

options(yourChoice)