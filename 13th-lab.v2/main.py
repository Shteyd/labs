import re
import csv
import PySimpleGUI as sg
from string import punctuation
from abc import ABC, abstractmethod


sg.theme('DarkPurple6')


class Animals(ABC):
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
    
    @abstractmethod
    def food_count(self) : pass

    @abstractmethod
    def food_type(self) : pass
    
    @abstractmethod
    def animal_type(self) : pass
    
    def data(self) : return [self.animal_type(), self.name, self.food_type(), f'{self.food_count():.3}']


class Predator(Animals):
    def food_type(self) : return 'Мясо'
    def food_count(self) : return self.weight / 19
    def animal_type(self) : return 'Хищник'


class Herbivores(Animals):
    def food_type(self) : return 'Трава'
    def food_count(self) : return self.weight / 23
    def animal_type(self) : return 'Травоядный'


class Omnivores(Animals):
    def food_type(self) : return 'Всё'
    def food_count(self) : return self.weight / 25
    def animal_type(self) : return 'Всеядный'


data = []
with open("./data/animals.csv", "r", encoding='utf-8') as csvfile:
    student_reader = csv.reader(csvfile, delimiter=';')
    for row in student_reader:
        if row[-1] == 'хищник' : data.append(Predator(row[0], int(row[1])))
        elif row[-1] == 'травоядный' : data.append(Herbivores(row[0], int(row[1])))
        elif row[-1] == 'всеядный' : data.append(Omnivores(row[0], int(row[1])))


def add_animal():
    def __add():
        layout = [
            [sg.Text('Класс:', size=(10, 1)), sg.InputText()],
            [sg.Text('Имя:', size=(10, 1)), sg.InputText()],
            [sg.Text('Вес:', size=(10, 1)), sg.InputText()],
            [sg.Yes(), sg.Cancel()],
        ]

        window = sg.Window('', layout)
        event, values = window.read()
        window.close()
        if event == 'Cancel' or values[2].isdigit() == False : return
        elif event == 'Yes' : return [values[0].lower(), values[1], int(values[2])]
    
    animal = __add()
    
    if animal == None : return
    elif animal[0] == 'хищник' : data.append(Predator(animal[1], int(animal[-1])))
    elif animal[0] == 'всеядный' : data.append(Herbivores(animal[1], int(animal[-1])))
    elif animal[0] == 'травоядный' : data.append(Omnivores(animal[1], int(animal[-1])))
    
    window.Element('-TABLE-').Update(get_data(data))


def get_data(data):
    table_data = []
    for item in data:
        table_data.append(item.data())
    return table_data


def sorted_data():
    def __sorted():
        layout = [
            [sg.Button('Тип', key=0, size=(15, 7)), sg.Button('Имя', key=1, size=(15, 7))],
            [sg.Button('Еда', key=2, size=(15, 7)), sg.Button('Количество', key=3, size=(15, 7))],
        ]

        window = sg.Window('', layout, no_titlebar=True)

        event = window.read()
        window.close()

        return event[0]
    
    count = __sorted()
    table_data = sorted(get_data(data), key=lambda x: x[count])
    window.Element('-TABLE-').update(table_data)
    
    return table_data


def save_in_csv(data):
    folderpath = sg.popup_get_folder('Перейдите в нужную директорию:')

    if folderpath == None : return

    filename = sg.popup_get_text('Введите название для .csv файла (по умолчанию animals_data)\np.s.: Так же нельзя использовать спец. символы!')
    if len(re.findall(f"[{punctuation}]", filename)) != 0 : return sg.popup('Введены спец. символы!')

    if filename == None : return
    if filename == '' : filename = 'animals_data'
    if folderpath == '' : folderpath = './data'

    with open(f"{folderpath}/{filename}.csv", "w", encoding="utf-8", newline='') as csv_file:
        csv_file.truncate()
        writer = csv.writer(csv_file, delimiter=';')
        for item in data:
            writer.writerow(item.data())


left_column = [
	[sg.Button('Добавить новое животное', size=(25, 11), key='-ADD-', border_width=2)],
	[sg.Button('Сортировка', size=(25, 11), key='-SORT-', border_width=2)],
]

right_column = [
	[sg.Button('Вывести первые 5', size=(25, 11), key='-SHOW-5-', border_width=2)],
	[sg.Button('3 идентификатора', size=(25, 11), key='-THREE-', border_width=2)],
]

table_data = get_data(data)

animal_table = [
    [
        sg.Table(
            values=table_data,
            headings=['Тип', 'Животное', 'Тип еды', 'Сколько еды давать'],
            justification='center',
            num_rows=10,
            key='-TABLE-',
            row_height=35,
            auto_size_columns=True,
            size=(250, 250)
        )
    ]
]

layout = [
    [
        sg.Column(left_column),
        sg.Column(animal_table),
        sg.Column(right_column)
    ],
    [sg.Button('Вывести всех', key='-ALL-', size=(120, 3))],
    [
        sg.Button('Сохранить внесенные данные', size=(59, 3), key='-SAVE-'),
        sg.Button('Выход', size=(59, 3), key='-EXIT-'),
    ],
]


window = sg.Window('13ая лаба',
                    layout,
                    element_justification='c',
                    alpha_channel=.9,)


while True:
    event, values = window.read()
    if event in [sg.WIN_CLOSED, '-EXIT-'] : break
    elif event == '-ALL-' : window.Element('-TABLE-').Update(get_data(data))
    elif event == '-SAVE-' : save_in_csv(data)
    elif event == '-SORT-' : table_data = sorted_data()
    elif event == '-ADD-' : add_animal()
    elif event == '-SHOW-5-' : window.Element('-TABLE-').Update(table_data[:5])
    elif event == '-THREE-' : window.Element('-TABLE-').Update(table_data[-3:])


window.close()
