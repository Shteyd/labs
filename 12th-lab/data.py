import re
import json
import PySimpleGUI as sg
from difflib import SequenceMatcher


def getAllData():
    with open("./assets/teachers.json", "r", encoding="utf-8") as read_file:
        teachers_data = json.load(read_file)

    with open("./assets/subjects.json", "r", encoding="utf-8") as read_file:
        subjects_data = json.load(read_file)

    for counter in range(len(teachers_data)):
        listOfSubjects = []
        subjects_id = teachers_data[counter]['subjects']
        for item in subjects_id:
            for subject in subjects_data:
                if subject['subject_id'] == item:
                    listOfSubjects.append(subject['name'])
        teachers_data[counter]['subjects'] = "\n".join(listOfSubjects)
    
    teachers = []; subjects = []

    for row in teachers_data:
        local = []
        for item in row:
            local.append(row[item])
        teachers.append(local)

    for row in subjects_data:
        local = []
        for item in row:
            local.append(row[item])
        subjects.append(local)

    return teachers, subjects


def check_work(teachers, subjects, key):
    name = sg.popup_get_text("Введите ФИО преподавателя, которого хотите посмотреть")

    for teacher in teachers:
        ratio = SequenceMatcher(lambda x: x=="", name, teacher[1]).ratio()
        if ratio > 0.666:
            break
    
    if len(re.findall(r'\n', teacher[-1])) > 0:
        _subjects = teacher[-1].split('\n')
    else:
        _subjects = [teacher[-1]]

    listOfItems = []
    for item in _subjects:
        for subject in subjects:
            if item == subject[1] and subject[key] == True:
                listOfItems.append(item)
    
    if key == -2:
        if listOfItems == [] : sg.popup(f'У {teacher[1]} нет предметов, по которым предусмотрена курсовая работа')
        else : sg.popup(f'У {teacher[1]} есть возможность написания курсовых работ по следующим предметам:\n\t- ' + '\n\t- '.join(listOfItems))
    else:
        if listOfItems == [] : sg.popup(f'У {teacher[1]} нет предметов, по которым предусмотрена самостоятельная работа')
        else : sg.popup(f'У {teacher[1]} есть возможность написания самостоятельных работ по следующим предметам:\n\t- ' + '\n\t- '.join(listOfItems))


def check_pi(subjects):
    _subjects = []
    for subject in subjects:
        if re.findall(r'[Пп]', subject[1]) != []:
            _subjects.append(subject[1])

    if _subjects == [] : sg.popup(f'Дисциплин, в названии которых есть буква "П", нет')
    else : sg.popup(f'Список всех дисциплин, в названии которых встречается буква "П":\n\t- ' + '\n\t- '.join(_subjects))
