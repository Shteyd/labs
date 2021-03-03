import csv
from prettytable import PrettyTable

students_table = PrettyTable()

students = []; count = 0

with open("labs/5th lab/data/student.csv", "r", encoding='utf-8') as csvfile:
    student_reader = csv.reader(csvfile, delimiter=';')
    for row in student_reader:
        if count == 0:
            count += 1
            continue
        if int(row[2]) > 22:
            students.append(row)
        
print('\n\tИнформация о студентах: ')
students_table.field_names = ["№", "ФИО", "Возраст", "Группа"]
students_table.add_rows(students)
print(students_table)