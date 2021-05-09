import csv
import PySimpleGUI as sg


students_list, counter = [], 0
with open('./assets/students.csv', 'r', encoding='utf-8') as csv_file:
    students_reader = csv.reader(csv_file, delimiter=';')
    for row in students_reader:
        students_list.append(row)


def save_data_CSV(students_list):
    with open("./assets/students.csv", "w", encoding="utf-8", newline='') as fp:
        fp.truncate()
        writer = csv.writer(fp, delimiter=';')
        writer.writerows(students_list)
    sg.Popup('Данные успешно сохранены!', title='')


def delete_student():
    tableData = window.Element('-TABLE-').get()
    key = sg.popup_get_text(
        'Введите номер студента, которого хотите удалить', title=' ')
    for row in tableData:
        if row[0] == key:
            tableData.remove(row)
            break
    window.Element('-TABLE-').Update(values=tableData)


def add_new_student():
    tableData = window.Element('-TABLE-').get()
    keys, student = [], []
    for row in tableData:
        keys.append(row[0])
    while True:
        check = 0
        student.append(sg.popup_get_text('Введите номер студента:', title=' '))
        if student[0] in keys:
            sg.popup('Такой ключ уже есть! Введите другой.', title=' ')
            student.clear()
            continue
        student.append(sg.popup_get_text('Введите ФИО студента:', title=' '))
        student.append(sg.popup_get_text(
            'Введите возраст студента:', title=' '))
        student.append(sg.popup_get_text(
            'Введите группу студента:', title=' '))
        for item in student:
            if item == '':
                sg.popup('Вы ввели не все данные! Попробуйте ещё раз.', title=' ')
                check += 1; student.clear()
                break
        if check != 0:
            continue
        else:
            break
    tableData.append(student)
    window.Element('-TABLE-').Update(values=tableData)


def show_student():
    tableData = window.Element('-TABLE-').get()
    key = sg.popup_get_text(
        'Введите номер студента, которого хотите посмотреть', title=' ')
    for row in tableData:
        if row[0] == key:
            text = f'Номер студента: {row[0]}\nФИО студента: {row[1]}\nВозраст студента: {row[2]}\nГруппа студента: {row[-1]}'
            sg.popup(text, title=' ')


def change_data():
    tableData = window.Element('-TABLE-').get()
    keys = []
    key = sg.popup_get_text(
        'Введите номер студента, которого хотите изменить', title=' ')
    for row in tableData:
        keys.append(row[0])
    for counter in range(0, len(tableData)):
        if tableData[counter][0] == key:
            break

    while True:
        key = sg.popup_get_text(f'{key}  Введите номер студента:', title=' ')
        if key in keys:
            sg.popup('Такой ключ уже есть! Введите другой.', title=' ')
            continue
        tableData[counter][0] = key
        tableData[counter][1] = sg.popup_get_text(
            'Введите ФИО студента:', title=' ')
        tableData[counter][2] = sg.popup_get_text(
            'Введите возраст студента:', title=' ')
        tableData[counter][3] = sg.popup_get_text(
            'Введите группу студента:', title=' ')
        break
    window.Element('-TABLE-').Update(values=tableData)

sg.theme('DarkPurple6')

funcs_column = [
	[sg.Button('Добавить нового студента', size=(30, 9), key='-ADD-', border_width=5)],
	[sg.Button('Изменение всех данных студента', size=(30, 9), key='-CHANGE-', border_width=5)],
	[sg.Button('Удаление студента', size=(30, 9), key='-DELETE-', border_width=5)],
	[sg.Button('Вывести информацию об студенте', size=(30, 9), key='-SHOW-', border_width=5)],
    [
        sg.Button('Сохранить внесенные данные', key='-SAVE-'),
        sg.Button('Выход', key='-EXIT-'),
    ],
]

students_table = [[sg.Table(
    values=students_list[1:],
    headings=students_list[0],
    justification='center',
    num_rows=20,
    key='-TABLE-',
    row_height=35,
    auto_size_columns=False,
    col_widths=[5, 25, 7, 10],
    size=(250, 250)
)]]

layout = [
    [
        sg.Column(students_table),
        sg.Column(funcs_column)
    ],
]


window = sg.Window('Cyberpuk 2077',
                    layout,
                    element_justification='r',
                    alpha_channel=.9,)

while True:
    event, values = window.read()
    if event in [sg.WIN_CLOSED, '-EXIT-']:
        break
    elif event == '-SAVE-':
        save_data_CSV(students_list)
    elif event == '-DELETE-':
        delete_student()
    elif event == '-ADD-':
        add_new_student()
    elif event == '-SHOW-':
        show_student()
    elif event == '-CHANGE-':
        change_data()


window.close()
