import csv
from prettytable import PrettyTable


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
    print(students_table)
else:
    with open("./data/student.csv", "w", encoding="utf-8", newline='') as fp:
        fp.truncate()
        writer = csv.writer(fp, delimiter=';')
        writer.writerow(['№', 'ФИО', 'Возраст', 'Группа'])
        for i in students.items():
            row = list(i[0]) + i[1]
            writer.writerow(row)
            row.clear()
    print(students_table)
