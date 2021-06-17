from functools import reduce


def main():
    try:
        choice = list(
            map(int, input('Введите вариант и задание через пробел: ').split()))

        if choice[0] == 1:
            a = int(input("Введите A: "))
            b = int(input("Введите B: "))
            c = int(input("Введите C: "))
            if choice[1] == 1:
                k = int(input("Введите K: "))
            elif choice[1] == 2:
                d = int(input("Введите D: "))
                k = int(input("Введите K: "))
            elif choice[1] == 4:
                d = int(input("Введите D: "))
                f = int(input("Введите F: "))
        elif choice[0] == 2:
            someList = list(input("> ").split())
        else:
            someList = list(map(int, input("> ").split()))

        tasks = {
            1: {
                1: lambda: abs(((a**2 / b**2) + (c**2 * a**2)) / (a + b + c * (k - a / b**3)) + c + (k/b - k/a)*c),
                2: lambda: abs(((a**2 - b**3 - c**3 * a**2) * (b - c + c * (k - d / b**3)) - (k / b - k / a) * c)**3 - 20000),
                3: lambda: abs(1 - a * b**c - a * (b**2 - c**2) + (b - c + a) * (12 + b) / (c - a)),
                4: lambda: abs(a - b * c * d**3 + (c**5 - a**2)/a + f**3 * (a - 213)),
            },
            2: {
                1: lambda: '\n\t'.join(someList[::2]),
                2: lambda: '\n\t'.join(someList[1::2]),
                3: lambda: ' '.join(someList[::2]),
                4: lambda: ' '.join(someList[1::2]),
            },
            3: {
                1: lambda: sum([i for i in someList if i > 10]),
                2: lambda: sum([i for i in someList if 10 > i > 1]),
                3: lambda: reduce(lambda x, y: x*y, [i for i in someList if i < 10]),
            },
            4: {
                1: lambda: max(someList),
                2: lambda: min(someList),
                3: lambda: float(sum(someList)) / max(len(someList), 1),
                4: lambda: someList[len(someList) // 2],
            }
        }

        print(f'Ответ:\n\t{tasks[choice[0]][choice[1]]()}')
    except Exception as e:
        print(f"Ошибка! {e}")


if __name__ == '__main__':
    main()
