import csv
from widgets.books_table import add_book, book_table, sorted_table
import PySimpleGUI as sg


def library():
    sg.theme('DarkPurple6')
    class Library(object):
        def __init__(self, arg):
            self.writer = arg[0]
            self.name = arg[1]
            self.year = arg[2]

        def get_data(self) : return self.writer, self.name, int(self.year)


    data = []; writers = []
    with open("./data/books.csv", "r", encoding='utf-8') as csvfile:
        student_reader = list(csv.reader(csvfile, delimiter=';'))
        for row in student_reader[1:]:
            if row[0] not in writers : writers.append(row[0])
            data.append(Library(row))

    layout = [
        [sg.Button('Список всех книг', key='-DATA-', size=(32, 2))],
        [sg.Button('Добавить книгу ', key='-ADD-', size=(32, 2))],
        [sg.Button('Удалить книгу', key='-DEL-', size=(32, 2))],
        [sg.Button('Сортировать книги', key='-SORT-', size=(32, 2))],
        [sg.Button('Выход', key='-EXIT-', size=(32, 2))],
    ]


    window = sg.Window(' ', layout)


    while True:
        event, values = window.read()
        if event in [sg.WIN_CLOSED, '-EXIT-'] : break
        elif event == '-DATA-' : book_table(data)
        elif event == '-ADD-':
            item = add_book()
            data.append(Library([item[0], item[1], int(item[2])]))
        elif event == '-DEL-':
            key = sg.popup_get_text('Введите название книги')
            for item in range(len(data)):
                if data[item].get_data()[1] == key:
                    del data[item]
        elif event == '-SORT-':
            sorted_table(data)

    window.close()
