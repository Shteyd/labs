yourChoice = int(input("Какой вариант вы хотите выбрать (1 / 2 / 3 / 4): "))

def options(yourChoice):
    my_len = [['БО-331101',['Акулова Алена', 'Бабушкина Ксения']],['БОВ-421102', ['Пупкин Вася', 'Петров Андрей']],['БО-331103', ['Береговский Илья', 'Курдус Аким']]]
    if yourChoice == 1:
        newChoice = int(input("Какую группу вы хотите посмотреть: "))
        print('{0}:\n\t{1}'.format(my_len[newChoice][0], "\n\t".join(my_len[newChoice][1])))
    if yourChoice == 2:
        for i in range(len(my_len)):
            print('{0}: {1}'.format(my_len[i][0], ", ".join(my_len[i][1])))
    if yourChoice == 3:
        for i in range(len(my_len)):
            print(my_len[i][0])
            for j in my_len[i][1]:
                print("".join(j))
    if yourChoice == 4:
        for i in range(len(my_len)):
            for j in my_len[i]:
                if my_len[i][0][:3] == 'БО-':
                    print('{0}:\n\t{1}'.format(my_len[i][0], "\n\t".join(my_len[i][1])))

options(yourChoice)