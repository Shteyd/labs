import csv
from prettytable import PrettyTable


yourChoice = int(input("Какой вариант вы хотите выбрать (1 / 2 / 3 / 4): "))
students_table = PrettyTable()
students = []

with open("./data/student.csv", "r", encoding='utf-8') as csvfile:
    student_reader = csv.reader(csvfile, delimiter=';')
    for row in student_reader:
        students.append(row)

students_table.field_names = students[0]
del students[0]

sorted_students = {
    1: sorted(students, key=lambda person: person[1]),
    2: sorted(students, key=lambda person: person[2]),
    3: sorted(students, key=lambda person: person[3]),
    4: [row for row in students if int(row[2]) > 22],
}
students_table.add_rows(sorted_students[yourChoice])

print('\n\tИнформация о студентах: ')
print(students_table)
