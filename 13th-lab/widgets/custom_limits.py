import PySimpleGUI as sg


def change_limits(limits):
    layout = [
        [sg.Text('Первый лимит:', size=(15, 2)), sg.InputText()],
        [sg.Text('Второй лимит:', size=(15, 2)), sg.InputText()],
        [sg.Submit(), sg.Cancel()]
    ]
    
    window = sg.Window('Информация', layout)
    
    while True:
        event, values = window.read()
        if event in [sg.WIN_CLOSED, '-EXIT-'] : break
        elif event == 'Submit':
            limits[0] = int(values[0])
            limits[1] = int(values[1])
            break

    window.close()
    return limits


def customer_table(customers, limits):
    
    def __sorted(data) : return sorted(data, key=lambda x: x[0])
    
    def __get_data(customers):
        data = []
        for item in customers:
            item = item.get_data()
            if item[-2] in range(limits[0], limits[1]):
                data.append(item)
        
        data = __sorted(data)
        return data
        
        
    sg.theme('DarkPurple6')
    layout = [
        [
            sg.Table(
                values=__get_data(customers),
                headings=['Фамилия', 'Имя', 'Отчество', 'Адрес', 'Номер карточки', 'Номер счета'],
                justification='l',
                num_rows=20,
                key='-TABLE-',
                row_height=35,
                auto_size_columns=False,
                col_widths=[10, 10, 10, 20, 12, 12],
            )
        ],
        [sg.Button('Выход', key='-EXIT-', size=(84, 2))]
    ]
    
    window = sg.Window('Информация', layout)
    
    while True:
        event, values = window.read()
        if event in [sg.WIN_CLOSED, '-EXIT-'] : break

    window.close()
