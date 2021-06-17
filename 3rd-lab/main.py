import re
from prettytable import PrettyTable


def main():
    my_string = 'ФИО;Возраст;Категория;_Иванов Иван Иванович;23 года;Студент 3 курса;_Петров Семен Игоревич;22 года;Студент 2 курса;_Иванов Семен Игоревич;22 года;Студент 2 курса;_Акибов Ярослав Наумович;23 года;Студент 3 курса;_Борков Станислав Максимович;21 год;Студент 1 курса;_Петров Семен Семенович;21 год;Студент 1 курса;_Романов Станислав Андреевич;23 года;Студент 3 курса;_Петров Всеволод Борисович;21 год;Студент 2 курса'.split(';_')
    
    fields = {
        1: ['ФИО', 'Категория', 'Возраст'],
        2: ['ФИО', 'Возраст', 'Категория'],
        3: ['Ф', 'И', 'О', 'О студенте'],
        4: ['ФИО', 'О студенте'],
    }

    tasks = {
        1: {
            1: lambda: ' '.join(re.findall(r'\b\w{1,5}\b', user_str)),
            2: lambda: ' '.join(re.findall(r"Ли\w+", user_str)),
            3: lambda: ' '.join(re.findall(r"\w{5,10}", user_str)),
            4: lambda: ' '.join(re.findall(r"\w+ов\b", user_str)),
        },
        2: {
            1: lambda: [[i[0], i[2], i[1]] for i in my_string],
            2: lambda: my_string,
            3: lambda: [[*i[0].split(), f'{i[2]}, {i[1]}'] for i in my_string],
            4: lambda: [[i[0], f'{i[2]}, {i[1]}'] for i in my_string],
        },
        3: {
            1: lambda: [i.split(';') for i in my_string if re.findall(r'Петров', i) != []],
            2: lambda: [i.split(';') for i in my_string if re.findall(r'21\s', i) != ['21 ']],
            3: lambda: [i.split(';') for i in my_string if int(*re.findall(r'\d\d', i)) > 21],
            4: lambda: [i.split(';') for i in my_string if re.findall(r"^[АБ]\w+", i) != []],
        },
        4: {
            1: lambda: ''.join(['Символов: ', str(len(user_str)), '\nСлов: ', str(len(re.findall(r"\w+", user_str)))]),
        }
    }

    key = list(map(int, input("Выбор варианта и задания: ").split()))

    if key[0] in [1, 4]:
        user_str = input("Введите строку: ")
        result = tasks[key[0]][key[1]]()
    else:
        if key[0] == 2 : my_string = [i.split(';') for i in my_string]
        result = PrettyTable()
        result.field_names = fields[key[1]] if key == 2 else fields[2]
        result.add_rows(tasks[key[0]][key[1]]()[1:])

    print(result)

if __name__ == '__main__':
    main()
