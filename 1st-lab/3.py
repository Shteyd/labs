yourChoice = int(input("Какой вариант вы хотите выбрать (1 / 2 / 3 / 4): "))

def options(yourChoice):
    someList = list(map(int, input("Введите числа: ").split())); result = 0
    if yourChoice == 1:
        for i in someList:
            if i > 10:
                result += i
        return result
    if yourChoice == 2:
        for i in someList:
            if 10 > i > 1:
                result += i
        return result
    if yourChoice == 3 or 4:
        result += 1
        for i in someList:
            if i < 10:
                result *= i
        return result

print(options(yourChoice))