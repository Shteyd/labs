import PySimpleGUI as sg


sg.theme('DarkPurple6')
def new_choice():
    layout = [
        [sg.Button('1', key='-1-', size=(15, 7)), sg.Button('2', key='-2-', size=(15, 7))],
    ]

    window = sg.Window(' ', layout)

    while True:
        event, values = window.read()
        if event is sg.WIN_CLOSED:
            window.close()
            break
        elif event == '-1-':
            window.close()
            return 1
        elif event == '-2-':
            window.close()
            return 2
