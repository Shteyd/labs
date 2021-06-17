import PySimpleGUI as sg


def four_or_five(students, key):
    
    data = []
    for item in students:
        item = item.get_data()
        if item[-1] == key : data.append([item[0], item[1], f'{item[-1]:.3}'])
    
    if data == [] : return sg.popup('Таких учеников нет!')
    
    layout = [
        [
            sg.Table(
                values=data,
                headings=['Студент', 'Группа', 'Ср. оценка'],
                justification='l',
                num_rows=10,
                key='-TABLE-',
                row_height=35,
                auto_size_columns=False,
                col_widths=[25, 10, 10],
            )
        ],
        [sg.Button('Выход', key='-EXIT-', size=(52, 2))]
    ]
    
    window = sg.Window('Студенты', layout)
    
    while True:
        event, values = window.read()
        if event in [sg.WIN_CLOSED, '-EXIT-']:
            break

    window.close()
