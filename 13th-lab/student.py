from widgets.students_four_or_five import four_or_five
from widgets.custom_table import print_table
import PySimpleGUI as sg


def student():
    sg.theme('DarkPurple6')
    class Student(object):
        def __init__(self, arg):

            def __getAverage(marks):
                if marks == [0] * 5 : return 0
                else : return (marks[0] * 1 + marks[1] * 2 + marks[2] * 3 + marks[3] * 4 + marks[4] * 5) / sum(marks)

            self.name = arg[0]
            self.group = arg[1]
            self.mark = arg[2]
            self.average = __getAverage(arg[2])

        
        def get_data(self) : return self.name, self.group, self.mark, self.average


    students = [
        Student(('Аргишев Тимур', 'ВКБ13', [0, 0, 1, 2, 3])),
        Student(('Беляков Ефим', 'ВКБ13', [0, 0, 2, 3, 1])),
        Student(('Боруля Максим', 'ВКБ13', [0, 1, 4, 1, 0])),
        Student(('Курдус Аким', 'ВКБ13', [0, 0, 0, 3, 0])),
        Student(('Ивахненко Юлия', 'ВКБ13', [1, 0, 0, 2, 4])),
        Student(('Калитурина Яна', 'ВКБ13', [0, 0, 0, 1, 3])),
        Student(('Журилко Григорий', 'ВКБ13', [0, 0, 0, 8, 0])),
        Student(('Малышев Владислав', 'ВКБ13', [0, 0, 0, 0, 7])),
        Student(('Петренко Даниил', 'ВКБ13', [0, 2, 0, 4, 1])),
        Student(('Шепило Алина', 'ВКБ13', [0, 0, 0, 4, 0])),
    ]


    layout = [
        [sg.Button('Список всех студентов', key='-DATA-', size=(32, 2))],
        [sg.Button('У кого 4', key='-4-', size=(15, 2)), sg.Button('У кого 5', key='-5-', size=(15, 2))],
        [sg.Button('Выход', key='-EXIT-', size=(32, 2))],
    ]


    window = sg.Window('Студентам', layout)


    while True:
        event, values = window.read()
        if event in [sg.WIN_CLOSED, '-EXIT-']:
            break
        elif event == '-DATA-':
            print_table(1, students, ['Студент', 'Группа', 'Ср. оценка'])
        elif event == '-4-':
            four_or_five(students, 4.0)
        elif event == '-5-':
            four_or_five(students, 5.0)

    window.close()
