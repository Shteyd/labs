import csv
from prettytable import PrettyTable


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

print(students_table)
