from data import check_pi, check_work, getAllData
import PySimpleGUI as sg


sg.theme('DarkPurple6')
teachers, subjects = getAllData()


teachers_column = [
    [
        sg.Table(
            values=teachers,
            headings=['№', 'Имя', 'Предметы'],
            justification='l',
            num_rows=10,
            row_height=35,
            auto_size_columns=False,
            col_widths=[3, 20, 32],
            size=(250, 250)
        )
    ]
]


subjects_column = [
    [
        sg.Table(
            values=subjects,
            headings=['№', 'Имя', 'Лекций', 'Практик'],
            justification='l',
            num_rows=10,
            row_height=35,
            auto_size_columns=False,
            col_widths=[3, 32, 10, 10],
            size=(250, 250)
        )
    ]
]


buttons_column = [
    sg.Button('Наличие курсовых', key='-COURSE-', size=(31, 3)),
    sg.Button('Наличие самостоятельных', key='-INDEPENDENT-', size=(31, 3)),
    sg.Button('Наличие "П" в предмете', key='-PI-', size=(31, 3)),
    sg.Button('Выход из программы', key='-EXIT-', size=(31, 3))
]


layout = [
    [
        sg.Column(teachers_column),
        sg.Column(subjects_column),
    ],
    buttons_column

]


window = sg.Window('12ая лаба', layout)
            

while True:
    event, values = window.read()
    if event in [sg.WIN_CLOSED, '-EXIT-']:
        break
    elif event == '-COURSE-':
        check_work(teachers, subjects, -2)
    elif event == '-INDEPENDENT-':
        check_work(teachers, subjects, -1)
    elif event == '-PI-':
        check_pi(subjects)

window.close()

