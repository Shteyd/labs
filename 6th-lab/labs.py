import re
import os
import csv
from functools import reduce
from random import randint, choice
from string import ascii_letters, digits
from prettytable import PrettyTable


# ! Первый вариант
def lab1_1():
    a, b, c, d, f = map(int, input("Введите числа (a, b, c, d, f): ").split())
    if a == 0:
        return "Error: Деление на ноль"
    else:
        return abs(a - b * c * d**3 + (c**5 - a**2)/a + f**3 * (a - 213))
def lab1_2():
    user_list = input("Введите текст: ").split()
    return ''.join(user_list[1::2])
def lab1_3():
    user_numbers = list(map(int, input("Введите числа: ").split()))
    return reduce(lambda x, y: x*y, [num for num in user_numbers if num < 10])
def lab1_4():
    user_numbers = list(map(int, input("Введите числа: ").split()))
    return user_numbers[len(user_numbers) // 2]

# ! Второй вариант
def lab2_1():
    computer_number = randint(0, 101)
    user_number = int(input("Введите число от 0 до 100: "))
    if user_number > computer_number:
        return f"computer_number = {computer_number}\nuser_number = {user_number}"
    else:
        print("Ещё раз")
        return random_num()
def lab2_2():
    user_list = input("Введите строку: ")
    return ' '.join(re.findall(r'\br\w+', user_list))
def lab2_3():
    lettersAndDigits = ascii_letters + digits
    computer_str = ''.join([choice(lettersAndDigits) for _ in range(8)])
    if computer_str.isalpha() == True:
        computer_str = computer_str.replace(computer_str[randint(0, 9)], choice(digits))
    return computer_str
def lab2_4():
    user_str = input("Введите текст: ")
    numbers = ''.join(re.findall(r'\d', user_str))
    letters = ''.join(re.findall(r'[a-zа-я]', user_str, re.IGNORECASE))
    return f'Цифры из строки: {numbers}\nБуквы из строки: {letters}'


# ! Третий вариат
def lab3_1():
    user_str = input("Введите текст: ")
    return ' '.join(re.findall(r"\w+ов\b", user_str))
def lab3_2():
    my_string = 'Ф;И;О;Возраст;Категория;_Иванов;Иван;Иванович;23 года;Студент 3 курса;_Петров;Семен;Игоревич;22 года;Студент 2 курса'.split(';_')
    my_string = [string.split(';') for string in my_string]
    students_table = PrettyTable()
    students_table.field_names = ['ФИО', 'О студенте']
    students_table.add_rows([
        [' '.join(my_string[1][:3]), my_string[1][4] + ', ' + my_string[1][3], ],
        [' '.join(my_string[2][:3]), my_string[2][4] + ', ' + my_string[2][3], ],
    ])
    return students_table
def lab3_3():
    my_string = 'ФИО;Возраст;Категория;_Иванов Иван Иванович;23 года;Студент 3 курса;_Петров Семен Игоревич;22 года;Студент 2 курса;_Иванов Семен Игоревич;22 года;Студент 2 курса;_Акибов Ярослав Наумович;23 года;Студент 3 курса;_Борков Станислав Максимович;21 год;Студент 1 курса;_Петров Семен Семенович;21 год;Студент 1 курса;_Романов Станислав Андреевич;23 года;Студент 3 курса;_Петров Всеволод Борисович;21 год;Студент 2 курса'.split(';_')
    students_table = PrettyTable()
    students_table.field_names = [field for field in my_string[0].split(';')]
    for student in my_string:
        if re.findall(r"^[АБ]\w+", student) != []:
            students_table.add_row(student.split(';'))
    return students_table
def lab3_4():
    user_str = input("Введите строку: ")
    return 'Символов: {0}\nСлов: {1}'.format(len(user_str), len(re.findall(r"\w+", user_str)))


# ! Четвертый вариант
def lab4_1():
    print("Введите матрицу построчно (каждый элемент матрицы через пробел)"); i = 1; matrix = []; sum = 0
    while True:
        print(f"{i}-ая строка матрицы: ", end="")
        some_matrix = list(map(int, input().split()))
        if some_matrix == []:
            break
        for _ in some_matrix:
            sum += _
        matrix.append(some_matrix)
        i += 1
    return f"Ответы:\nМатрица: {matrix}\nСумма всех элементов матрицы: {sum}"
def lab4_2():
    user_list = input("Введите элементы списка: ").split()
    new_data = input("Введите 5 новых элементов списка: ").split()
    user_list.extend(new_data)
    return user_list[1::2]
def lab4_3():
    my_len = [['БО-331101',['Акулова Алена', 'Бабушкина Ксения']],['БОВ-421102', ['Пупкин Вася', 'Петров Андрей']],['БО-331103', ['Береговский Илья', 'Курдус Аким']]]
    students = ''; list_students = []
    for group in my_len:
        if group[0][:3] == 'БО-':
            students = '\n\t'.join(group[1])
            list_students.append('\n\t'.join([group[0], students]))
    return '\n'.join(list_students)
def lab4_4():
    my_len = [['БО-331101',['Акулова Алена', 'Бабушкина Ксения']],['БОВ-421102', ['Пупкин Вася', 'Петров Андрей']],['БО-331103', ['Береговский Илья', 'Курдус Аким']]]
    students = ''; list_students = []
    for group in my_len:
        students = ', '.join(group[1][::2])
        list_students.append(f'{group[0]}:\t{students}')
    return '\n'.join(list_students)


# ! Пятый вариант
def lab5_1():
    choice = input("Вы хотите ввести свою директорию: [Y]-Да [N]-Нет\n  > ")
    if choice == 'Y':
        return len(os.listdir(input("Введите директорию: ")))
    else:
        return len(os.listdir("C:\\Users\Shteyd\Downloads"))
def lab5_2():
    students_table = PrettyTable()
    students = []
    with open("./data/student.csv", "r", encoding='utf-8') as csvfile:
        student_reader = csv.reader(csvfile, delimiter=';')
        for row in student_reader:
            students.append(row)
    
    students_table.field_names = students[0]
    del students[0]
    students_table.add_rows([row for row in students if int(row[2]) > 22])
    return students_table
def rewrote_csv(students):
    with open("./data/student.csv", "w", encoding="utf-8", newline='') as fp:
        fp.truncate()
        writer = csv.writer(fp, delimiter=';')
        writer.writerow(['№', 'ФИО', 'Возраст', 'Группа'])
        writer.writerows(students)
def lab5_3():
    students_table = PrettyTable()
    students = []; groups = []
    with open("./data/student.csv", "r", encoding='utf-8') as csvfile:
        student_reader = csv.reader(csvfile, delimiter=';')
        for row in student_reader:
            groups.append(row[3])
            students.append(row)
    students_table.field_names = students[0]
    del groups[0]
    groups = set(groups)
    del students[0]
    print("Список групп: " + ', '.join(groups))
    group_choice = input('Студентов какой группы вы хотите выбрать: ')
    for row in students:
        if row[3] == group_choice:
            row[2] = int(row[2]) - 1
        students_table.add_row(row)
    user_choice = input("Хотите ли вы сохранить изменения в .csv файле: [Y]-Да, [N]-Нет\n\t> ")
    if user_choice == 'N':
        return students_table
    else:
        rewrote_csv(students)
        return students_table


# ! Седьмой вариант
def lab7_1():
    counter = 0; new_counter = 0
    
    some_dict = {
        '1': '123',
        2: '12134',
        '3': [
            '111',
            {
                11: 'afxcz',
                '12': 123
            },
            {
                13: 12323,
                '14': {
                    15: 123,
                    '16': 12345,
                },
            }
        ],
        '4': {
            '5': 123,
            6: '567',
        },
        '7': 25257,
        '8': {
            '9': 123,
            10: '567',
        },
    }
    
    def parseList(listName, new_counter):
        for j in listName:
            if type(j) == dict:
                newDict = j
                new_counter += parseDict(newDict, counter)
        return new_counter
    def parseDict(dictName, counter):
        dictKeys = list(dictName.keys())
        counter += len(dictKeys)
        for i in range(len(dictName)):
            if type(dictName.get(dictKeys[i])) == dict:
                newDict = dictName.get(dictKeys[i])
                counter = parseDict(newDict, counter)
            if type(dictName.get(dictKeys[i])) == list:
                listName = dictName.get(dictKeys[i])
                counter += parseList(listName, new_counter)
        return counter + new_counter
    
    return parseDict(some_dict, counter)
def lab7_2():
    students_table = PrettyTable()
    students = {}

    with open("./data/student.csv", "r", encoding='utf-8') as csvfile:
        student_reader = csv.reader(csvfile, delimiter=';')
        for row in student_reader:
            students[row[0]] = row[1:]

    students_table.field_names = students.get('№')
    del students['№']
    students_table.add_rows([students.get(key) for key in list(
        students.keys()) if int(students.get(key)[1]) > 22])
    
    return students_table
def lab7_3():
    students_table = PrettyTable()
    students = {}; row = []

    with open("./data/student.csv", "r", encoding='utf-8') as csvfile:
        student_reader = csv.reader(csvfile, delimiter=';')
        for row in student_reader:
            students[row[0]] = row[1:]

    students_table.field_names = students.get('№')
    del students['№']

    for key in list(students.keys()):
        student = students.get(key)
        age = int(student[1]) - 1
        student[1] = str(age)
        students[key] = student

    students_table.add_rows(students.values())

    choice = input("Хотите ли вы сохранить изменения в .csv файле: [Y]-Да, [N]-Нет\t")
    if choice == 'N':
        return students_table
    else:
        with open("./data/student.csv", "w", encoding="utf-8", newline='') as fp:
            fp.truncate()
            writer = csv.writer(fp, delimiter=';')
            writer.writerow(['№', 'ФИО', 'Возраст', 'Группа'])
            for i in students.items():
                row = list(i[0]) + i[1]
                writer.writerow(row)
                row.clear()
        return students_table

def all_labs(key):
    labs = {
        '1': lab1_1, '2': lab1_2, '3': lab1_3, '4': lab1_4,
        '5': lab2_1, '6': lab2_2, '7': lab2_3, '8': lab2_4,
        '9': lab3_1, '10': lab3_2, '11': lab3_3, '12': lab3_4,
        '13': lab4_1, '14': lab4_2, '15': lab4_3, '16': lab4_4,
        '17': lab5_1, '18': lab5_2, '19': lab5_3,
        '20': lab7_1, '21': lab7_2, '22': lab7_3,
    }
    return labs.get(key)()
