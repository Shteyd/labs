import PySimpleGUI as sg


title = 'Обновление таблиц'


def add_product():

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
        return tuple([values[0], int(values[1]), int(values[2]), int(values[3]), int(values[4])])


def add_type():

    layout = [
        [sg.Text('Название типа:', size=(15, 1)), sg.InputText()],
        [sg.Submit(), sg.Cancel()],
    ]

    window = sg.Window('Обновление таблиц', layout)
    event, values = window.read()
    window.close()

    if event == 'Submit':
        return tuple([values[0]])


def add_color():

    layout = [
        [sg.Text('Цвет:', size=(10, 1)), sg.InputText()],
        [sg.Submit(), sg.Cancel()],
    ]

    window = sg.Window('Обновление таблиц', layout)
    event, values = window.read()
    window.close()

    if event == 'Submit':
        return tuple([values[0]])



def add_popup():
    layout = [
        [
            sg.Button('Продукты', key='-PRODUCTS-', size=(15, 5)),
            sg.Button('Типы', key='-TYPES-', size=(15, 5)),
            sg.Button('Цвета', key='-COLORS-', size=(15, 5)),
        ],
        [sg.Button('Назад', key='-EXIT-', size=(50, 2))]
    ]

    window = sg.Window('Обновление таблиц', layout); querry = None

    while True:
        event, value = window.read()
        if event in [sg.WIN_CLOSED, '-EXIT-']:
            break
        elif event == '-PRODUCTS-':
            values = add_product()
            querry = """ INSERT INTO products (product_name, price, type_id, availability, color_id) VALUES(?, ?, ?, ?, ?) """, values
            break
        elif event == '-TYPES-':
            values = add_type()
            querry = """ INSERT INTO types (type_name) VALUES(?) """, values
            break
        elif event == '-COLORS-':
            values = add_color()
            querry = """ INSERT INTO colors (color_name) VALUES(?) """, values
            break
    
    window.close()
    if querry != None:
        return querry
