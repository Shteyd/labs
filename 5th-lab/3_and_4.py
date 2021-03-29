import csv
from prettytable import PrettyTable


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

print(
'''
    Что вы хотите сделать?
    1 - Увеличить возраст всех студентов на 1.
    2 - Уменьшить возраст всех студентов на 1.
    3 - Увеличить возраст студентов в заданной пользователем группе на 1.
    4 - Уменьшить возраст студентов в заданной пользователем группе на 1.
'''); yourChoice = int(input("Ваш выбор: "))

if yourChoice == 1:
    for row in students:
        row[2] = int(row[2]) + 1
        students_table.add_row(row)
if yourChoice == 2:
    for row in students:
        row[2] = int(row[2]) - 1
        students_table.add_row(row)
if yourChoice == 3:
    print("Список групп: " + ', '.join(groups))
    group_choice = input('Студентов какой группы вы хотите выбрать: ')
    for row in students:
        if row[3] == group_choice:
            row[2] = int(row[2]) + 1
        students_table.add_row(row)

if yourChoice == 4:
    print("Список групп: " + ', '.join(groups))
    group_choice = input('Студентов какой группы вы хотите выбрать: ')
    for row in students:
        if row[3] == group_choice:
            row[2] = int(row[2]) - 1
        students_table.add_row(row)

# ! Ниже приведено решение задания №4

yourChoice = input("Хотите ли вы сохранить изменения в .csv файле: [Y]-Да, [N]-Нет\t")
if yourChoice == 'N':
    print(students_table)
else:
    with open("./data/student.csv", "w", encoding="utf-8", newline='') as fp:
        fp.truncate()
        writer = csv.writer(fp, delimiter=';')
        writer.writerow(['№', 'ФИО', 'Возраст', 'Группа'])
        writer.writerows(students)
    print(students_table)
