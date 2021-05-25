import PySimpleGUI as sg


def __get_data(clsobj):
    data = []
    for item in clsobj:
        item = item.get_data()
        data.append(item)
    
    return data


def book_table(data):
    layout = [
        [
            sg.Table(
                values=__get_data(data),
                headings=['Автор', 'Название', 'Год'],
                justification='l',
                num_rows=20,
                key='-TABLE-',
                row_height=35,
                auto_size_columns=False,
                col_widths=[25, 25, 5],
            )
        ],
        [sg.Button('Выход', key='-EXIT-', size=(64, 2))]
    ]
    
    window = sg.Window('Информация', layout)
    
    while True:
        event, values = window.read()
        if event in [sg.WIN_CLOSED, '-EXIT-'] : break

    window.close()


def add_book():
    layout = [
        [sg.Text('Автор', size=(10, 2)), sg.InputText()],
        [sg.Text('Название', size=(10, 2)), sg.InputText()],
        [sg.Text('Год', size=(10, 2)), sg.InputText()],
        [sg.Submit(), sg.Cancel()],
    ]
    
    window = sg.Window(' ', layout)
    
    while True:
        event, values = window.read()
        if event in [sg.WIN_CLOSED, '-EXIT-'] : break
        elif event == 'Submit':
            break

    window.close()
    return values

def sorted_table(data):
    
    def __sorted():
        layout = [
            [sg.Text('Список полей для сортировки', size=(32, 2))],
            [sg.Button('Автор ', key='WRITER', size=(32, 2))],
            [sg.Button('Название книги', key='NAME', size=(32, 2))],
            [sg.Button('Год', key='YEAR', size=(32, 2))],
        ]

        window = sg.Window(' ', layout)

        while True:
            event, values = window.read()
            if event in [sg.WIN_CLOSED, '-EXIT-'] : break
            else : break

        window.close()
        return event
        
    choice = __sorted()
    data = __get_data(data)
    
    if choice == 'WRITER':
        data = sorted(data, key=lambda x: x[0])
    elif choice == 'NAME':
        data = sorted(data, key=lambda x: x[1])
    elif choice == 'YEAR':
        data = sorted(data, key=lambda x: x[2])

    
    layout = [
        [
            sg.Table(
                values=data,
                headings=['Автор', 'Название', 'Год'],
                justification='l',
                num_rows=20,
                key='-TABLE-',
                row_height=35,
                auto_size_columns=False,
                col_widths=[25, 25, 5],
            )
        ],
        [sg.Button('Выход', key='-EXIT-', size=(64, 2))]
    ]
    
    window = sg.Window('Информация', layout)
    
    while True:
        event, values = window.read()
        if event in [sg.WIN_CLOSED, '-EXIT-'] : break

    window.close()
