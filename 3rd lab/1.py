yourChoice = int(input("Какой вариант вы хотите выбрать (1 / 2 / 3 / 4): "))

def options(yourChoice):
    user_len = input().split()
    if yourChoice == 1:
        result = []
        for i in user_len:
            if i.isalpha() == False:
                i = i[:-1]
            if len(i) > 4:
                result.append(i)
        return " ".join(result)
    if yourChoice == 2:
        result = []
        for i in user_len:
            if len(i) < 2:
                continue
            if i[0] + i[1] == 'Ли':
                result.append(i)
        return ", ".join(result)
    if yourChoice == 3:
        result = []
        for i in user_len:
            if 11 > len(i) > 5:
                result.append(i)
        return ", ".join(result)
    if yourChoice == 4:
        result = []
        for i in user_len:
            if len(i) < 2:
                    continue
            if i[-2] + i[-1] == 'ов':
                result.append(i)
        return ", ".join(result)

print(options(yourChoice))