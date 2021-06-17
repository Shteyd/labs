from random import randint, sample
from string import ascii_letters, digits


def main():
    choice = list(
            map(int, input('Введите вариант и задание через пробел: ').split()))

    if choice[0] == 1 : my_number = randint(0, 100)
    elif choice[0] == 2 : yourLens = input("Введите несколько строк: ").split()
    elif choice[0] == 4 : yourLen = input("Введите строку: ")

    def __random(key):
        user_number = int(input("Введите число (0-100): "))
        if key == 1:
            if user_number > my_number : return user_number
        elif key == 2:
            if user_number == my_number : return user_number
        elif key == 3:
            if user_number != my_number : return user_number
        elif key == 4:
            if user_number < my_number : return user_number
        return __random(key)

    tasks = {
        1: lambda: f'\nВаше число: {__random(choice[1])}\nЧисло компьютера:{my_number}',
        2: {
            1: lambda: ', '.join([i for i in yourLens if 10 > len(i) > 5]),
            2: lambda: ', '.join([i for i in yourLens if len(i) < 10]),
            3: lambda: ', '.join([i for i in yourLens if i[-1] == 'r']),
            4: lambda: ', '.join([i for i in yourLens if i[0] == 'r']),
        },
        3: {
            1: lambda: ''.join([chr(randint(1040, 1072)) for _ in range(5)]),
            2: lambda: ''.join(['R' * int(input("Введите N: "))]),
            3: lambda: ''.join(str(randint(10000, 99999)) + '3'),
            4: lambda: ''.join(sample(ascii_letters + digits, 7) + list(str(randint(0,9))))
        },
        4: {
            1: lambda: ''.join([i for i in yourLen if i.isdigit() == True]),
            2: lambda: ''.join([i for i in yourLen if i.isalpha() == True]),
            3: lambda: ''.join([i for i in yourLen if i == 'Л']),
            4: lambda: ''.join([i for i in yourLen if i.isalpha() == True]) + ', ' + ''.join([i for i in yourLen if i.isdigit() == True])
        }
    }; print('Ответ:', tasks[choice[0]][choice[1]]() if choice[0] != 1 else tasks[choice[0]]())

if __name__ == '__main__':
    main()