import PySimpleGUI as sg


# matrix = [
#     [sg.Text('1    2    3    4    5    6    7    8')],
#     [sg.Text('8    7    6    5    4    3    2    1')],
#     [sg.Text('2    3    4    5    6    7    8    9')],
#     [sg.Text('9    8    7    6    5    4    3    2')],
#     [sg.Text('1    3    5    7    9    7    5    3')],
#     [sg.Text('3    1    5    3    2    6    5    7')],
#     [sg.Text('1    7    5    9    7    3    1    5')],
#     [sg.Text('2    6    3    5    1    7    3    2')],
# ]

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


for row in range(0, len(matrix)):
    for item in range(0, len(matrix[row])):
        matrix[row][item] = f'  {matrix[row][item]}  '


matrix_table = [[sg.Listbox(
    values=matrix,
    key='-TABLE-',
    size=(250, 250)
)]]


funcs_column = [
	[sg.Button('Умножение по строкам', size=(20, 2), key='-MUL-')],
	[sg.Button('Сложение элементов', size=(20, 2), key='-SUM-')],
	[sg.Button('Сравнение сумм элементов < 5 и >= 5', size=(20, 2), key='-COM-')],
	[sg.Button('Все нули', size=(20, 2), key='-ZERO-')],
]

layout = [
    [
        sg.Column(matrix_table, element_justification='c'),
        sg.Column(funcs_column)
    ],
    [sg.Button('Выход', key='-EXIT-')],
]


window = sg.Window('Решатель десятой лабы Mark II',
                   layout, element_justification='r')

while True:
    event, values = window.read()
    if event in [sg.WIN_CLOSED, '-EXIT-']:
        break
    elif event == '-ZER0-':
        for row in range(0, len(matrix)):
            for item in range(0, len(matrix[row])):
                matrix[row][item] = '  0  '
        
        window.Element('-MATRIX-').Update(values=matrix)


window.close()

