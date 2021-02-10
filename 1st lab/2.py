yourChoice = int(input("Какой вариант вы хотите выбрать (1 / 2 / 3 / 4): "))

def options(yourChoice):
    someList = list(input("Введите текст: ").split())
    if yourChoice == 1:
        for i in range(0, len(someList)):
            if i % 2 == 0:
                print(someList[i])
    if yourChoice == 2:
        for i in range(0, len(someList)):
            if i % 2 == 1:
                print(someList[i])
    if yourChoice == 3:
        listOfEvenElements = []
        for i in range(0, len(someList)):
            if i % 2 == 0:
                listOfEvenElements.append(someList[i])
        
        print("".join(listOfEvenElements))
    if yourChoice == 3:
        listOfEvenElements = []
        for i in range(0, len(someList)):
            if i % 2 == 1:
                listOfEvenElements.append(someList[i])
        
        print("".join(listOfEvenElements))

options(yourChoice)