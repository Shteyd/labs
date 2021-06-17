import PySimpleGUI as sg


def __get_data(key, clsobj):
    data = []
    if key == 1:
        for item in clsobj:
            item = item.get_data()
            data.append([item[0], item[1], f'{item[-1]:.3}'])
    elif key == 2:
        for item in clsobj:
            data.append(list(item.get_data()))
        data = sorted(data, key=lambda x: x[0])
    else:
        number = sg.popup_get_text('Введите номер поезда')
        for item in clsobj:
            item = item.get_data()
            if item[1] == number:
                data.append(list(item))
    
    return data


def print_table(key, clsobj, fields):
    
    data = __get_data(key, clsobj)
    
    layout = [
        [
            sg.Table(
                values=data,
                headings=fields,
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
    
    window = sg.Window('Информация', layout)
    
    while True:
        event, values = window.read()
        if event in [sg.WIN_CLOSED, '-EXIT-']:
            break

    window.close()
