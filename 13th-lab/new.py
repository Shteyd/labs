from widgets.choice import new_choice
import PySimpleGUI as sg


def new():
    sg.theme('DarkPurple6')
    class NewClass(object):
        def __init__(self, first, second):
            self.first = first
            self.second = second
        
        def get_data(self) : return self.first, self.second
        
        def update_data(self):
            choice = new_choice()
            if choice is None : return
            if choice == 1:
                self.first = int(sg.popup_get_text('Введите новое значение'))
            else:
                self.second = int(sg.popup_get_text('Введите новое значение'))



    data = NewClass(0, 0)

    layout = [
        [sg.Button('Показать обе переменные', key='-DATA-', size=(32, 2))],
        [sg.Button('Изменить эти переменные', key='-UPDATE-', size=(32, 2))],
        [sg.Button('Большая переменная', key='-MAX-', size=(32, 2))],
        [sg.Button('Выход', key='-EXIT-', size=(32, 2))],
    ]


    window = sg.Window(' ', layout)


    while True:
        event, values = window.read()
        if event in [sg.WIN_CLOSED, '-EXIT-']:
            break
        elif event == '-DATA-':
            sg.popup(f'Значение первой переменной: {data.get_data()[0]}\nЗначение второй переменной: {data.get_data()[1]}')
        elif event == '-UPDATE-':
            data.update_data()
        elif event == '-MAX-':
            sg.popup(f'Большее значение: {max(data.get_data())}')


    window.close()
            