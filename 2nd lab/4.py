from string import digits, ascii_letters

yourChoice = int(input("Какой вариант вы хотите выбрать (1 / 2 / 3 / 4): "))

def options(yourChoice):
    letters = 'йцукенгшщзхъфывапролджэячсмитьбюЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮёЁ'
    yourLen = input("Введите строку: ")
    if yourChoice == 1:
        newLen = ''
        for i in yourLen:
            if i in digits:
                newLen += i
        return newLen
    if yourChoice == 2:
        newLen = ''
        for i in yourLen:
            if i in ascii_letters or letters:
                newLen += i
        return newLen
    if yourChoice == 3:
        for i in yourLen:
            if i == 'Л':
                newLen += i
        return newLen
    if yourChoice == 4:
        newLenLetters = ''
        newLenDigits = ''
        for i in yourLen:
            if i in digits:
                newLenDigits += i
            else:
                newLenLetters += i
        return newLenLetters, newLenDigits

print(options(yourChoice))