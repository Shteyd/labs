from labs import all_labs
from time import sleep


def close_program(choice):
    if choice == '' or choice == 'N':
        print('Выход из программы...')
        for _ in range(2):
            sleep(0.5)
            print('...')
        exit()

while True:
    print('''
                            Список функций (заданий):
    1 - Lab1_1 | 5 - Lab2_1 |  9 - Lab3_1 | 13 - Lab4_1 | 17 - Lab5_1 | 20 - lab7_1
    2 - Lab1_2 | 6 - Lab2_2 | 10 - Lab3_2 | 14 - Lab4_2 | 18 - Lab5_2 | 21 - lab7_2
    3 - Lab1_3 | 7 - Lab2_3 | 11 - Lab3_3 | 15 - Lab4_3 | 19 - Lab5_3 | 22 - lab7_3
    4 - Lab1_4 | 8 - Lab2_4 | 12 - Lab3_4 | 16 - Lab4_4 |             |
    '''); choice = input("Выш выбор:\n\t> ")
    close_program(choice)
    print(all_labs(choice))
    choice = input('Вы хотите продолжить? [Y]-Yes [N]-No\n\t> ')
    close_program(choice)
