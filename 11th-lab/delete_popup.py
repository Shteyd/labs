import PySimpleGUI as sg


title = 'Удаление из таблицы'


def get_key() : return int(sg.popup_get_text('Введите ключ'))


def delete_popup():
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
            querry = """ DELETE FROM products WHERE product_id = ? """, tuple([get_key()])
            break
        elif event == '-TYPES-':
            querry = """ DELETE FROM types WHERE type_id = ? """, tuple([get_key()])
            break
        elif event == '-COLORS-':
            querry = """ DELETE FROM colors WHERE color_id = ? """, tuple([get_key()])
            break
    
    window.close()
    if querry != None:
        return querry