from all_ex import all_ex
from time import sleep


def close_program(choice):
    if choice == '' or choice == 'N':
        print('Выход из программы...')
        for _ in range(2):
            sleep(0.5)
            print('...')
        exit()

while True:
    print(
        '''
                Список функций:
        1 - ex1 | 5 - ex5 |  9 - ex9
        2 - ex2 | 6 - ex6 | 10 - ex10
        3 - ex3 | 7 - ex7 | 
        4 - ex4 | 8 - ex8 | 
        '''
    ); choice = input('Ваш выбор:\n\t> ')
    close_program(choice)
    print(all_ex(choice))
    choice = input('Вы хотите продолжить? [Y]-Yes [N]-No\n\t> ')
    close_program(choice)
    