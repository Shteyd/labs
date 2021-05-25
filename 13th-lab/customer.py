from widgets.custom_limits import change_limits, customer_table
import PySimpleGUI as sg


def customer():
    sg.theme('DarkPurple6')
    class Customer(object):
        def __init__(self, arg):
            self.first_name = arg[0]
            self.second_name = arg[1]
            self.thrid_name = arg[2]
            self.adress = arg[3]
            self.card_number = arg[4]
            self.bank_number = arg[5]
        
        def get_data(self) : return self.first_name, self.second_name, self.thrid_name, self.adress, self.card_number, self.bank_number


    customers = [
        Customer(['Петров', 'Игорь', 'Михайлович', 'ул. Большая Садовая 28', 9807, 408867]),
        Customer(['Сидоров', 'Михаил', 'Евгеньевич', 'ул. Большая Садовая 56', 2284, 562282]),
        Customer(['Баширов', 'Игорь', 'Васильевич', 'Ворошиловский пр. 18', 4950, 759989]),
        Customer(['Иванов', 'Иван', 'Иванович', 'ул. Красноармейская 56', 8416, 333050]),
        Customer(['Петренко', 'Даниил', 'Михайлович', 'Буденовский пр. 14', 9037, 797374]),
    ]; limits = [1000, 10000]


    layout = [
        [sg.Button('Список всех покупателей', key='-DATA-', size=(32, 2))],
        [sg.Button('Задать диапазон', key='-UPDATE-', size=(32, 2))],
        [sg.Button('Выход', key='-EXIT-', size=(32, 2))],
    ]


    window = sg.Window(' ', layout)


    while True:
        event, values = window.read()
        if event in [sg.WIN_CLOSED, '-EXIT-'] : break
        elif event == '-DATA-' : customer_table(customers, limits)
        elif event == '-UPDATE-' : limits = change_limits(limits)

    window.close()
