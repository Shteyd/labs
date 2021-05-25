from widgets.custom_table import print_table
import PySimpleGUI as sg


def train():
    sg.theme('DarkPurple6')
    class Train(object):
        def __init__(self, arg):
            self.name = arg[0]
            self.number = arg[1]
            self.time = arg[2]
        
        def get_data(self) : return self.name, self.number, self.time


    trains = [
        Train(['Батайск', '124', '16:30']),
        Train(['Ростов-Главный', '135', '17:05']),
        Train(['Шахты', '140', '19:10']),
        Train(['Новочеркасск', '125', '14:35']),
        Train(['Красодар-1', '341', '8:00']),
    ]


    layout = [
        [sg.Button('Список всех поездов', key='-DATA-', size=(32, 2))],
        [sg.Button('Поезд', key='-4-', size=(15, 2)), sg.Button('Сортировка', key='-SORT-', size=(15, 2))],
        [sg.Button('Выход', key='-EXIT-', size=(32, 2))],
    ]


    window = sg.Window('Позда', layout)


    while True:
        event, values = window.read()
        if event in [sg.WIN_CLOSED, '-EXIT-']:
            break
        elif event == '-DATA-':
            print_table(2, trains, ['Станция', 'Номер', 'Время'])
        elif event == '-4-':
            print_table(3, trains, ['Станция', 'Номер', 'Время'])
        elif event == '-SORT-':
            print_table(2, trains, ['Станция', 'Номер', 'Время'])


    window.close()
