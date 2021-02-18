yourChoice = int(input("Какой вариант вы хотите выбрать (1 / 2 / 3 / 4): "))

def options(yourChoice):
    my_len = [['БО-331101',['Акулова Алена', 'Бабушкина Ксения']],['БОВ-421102', ['Пупкин Вася', 'Петров Андрей']],['БО-331103', ['Береговский Илья', 'Курдус Аким']]]; id = 0
    if yourChoice == 1:
        for i in range(len(my_len)):
            for j in my_len[i][1]:
                if j[:1] == 'А':
                    print("{0}:\t{1}".format(my_len[i][0], j))
    if yourChoice == 2:
        for i in range(len(my_len)):
            for j in my_len[i][1]:
                some_name = j.split()
                if len(some_name[0]) <= 7:
                    print("{0}:\t{1}".format(my_len[i][0], j))
    if yourChoice == 3:
        for i in range(len(my_len)):
            for j in my_len[i][1]:
                some_name = j.split()
                if some_name[0][:1] == 'П':
                    if some_name[1][:1] == 'А':
                        print("{0}:\t{1}".format(my_len[i][0], j))
    if yourChoice == 4:
        for i in range(len(my_len)):
            id = 0
            for j in my_len[i][1]:
                if id % 2 == 0:
                    print("{0}:\t{1}".format(my_len[i][0], j))
                id += 1


options(yourChoice)