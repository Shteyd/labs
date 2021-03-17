yourChoice = int(input("Какой вариант вы хотите выбрать (1 / 2 / 3 / 4): "))

def options(yourChoice):
    my_len = [['БО-331101',['Акулова Алена', 'Бабушкина Ксения']],['БОВ-421102', ['Пупкин Вася', 'Петров Андрей']],['БО-331103', ['Береговский Илья', 'Курдус Аким']]]
    students = ''; list_students = []
    if yourChoice == 1:
        newChoice = int(input("Какую группу вы хотите посмотреть: "))
        print(my_len[newChoice][0], ", ".join(my_len[newChoice][1]), sep=': ')
    if yourChoice == 2:
        newChoice = int(input("Какую группу вы хотите посмотреть: "))
        print('{0}:\n\t{1}'.format(my_len[newChoice][0], "\n\t".join(my_len[newChoice][1])))
    if yourChoice == 3:
        for group in my_len:
            print(group[0], '\n\t'.join(group[1]), sep=':\n\t')
    if yourChoice == 4:
        for group in my_len:
            if group[0][:3] == 'БО-':
                students = '\n\t'.join(group[1])
                list_students.append('\n\t'.join([group[0], students]))
        print('\n'.join(list_students))

options(yourChoice)