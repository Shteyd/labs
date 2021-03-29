yourChoice = int(input("Какой вариант вы хотите выбрать (1 / 2 / 3 / 4): "))

def options(yourChoice):
    yourLen = input("Введите строку: ")
    if yourChoice == 1:
        newLen = ''
        for i in yourLen:
            if i.isdigit() == True:
                newLen += i
        return newLen
    if yourChoice == 2:
        newLen = ''
        for i in yourLen:
            if i.isalpha() == True:
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
            if i == ' ':
                continue
            if i.isdigit() == True:
                newLenDigits += i
            else:
                newLenLetters += i
        return newLenLetters, newLenDigits

print(options(yourChoice))