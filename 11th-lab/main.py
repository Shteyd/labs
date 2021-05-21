from delete_popup import delete_popup
from update_popup import update_popup
from add_popup import add_popup
import re
import csv
import sqlite3
import string
import PySimpleGUI as sg


sg.theme('DarkPurple6')
db = sqlite3.connect('./assets/products.db')
cursor = db.cursor()


def add_data():
    querry = add_popup()
    if querry != None:
        cursor.execute(querry[0], querry[1])
        db.commit()


def update_data():
    querry = update_popup()
    if querry != None:
        cursor.execute(querry[0], querry[1])
        db.commit()


def del_data():
    querry = delete_popup()
    if querry != None:
        cursor.execute(querry[0], querry[1])
        db.commit()


def color_statistics():
    querry = """ SELECT colors.color_name FROM products INNER JOIN colors ON products.color_id = colors.color_id """
    cursor.execute(querry)

    colors = {}; colors_result = "Статистика по цветам:\n\n"
    for row in cursor.fetchall():
        if row[0] not in colors:
            colors[row[0]] = 1
        else:
            colors[row[0]] += 1
    
    for key in colors:
        colors_result += f'{key}: {colors[key]}\n'
    
    sg.Popup(colors_result, font=35)


def save_in_csv(products):
    folderpath = sg.popup_get_folder('Перейдите в нужную директорию:')

    if folderpath == None : return

    filename = sg.popup_get_text('Введите название для .csv файла (по умолчанию products)\np.s.: Так же нельзя использовать спец. символы!')

    if filename == None : return
    if filename == '' : filename = 'products'
    if folderpath == '' : folderpath = './assets'
    if len(re.findall(f"""[{string.punctuation}]""", filename)) != 0 : return sg.popup('Введены спец. символы!')
    
    with open(f"{folderpath}/{filename}.csv", "w", encoding="utf-8", newline='') as csv_file:
        csv_file.truncate()
        writer = csv.writer(csv_file, delimiter=';')
        writer.writerows(products)


def get_all_data():
    querry = """ SELECT products.product_id, product_name, price, types.type_name, existence.availability, colors.color_name FROM products INNER JOIN
                        existence ON products.availability = existence.id INNER JOIN
                        types ON products.type_id = types.type_id INNER JOIN
                        colors ON products.color_id = colors.color_id """
    cursor.execute(querry)
    products = [list(row) for row in cursor.fetchall()]
    return products

products = get_all_data()

table_column = [
    [
        sg.Table(
            values=products,
            headings=['Ключ', 'Имя', 'Цена', 'Тип', 'Наличие', 'Цвет'],
            justification='center',
            num_rows=20,
            key='-TABLE-',
            row_height=35,
            auto_size_columns=False,
            col_widths=[5, 25, 7, 10],
            size=(250, 250)
        )
    ]
]


buttons_column = [
    [sg.Button('Добавить данные', key='-ADD-', size=(30, 7))],
    [sg.Button('Изменить данные', key='-UPDATE-', size=(30, 7))],
    [sg.Button('Удалить данные', key='-DELETE-', size=(30, 7))],
    [sg.Button('Цветная статистика', key='-COLOR-', size=(30, 7))],
    [sg.Button('Сохранить в .csv', key='-CSV-', size=(30, 7))],
    [sg.Button('Выход из программы', key='-EXIT-', size=(30, 7))]
]


layout = [
    [
        sg.Column(table_column),
        sg.Column(buttons_column)
    ]

]

window = sg.Window('11ая лаба', layout)

while True:
    event, values = window.read()
    if event in [sg.WIN_CLOSED, '-EXIT-']:
        break
    elif event == '-ADD-':
        add_data()
        products = get_all_data()
        window.Element('-TABLE-').update(values=products)
    elif event == '-UPDATE-':
        update_data()
        products = get_all_data()
        window.Element('-TABLE-').update(values=products)
    elif event == '-DELETE-':
        del_data()
        products = get_all_data()
        window.Element('-TABLE-').update(values=products)
    elif event == '-CSV-':
        save_in_csv(products)
    elif event == '-COLOR-':
        color_statistics()


cursor.close()
window.close()
