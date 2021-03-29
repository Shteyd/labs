import re
from prettytable import PrettyTable

yourChoice = int(input("Какой вариант вы хотите выбрать (1 / 2 / 3 / 4): "))

def options(yourChoice):
    my_string = 'ФИО;Возраст;Категория;_Иванов Иван Иванович;23 года;Студент 3 курса;_Петров Семен Игоревич;22 года;Студент 2 курса;_Иванов Семен Игоревич;22 года;Студент 2 курса;_Акибов Ярослав Наумович;23 года;Студент 3 курса;_Борков Станислав Максимович;21 год;Студент 1 курса;_Петров Семен Семенович;21 год;Студент 1 курса;_Романов Станислав Андреевич;23 года;Студент 3 курса;_Петров Всеволод Борисович;21 год;Студент 2 курса'.split(';_')
    students_table = PrettyTable()
    for_fields_name = my_string[0].split(';')
    students_table.field_names = [for_fields_name[i] for i in range(3)]

    if yourChoice == 1:
        for student in my_string:
            if re.findall(r"Петров", student) != []:
                students_table.add_row(student.split(';'))
        return students_table
    
    if yourChoice == 2:
        for student in my_string:
            if re.findall(r"21\s", student) == ['21 ']:
                students_table.add_row(student.split(';'))
        return students_table

    if yourChoice == 3:
        for student in my_string:
            number = re.findall(r"\d\d", student)
            number = int(*number)
            if number > 21:
                students_table.add_row(student.split(';'))
        return students_table

    if yourChoice == 4:
        for student in my_string:
            if re.findall(r"^[АБ]\w+", student) != []:
                students_table.add_row(student.split(';'))
        return students_table

print(options(yourChoice))
