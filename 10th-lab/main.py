import PySimpleGUI as sg


sg.theme('DarkPurple6')


def zero():
    matrix_table = ''
    for row in range(len(matrix)):
        for item in range(len(matrix[row])):
            matrix[row][item] = 0
            matrix_table += f'0\t'
        matrix_table += '\n\n\n'
    window.Element('-MATRIX-').Update(matrix_table)


def multi():
    number = int(sg.popup_get_text('Введите число, на которое хотите умножить матрицу:', title=' '))
    matrix_table = ''
    for row in range(len(matrix)):
        for item in range(len(matrix[row])):
            matrix[row][item] *= number 
            matrix_table += f'{matrix[row][item]}\t'
        matrix_table += '\n\n\n'
    window.Element('-MATRIX-').Update(matrix_table)


def sum_items():
    sum = 0
    for row in matrix:
        for item in row:
            sum += item
    sg.popup(f'Сумма всех элементов: {sum}', title=' ')


def compare():
    sumL = 0; sumH = 0
    for row in matrix:
        for item in row:
            if item < 5:
                sumL += item
            else:
                sumH += item
    if sumL > sumH:
        sg.popup(f'Сумма чисел < 5: {sumL}')
    else:
        sg.popup(f'Сумма чисел >= 5: {sumH}')


matrix = [
    [1, 2, 3, 4, 5, 6, 7, 8],
    [8, 7, 6, 5, 4, 3, 2, 1],
    [2, 3, 4, 5, 6, 7, 8, 9],
    [9, 8, 7, 6, 5, 4, 3, 2],
    [1, 3, 5, 7, 9, 7, 5, 3],
    [3, 1, 5, 3, 2, 6, 5, 7],
    [1, 7, 5, 9, 7, 3, 1, 5],
    [2, 6, 3, 5, 1, 7, 3, 2],
]

matrix_table = ''

for row in matrix:
    for item in row:
        matrix_table += f'{item}\t'
    matrix_table += '\n\n\n'

students_table = [[sg.Text(
    text=matrix_table,
    key='-MATRIX-'
)]]

funcs_column = [
	[sg.Button('Умножение по строкам', size=(30, 5), key='-MULTI-', border_width=5)],
	[sg.Button('Сумма всех элементов', size=(30, 5), key='-SUM-', border_width=5)],
	[sg.Button('Сравнение сумм', size=(30, 5), key='-COMPARE-', border_width=5)],
	[sg.Button('Замена всех элементов на 0', size=(30, 5), key='-ZERO-', border_width=5)],
    [sg.Button('Выход', key='-EXIT-'),],
]

layout = [
    [
        sg.Column(students_table),
        sg.Column(funcs_column, element_justification='r')
    ],
]


window = sg.Window('10ая лаба',
                    layout,
                    element_justification='r',
                    alpha_channel=0.9,)


while True:
    event, values = window.read()
    if event in [sg.WIN_CLOSED, '-EXIT-']:
        break
    elif event == '-MULTI-':
        multi()
    elif event == '-SUM-':
        sum_items()
    elif event == '-COMPARE-':
        compare()
    elif event == '-ZERO-':
        zero()


window.close()
