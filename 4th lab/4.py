yourChoice = int(input("Какой вариант вы хотите выбрать (1 / 2 / 3 / 4): "))

def options(yourChoice):
    my_len = [['БО-331101',['Акулова Алена', 'Бабушкина Ксения']],['БОВ-421102', ['Пупкин Вася', 'Петров Андрей']],['БО-331103', ['Береговский Илья', 'Курдус Аким']]]
    students = ''; list_students = []
    if yourChoice == 1:
        for group in my_len:
            for student in group[1]:
                if student[0] == 'А':
                    print(group[0], student, sep=': ')
    if yourChoice == 2:
        for group in my_len:
            for student in group[1]:
                if len(student.split()[0]) < 7:
                    print(group[0], student, sep=': ')
    if yourChoice == 3:
        for group in my_len:
            for student in group[1]:
                if student.split()[0][0] == 'П' and student.split()[1][0] == 'А':
                    print(group[0], student, sep=': ')
    if yourChoice == 4:
        for group in my_len:
            students = ', '.join(group[1][::2])
            list_students.append(f'{group[0]}:\t{students}')
        print('\n'.join(list_students))


options(yourChoice)