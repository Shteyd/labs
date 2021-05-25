from customer import customer
from library import library
from new import new
from train import train
from student import student
import PySimpleGUI as sg


sg.theme('DarkPurple6')

layout = [
    [sg.Button('Student', key='-Student-', size=(13, 6)), sg.Button('Train', key='-Train-', size=(13, 6)), sg.Button('New', key='-New-', size=(13, 6)),],
    [sg.Button('Library', key='-Library-', size=(13, 6)), sg.Button('Customer', key='-Customer-', size=(13, 6)), sg.Button('Выход', key='-EXIT-', size=(13, 6)),],
]


window = sg.Window(' ', layout)


while True:
    event, values = window.read()
    if event in [sg.WIN_CLOSED, '-EXIT-'] : break
    elif event == '-Student-' : student()
    elif event == '-Train-' : train()
    elif event == '-New-' : new()
    elif event == '-Library-' : library()
    elif event == '-Customer-' : customer()

window.close()
