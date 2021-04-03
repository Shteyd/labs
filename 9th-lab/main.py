import csv
from time import sleep

students = {}

with open("./data/students.csv", "r", encoding='utf-8') as csvfile:
    student_reader = csv.reader(csvfile, delimiter=';')
    for row in student_reader:
        students[row[0]] = row[1:]

del students['№']

def writeCsv():
    choice = input("Хотите ли вы сохранить изменения в .csv файле: [Y]-Да, [N]-Нет\t")
    if choice != 'N':
        with open("./data/students.csv", "w", encoding="utf-8", newline='') as fp:
            fp.truncate()
            writer = csv.writer(fp, delimiter=';')
            writer.writerow(['№', 'ФИО', 'Возраст', 'Группа'])
            for i in students.items():
                row = list(i[0]) + i[1]
                writer.writerow(row)
                row.clear()

def addStudent():
    keys = list(students.keys())
    while True:
        id = input('Введите новый ID нового студента: ')
        if id in keys:
            print('Такой ID уже существует, введите другой')
            continue
        name = input('Введите ФИО нового студента: ')
        age = input('Введите возраст нового студента: ')
        group = input('Введите группу нового студента: ')
        students[id] = [name, age, group]
        break

def changeData():
    key = input('Введите ID студента: ')
    name = input('Введите новое ФИО студента: ')
    age = input('Введите новый возраст студента: ')
    group = input('Введите новую группу студента: ')
    students[key] = [name, age, group]

def deleteData():
    key = input('Введите ID студента: ')
    del students[key]

def printData():
    key = input("Введите ID студента: ")
    data = students.get(key)
    print(f'ID: {key}\nФИО: {data[0]}\nВозраст: {data[1]}\nГруппа: {data[2]}')

def funcs(key):
    allFuncs = {'1': addStudent, '2': changeData, '3': deleteData, '4': printData,}
    return allFuncs.get(key)()


print('\t\tСписок всех студентов: ')
for ID in students:
    print(f'\tID: {ID} -> Информация:', ', '.join(students.get(ID)))
while True:
    print('-+'*24)
    print('\t\tСписок команд:\n\t1 - Добавить нового студента\n\t2 - Изменить данные студента\n\t3 - Удаление студента\n\t4 - Вывести информацию о студенте')
    key = input('\nВаш выбор:\n\t> ')
    funcs(key)
    writeCsv()
    key = input('Вы хотите продолжить? [Y]-Yes [N]-No\n\t> ')
    if key == '' or key == 'N':
        print('Выход из программы...')
        for _ in range(2):
            sleep(0.5)
            print('...')
        exit()
