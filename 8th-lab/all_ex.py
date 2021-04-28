import csv
import re


students = {}

with open("./data/students.csv", "r", encoding='utf-8') as csvfile:
    student_reader = csv.reader(csvfile, delimiter=';')
    for row in student_reader:
        students[row[0]] = row[1:]

del students['№']

logo = """
░█████╗░████████╗██╗░░██╗  ██╗░░░░░░█████╗░██████╗░
██╔══██╗╚══██╔══╝██║░░██║  ██║░░░░░██╔══██╗██╔══██╗
╚█████╔╝░░░██║░░░███████║  ██║░░░░░███████║██████╦╝
██╔══██╗░░░██║░░░██╔══██║  ██║░░░░░██╔══██║██╔══██╗
╚█████╔╝░░░██║░░░██║░░██║  ███████╗██║░░██║██████╦╝
░╚════╝░░░░╚═╝░░░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═════╝░

           █▀█ █▀█ █▀█ █▀▀ █▀█ ▄▀█ █▀▄▀█
           █▀▀ █▀▄ █▄█ █▄█ █▀▄ █▀█ █░▀░█
"""


def ex1():
    choice = input("Введите ФИО студента: ")
    for num in students:
        student = students.get(num)
        if choice in student:
            age = int(student[1])
            student[1] = str(age + 1)
            students[num] = student
    return students

def ex2():
    choice = input("Введите ФИО студента: ")
    for num in students:
        student = students.get(num)
        if choice in student:
            name = input("Введите новое ФИО студента: ")
            student[0] = name
            students[num] = student
    return students

def ex3():
    choice = input("Введите номер студента: ")
    student = students.get(choice)
    age = int(student[1]) + 1
    student[1] = str(age)
    students[choice] = student
    return students

def ex4():
    choice = input("Введите ФИО студента: ")
    for num in students:
        student = students.get(num)
        if choice in student:
            group = input("Введите новую группу: ")
            student[-1] = group
            students[num] = student
    return students

def ex5():
    choice = input("Введите номер студента: ")
    del students[choice]
    return students

def ex6():
    for key in list(students.keys()):
        student = students.get(key)
        if student[1] > '22':
            age = int(student[1]) - 1
            student[1] = str(age)
            students[key] = student
    return students

def ex7():
    new_students = {}
    for key in list(students.keys()):
        student = students.get(key)
        if student[1] == '23':
            continue
        new_students[key] = student
    return new_students

def ex8():
    for key in list(students.keys()):
        student = students.get(key)
        if student[0].split()[0] == 'Иванов':
            age = int(student[1]) + 1
            student[1] = str(age)
            students[key] = student
    return students

def ex9():
    for key in list(students.keys()):
        student = students.get(key)
        if student[0].split()[0] == 'Иванов':
            name = student[0].split()[1]
            last_name = student[0].split()[2]
            student[0] = f'Сидоров {name} {last_name}'
            students[key] = student
    return students

def ex10():
    for key in students:
        student = students.get(key)
        group = student[-1]
        student[-1] = student[0]
        student[0] = group
        students[key] = student
    return students


def print_data(data_key):
    data = {
        1 : [[key, students.get(key)] for key in list(students.keys())[1:] if students.get(key)[-1] == 'БО-111111'],
        2 : [[key, students.get(key)] for key in list(students.keys())[1:] if int(key) in range(1, 11)],
        3 : [[key, students.get(key)] for key in list(students.keys())[1:] if students.get(key)[1] == '22'],
        4 : [[key, students.get(key)] for key in list(students.keys())[1:] if students.get(key)[0].split()[0] == 'Иванов'],
        5 : [[key, students.get(key)] for key in list(students.keys())[1:] if re.findall(r'а$', students.get(key)[0].split()[0]) == list('а')],
        6 : [[key, students.get(key)] for key in list(students.keys())[1:] if int(students.get(key)[1])%2 == 0],
        7 : [[key, students.get(key)] for key in list(students.keys())[1:] if len(re.findall(r'[5]', students.get(key)[1])) > 0],
        8 : [[key, students.get(key)] for key in list(students.keys())[1:] if len(re.findall(r'\d+$', students.get(key)[-1])[0]) > 7],
        9 : [[key, students.get(key)] for key in list(students.keys())[1:] if int(key)%2 == 0],
        10 : [[key, students.get(key)] for key in list(students.keys())[1:] if re.findall(r'\d$', students.get(key)[-1]) == list('1')],
    }; return data.get(data_key)



def all_ex(choice):
    exs = {
        '1': ex1, '5': ex5, '9': ex9,
        '2': ex2, '6': ex6, '10': ex10,
        '3': ex3, '7': ex7,
        '4': ex4, '8': ex8,
    }
    return exs.get(choice)()
