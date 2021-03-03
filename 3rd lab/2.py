yourChoice = int(input("Какой вариант вы хотите выбрать (1 / 2 / 3 / 4): "))

def options(yourChoice):
    my_string = 'Ф;И;О;Возраст;Категория;_Иванов;Иван;Иванович;23 года;Студент 3 курса;_Петров;Семен;Игоревич;22 года;Студент 2 курса'
    my_string = my_string.replace('_', '')
    my_string = list(my_string.split(';'))
    if yourChoice == 1:
        print('{0}\t\t\t{1}\t{2}'.format(''.join(my_string[:3]), my_string[4], my_string[3]))
        print('{0}\t{1}\t{2}'.format(' '.join(my_string[5:8]), my_string[9], my_string[8]))
        print('{0}\t{1}\t{2}'.format(' '.join(my_string[10:13]), my_string[14], my_string[13]))
    if yourChoice == 2:
        print('{0}\t\t\t{1}\t{2}'.format(''.join(my_string[:3]), my_string[3], my_string[4]))
        print('{0}\t{1}\t{2}'.format(' '.join(my_string[5:8]), my_string[8], my_string[9]))
        print('{0}\t{1}\t{2}'.format(' '.join(my_string[10:13]), my_string[13], my_string[14]))
    if yourChoice == 3:
        print('{0}\t\t\tО студенте'.format('\t'.join(my_string[:3])))
        print('{0}\t{1}'.format('\t'.join(my_string[5:8]), ', '.join(my_string[9:7:-1])))
        print('{0}\t{1}'.format('\t'.join(my_string[10:13]), ', '.join(my_string[:-3:-1])))
    if yourChoice == 4:
        print('{0}\t\t\tО студенте'.format(''.join(my_string[:3])))
        print('{0}\t{1}'.format(' '.join(my_string[5:8]), ', '.join(my_string[9:7:-1])))
        print('{0}\t{1}'.format(' '.join(my_string[10:13]), ', '.join(my_string[:-3:-1])))

options(yourChoice)