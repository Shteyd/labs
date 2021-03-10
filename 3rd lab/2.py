from prettytable import PrettyTable

def option_one(my_string, num):
    return [' '.join(my_string[num][:3]), my_string[num][-1], my_string[num][-2]]

def option_two(my_string, num):
    return [' '.join(my_string[num][:3]), my_string[num][-2], my_string[num][-1]]

def option_three(my_string, num):
    return [my_string[num][0], my_string[num][1], my_string[num][2], my_string[num][4] + ', ' + my_string[num][3]]

def option_four(my_string, num):
    return [' '.join(my_string[num][:3]), my_string[num][4] + ', ' + my_string[num][3], ]

yourChoice = int(input("Какой вариант вы хотите выбрать (1 / 2 / 3 / 4): "))

def options(yourChoice):
    my_string = 'Ф;И;О;Возраст;Категория;_Иванов;Иван;Иванович;23 года;Студент 3 курса;_Петров;Семен;Игоревич;22 года;Студент 2 курса'
    my_string = my_string.split(';_')  # разбиваем строку на студентов

    for count in range(3):
        my_string[count] = my_string[count].split(';')

    students_table = PrettyTable()  # создаем таблицу
    if yourChoice == 1:
        students_table.field_names = ['ФИО', 'Категория', 'Возраст']
        students_table.add_rows(
            [option_one(my_string, 1), option_one(my_string, 2), ])
        return students_table
    if yourChoice == 2:
        students_table.field_names = ['ФИО', 'Возраст', 'Категория']
        students_table.add_rows(
            [option_two(my_string, 1), option_two(my_string, 2), ])
        return students_table
    if yourChoice == 3:
        students_table.field_names = ['Ф', 'И', 'О', 'О студенте']
        students_table.add_rows(
            [option_three(my_string, 1), option_three(my_string, 2), ])
        return students_table
    if yourChoice == 4:
        students_table.field_names = ['ФИО', 'О студенте']
        students_table.add_rows(
            [option_four(my_string, 1), option_four(my_string, 2), ])
        return students_table


print(options(yourChoice))
