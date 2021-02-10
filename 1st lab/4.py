yourChoice = int(input("Какой вариант вы хотите выбрать (1 / 2 / 3 / 4): "))

def options(yourChoice):
    someList = list(map(int, input("Введите числа: ").split()))
    if yourChoice == 1:
        result = someList[0]
        for i in someList:
            if i > result:
                result = someList[i]
        return result
    if yourChoice == 2:
        result = someList[0]
        for i in someList:
            if i < result:
                result = someList[i]
        return result
    if yourChoice == 3:
        result = 0
        for i in someList:
            result += i
        result = result / len(someList)
        return result
    if yourChoice == 4:
        index = len(someList) // 2
        return someList[index]

print(options(yourChoice))