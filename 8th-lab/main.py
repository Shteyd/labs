import json, csv 
from time import sleep
from all_ex import all_ex, print_data, logo


def close_program(choice):
    if choice == '' or choice == 'N':
        choice = input("Хотите ли вы сохранить данные в .csv файле? [Y]-Yes [N]-No\n\t> ")
        if choice == 'Y':
            with open("./data/students.csv", "w", encoding="utf-8", newline='') as csv_file:
                csv_file.truncate()
                writer = csv.writer(csv_file, delimiter=';')
                writer.writerow(['№', 'ФИО', 'Возраст', 'Группа'])
                for row in students.items():
                    writer.writerow([row[0], *row[1]])
            print('Изменения успешно внесены в файл!')
        print('Выход из программы...')
        for _ in range(2):
            sleep(0.5)
            print('...')
        exit()


print(f"\033[32m {logo} \033[0m")

while True:
    print("""
    Какую чать лабораторной работы вы хотите выбрать:
        1) Второе задание; 2) Третье задание
    """); choice = int(input("\tВаш выбор:\n\t\t> "))
    if choice == 1:
        while True:
            print('''
                        Список функций:
                1 - ex1 | 4 - ex4 |  8 - ex8
                2 - ex2 | 5 - ex5 |  9 - ex9
                3 - ex3 | 6 - ex6 | 10 - ex10
                        | 7 - ex7 | 
            '''
            ); choice = input('\tВаш выбор:\n\t\t> ')
            students = all_ex(choice)
            print(json.dumps(students, indent=4, sort_keys=True, ensure_ascii=False).encode('utf-8').decode())
            choice = input('Вы хотите продолжить? [Y]-Yes [N]-No\n\t> ')
            close_program(choice)

    if choice == 2:
        while True:
            print("""
    Что вы хотите получить:
    1) Список студентов группы 'БО-111111'.
    2) Список студентов с номерами 1-10.
    3) Список студентов в возрасте 22 лет.
    4) Список студентов с фамилией 'Иванов'.
    5) Список студентов, чьи фамилии заканчиваются на «а».
    6) Список студентов, чей возраст – четное число.
    7) Список студентов, если в возрасте студента встречается число 5.
    8) Список студентов, если их номера группы длиннее 7 символов.
    9) Список студентов, если их «№» четное число.
    10) Список студентов, если их номер группы заканчивается на «1».
    ----------------------------------
    0 - Вернуться к предыдущему выбору
    """)
            choice = int(input('\t> '))

            if choice == 0:
                break
            else:
                data = print_data(choice)
                for row in data:
                    print(row[0] + ") " + ', '.join(row[1]))

            choice = input('Вы хотите продолжить? [Y]-Yes [N]-No\n\t> ')
            close_program(choice)