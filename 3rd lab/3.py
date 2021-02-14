yourChoice = int(input("Какой вариант вы хотите выбрать (1 / 2 / 3 / 4): "))

def options(yourChoice):
    my_string = 'ФИО;Возраст;Категория;_Иванов Иван Иванович;23 года;Студент 3 курса;_Петров Семен Игоревич;22 года;Студент 2 курса;_Иванов Семен Игоревич;22 года;Студент 2 курса;_Акибов Ярослав Наумович;23 года;Студент 3 курса;_Борков Станислав Максимович;21 год;Студент 1 курса;_Петров Семен Семенович;21 год;Студент 1 курса;_Романов Станислав Андреевич;23 года;Студент 3 курса;_Петров Всеволод Борисович;21 год;Студент 2 курса'.split(';')
    number_of_students = (len(my_string) - 3) / 3; id = 0
    if yourChoice == 1:
        for i in my_string:
            if i[0:7] == '_Петров':
                full_name = i.replace('_', '')
                print('{0} {1} {2}'.format(full_name, my_string[id + 1], my_string[id + 2]))
            id += 1
    if yourChoice == 2:
        for i in my_string:
            if i[0:2] == '21':
                full_name = my_string[id - 1].replace('_', '')
                print('{0} {1} {2}'.format(full_name, my_string[id], my_string[id + 1]))
            id += 1
    if yourChoice == 3:
        for i in my_string:
            if i[-4:] == 'года':
                if int(i[:2]) > 21:
                    full_name = my_string[id - 1].replace('_', '')
                    print('{0} {1} {2}'.format(full_name, my_string[id], my_string[id + 1]))
            id += 1
    if yourChoice == 4:
        for i in my_string:
            if i[0:2] == '_A' or i[0:2] == '_Б':
                full_name = i.replace('_', '')
                print('{0} {1} {2}'.format(full_name, my_string[id + 1], my_string[id + 2]))
            id += 1

options(yourChoice)