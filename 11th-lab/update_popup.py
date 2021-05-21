import PySimpleGUI as sg


title = 'Изменение данных в таблицах'


def update_products():

    key = sg.popup_get_text('Введите ключ')

    layout = [
        [sg.Text('Название:', size=(10, 1)), sg.InputText()],
        [sg.Text('Цена:', size=(10, 1)), sg.InputText()],
        [sg.Text('ID типа:', size=(10, 1)), sg.InputText()],
        [sg.Text('Наличие (1/2):', size=(10, 1)), sg.InputText()],
        [sg.Text('ID цвета:', size=(10, 1)), sg.InputText()],
        [sg.Submit(), sg.Cancel()],
    ]

    window = sg.Window(title, layout)
    event, values = window.read()
    window.close()

    if event == 'Submit':
        row = [values[item] for item in values]
        row = tuple([row[0], int(row[1]), int(row[2]), int(row[3]), int(row[4]), int(key)])
        return row


def update_types():
    
    key = int(sg.popup_get_text('Введите ключ'))

    layout = [
        [sg.Text('Новое значение:', size=(10, 1)), sg.InputText()],
        [sg.Submit(), sg.Cancel()],
    ]

    window = sg.Window(title, layout)
    event, values = window.read()
    window.close()

    if event == 'Submit' : return tuple(values[0], key)


def update_colors():
    
    key = int(sg.popup_get_text('Введите ключ'))

    layout = [
        [sg.Text('Новое значение:', size=(10, 1)), sg.InputText()],
        [sg.Submit(), sg.Cancel()],
    ]

    window = sg.Window(title, layout)
    event, values = window.read()
    window.close()

    if event == 'Submit' : return tuple(values[0], key)



def update_popup():
    layout = [
        [sg.Text('Из какой таблицы вы хотите удалить', size=(50, 2))],
        [
            sg.Button('Продукты', key='-PRODUCTS-', size=(15, 5)),
            sg.Button('Типы', key='-TYPES-', size=(15, 5)),
            sg.Button('Цвета', key='-COLORS-', size=(15, 5)),
        ],
        [sg.Button('Назад', key='-EXIT-', size=(50, 2))]
    ]

    window = sg.Window(title, layout); querry = None

    while True:
        event, value = window.read()
        if event in [sg.WIN_CLOSED, '-EXIT-']:
            break
        elif event == '-PRODUCTS-':
            values = update_products()
            querry = """ UPDATE products 
                            SET product_name = ?,
                            price = ?,
                            type_id = ?,
                            availability = ?,
                            color_id = ? 
                        WHERE product_id = ? """, values
            break
        elif event == '-TYPES-':
            values = update_types()
            querry = """ UPDATE types
                            SET type_name = ?
                        WHERE type_id = ? """, values
            break
        elif event == '-COLORS-':
            values = update_colors()
            querry = """ UPDATE types
                            SET color_name = ?
                        WHERE color_id = ? """, values
            break
    
    window.close()
    if querry != None:
        return querry